from django.core.cache import cache
from .login_dec import get_user_by_request

def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request, *args, **kwargs):
            # tedu/topics?t_id=1&a=100&b=200
            # GET  {'t_id':1,'a':100,'b':200}
            # keys() ['t_id','a','b']
            if 't_id' in request.GET.keys():
                # 文章详情页直接调用
                # return get(request, *args, **kwargs)：
                return func(request, *args, **kwargs)
            # 文章列表页设置缓存
            # 是博主访问自己吗？
            # 访问者
            visitor_username = get_user_by_request(request)
            # 谁的文章
            # 装饰器修饰的get方法
            # def get(self, request, author_id):

            # 拿的是path转换器传递给get方法的参数
            author_username = kwargs['author_id']
            print('访问者:%s,作者:%s' % (visitor_username,
                                    author_username))
            if visitor_username == author_username:
                # 博主访问
                cache_key = 'topic_cache_self_%s' % (request.get_full_path())
            else:
                # 非博主访问
                cache_key = 'topic_cache_%s' % (request.get_full_path())
            print('---cache key is %s--' % (cache_key))
            # 缓存思想
            res = cache.get(cache_key)
            if res:
                print('-------cache in--------')
                return res
            # 修饰的是get方法，所以以下语句就是对get方法的调用
            res = func(request, *args, **kwargs)
            # 将get方法返回的数据写入到缓存，
            cache.set(cache_key, res, expire)
            return res

        return wrapper

    return _topic_cache