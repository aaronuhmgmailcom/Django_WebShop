from django.http import JsonResponse
from django.shortcuts import render
from tools.login_dec import login_check
import json
from topic.models import Topic
from message.models import Message


# Create your views here.
@login_check
def message_view(request, topic_id):
    if request.method != 'POST':
        result = {'code': 10400, 'error': 'please use POST'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    content = json_obj['content']
    parent_id = json_obj.get('parent_id', 0)

    # 检查topic_id是否有效
    try:
        topic = Topic.objects.get(id=topic_id)
    except Exception as e:
        result = {'code': 10401, 'error': 'the topic id is error'}
        return JsonResponse(result)
    # 获取登录用户
    user = request.myuser
    Message.objects.create(topic=topic, content=content,
                           user_profile=user,
                           parent_message=parent_id)
    return JsonResponse({'code': 200})
