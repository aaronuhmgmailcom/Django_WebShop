import html
import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from tools.login_dec import login_check
from .models import Topic
from users.models import User
from tools.login_dec import get_user_by_request

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

        return JsonResponse({'code':200,'username':author.username})

    def make_topics_res(self,author,author_topics):
        topics_res=[]
        for topic in author_topics:
            d={}
            d['id']=topic.id
            d['title']=topic.title
            d['category']=topic.category
            d['introduce']=topic.introduce
            d['create_time']=topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
            d['author']=author.nickname
            topics_res.append(d)
        res={'code':200,'data':{}}
        res['data']['topics']=topics_res
        res['data']['nickname']=author.nickname
        return res

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

        p = request.GET.get('category')
        category_exist = False
        if p in ['tec','no-tec']:
            category_exist = True

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



