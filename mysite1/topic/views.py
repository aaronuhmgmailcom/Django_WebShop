import html
import json

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from tools.login_dec import login_check
from .models import Topic
from users.models import User
# from tools.login_dec import get_user_by_request
from tools.login_dec import get_user_by_request
from tools.cache_dec import topic_cache
from message.models import Message


class topic_views(View):
    @method_decorator(login_check)
    def post(self,request, author_id):
        json_str=request.body
        json_obj=json.loads(json_str)
        content=json_obj['content']
        content_text=json_obj['content_text']
        introduce=content_text[:20]
        title=json_obj['title']
        # title=html.escape(title)
        limit = json_obj['limit']
        if limit not in ['public','private']:
            result={'code':10300,'error':'this is not in limit'}
            return JsonResponse(result)
        category=json_obj['category']
        if category not in ['tec','no-tec']:
            result={'code':10301,'error':'the category is not in '}
            return JsonResponse(result)
        author = request.myuser

        Topic.objects.create(title=title,content=content,limit=limit,category=category,introduce=introduce,user_profile=author)
        self.clear_topic_caches(request)

        return JsonResponse({'code':200,'username':author.username})

    def make_topics_res(self,author,author_topics):
        topics_res=[]
        for topic in author_topics:
            d={}
            d['id']=topic.id
            d['title']=topic.title
            d['category']=topic.category
            d['introduce']=topic.introduce
            d['created_time']=topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
            d['author']=author.nickname
            topics_res.append(d)
        res={'code':200,'data':{}}
        res['data']['topics']=topics_res
        res['data']['nickname']=author.nickname
        return res

    def make_topic_res(self,author,author_topic,is_self):
        if is_self:
            next_topic=Topic.objects.filter(id__gt=author_topic.id,user_profile=author.id).first()
            last_topic = Topic.objects.filter(id__lt=author_topic.id, user_profile=author.id).last()
        else:
            next_topic = Topic.objects.filter(id__gt=author_topic.id, user_profile=author.id,limit='public').first()
            last_topic = Topic.objects.filter(id__lt=author_topic.id, user_profile=author.id,limit='public').last()
        if next_topic:
            next_id=next_topic.id
            next_title=next_topic.title
        else:
            next_id = None
            next_title = None
        if last_topic:
            last_id = last_topic.id
            last_title = last_topic.title
        else:
            last_id = None
            last_title = None

        all_message=Message.objects.filter(topic=author_topic).order_by('-created_time')
        # print(all_message)
        msg_list=[]
        r_dict={}
        msg_count=0
        for msg in all_message:
            if msg.parent_message:
                r_dict.setdefault(msg.parent_message,[])
                r_dict[msg.parent_message].append({'id':msg.id,'content':msg.content,'publisher':msg.user_profile.nickname,'publisher_avatar':str(msg.user_profile.IMAGE),'created_time':msg.created_time.strftime('%Y-%m-%d %H:%M:%S')})
            else:
                msg_count+=1
                msg_list.append({
                    'id':msg.id,
                    'content':msg.content,
                    'publisher':msg.user_profile.nickname,
                    'publisher_avatar':str(msg.user_profile.IMAGE),
                    'created_time':msg.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'reply':[]
                })

        for l in msg_list:
            if l['id'] in r_dict:
                l['reply']=r_dict[l['id']]

        d = {'code': 200, 'data': {}}
        d['data']['id'] = author_topic.id
        d['data']['nickname'] = author.nickname
        d['data']['title'] = author_topic.title
        d['data']['category'] = author_topic.category
        d['data']['content'] = author_topic.content
        d['data']['introduce'] = author_topic.introduce
        d['data']['author'] = author.nickname
        d['data']['created_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        d['data']['last_id'] =last_id
        d['data']['last_title'] = last_title
        d['data']['next_id'] = next_id
        d['data']['next_title'] = next_title
        d['data']['messages'] = msg_list
        d['data']['messages_count'] =msg_count
        return d

    def clear_topic_caches(self,request):
        all_path=request.get_full_path()
        all_key_p=['topic_cache_self_','topic_cache_']
        all_key=[]
        for key_p in all_key_p:
            for key_h in ['','?category=tec','?category=no-tec']:
                all_key.append(key_p+all_path+key_h)
        print(all_key)
        cache.delete_many(all_key)

    @method_decorator(topic_cache(60))
    def get(self, request, author_id):
        try:
            author = User.objects.get(username=author_id)
        except Exception as e:
            result = {'code': 10305, 'error': 'the author id is error'}
            return JsonResponse(result)
        # 返回文章列表前，确定访问者的身份
        # 如果是博主本身访问，返回所有文章
        # 如果非博客主人访问，只返回公开的文章
        # 从token中获取用户信息【博主】
        visitor_username = get_user_by_request(request)
        t_id=request.GET.get('t_id')
        is_self=False #是否博主访问自己
        if t_id:
            #获取文章详情
                #博主访问自己，可以看所有文章
            if visitor_username==author_id:
                is_self=True

                try:
                    author_topic=Topic.objects.get(id=t_id,user_profile=author.id)
                except Exception as e:
                    result={'code':10310,'error':'topic id is wrong'}
            else:#非博主只能看PUBLIC的
                try:
                    author_topic= Topic.objects.get(id=t_id,user_profile=author.id,limit = 'public')
                except Exception as e:
                    result ={'code':10310,'error':'the topic is error'}

            result = self.make_topic_res(author, author_topic, is_self)
            return JsonResponse(result)
        else:
            p = request.GET.get('category')
            category_exist = False
            if p in ['tec','no-tec']:
                category_exist = True
                result = {''}


            if author_id == visitor_username:
                # 博主访问自己的博客(返回个人+公开的文章)
                if not category_exist:
                    author_topics = Topic.objects.filter(user_profile=author.id)
                else:
                    author_topics = Topic.objects.filter(user_profile=author.id,
                                                          category=p)
            else:
                # 只返回该用户公开的文章
                if not category_exist:
                    author_topics = Topic.objects.filter(user_profile=author.id,
                                                     limit='public', )
                else:
                    author_topics = Topic.objects.filter(user_profile=author.id,
                                                     limit='public', category=p)

            # 按照一定的格式返回
            res = self.make_topics_res(author, author_topics)
            return JsonResponse(res)



