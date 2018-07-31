from django.core.urlresolvers import reverse
# from utils.wrappers import *


# 记录用户访问url中间件
class CheckRequestMiddleware(object):

    def process_request(self, request):
        """请求预处理函数,名称固定"""
        full_path = request.get_full_path()

        print('来了request:', full_path)
        # # 定义不记录的url列表
        # exclue_urls = [
        #     reverse('users:login'),
        #     reverse('users:register'),
        #     reverse('users:login_handle'),
        #     reverse('users:register_handle'),
        #     reverse('users:index'),
        #     reverse('users:address'),
        #     reverse('users:order'),
        #     reverse('users:logout'),
        #     '/favicon.ico',
        # ]
        #
        # # localhost:8000/abc/123/?a=100
        #
        # # 判断用户请求的url是否在排除列表
        # if request.path not in exclue_urls and response.status_code == 200:
        #     # 记录url
        #     set_cookie(response, 'pre_url', request.get_full_path())

        # return request
        # 对请求预处理
        request.request_type = 'check'





















