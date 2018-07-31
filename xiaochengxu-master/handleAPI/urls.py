
from django.conf.urls import url
from handleAPI import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'test/', csrf_exempt(views.yanzhi_api)),  # 小程序功能转接接口
    url(r'match/', csrf_exempt(views.pipei_api)),  # 小程序功能转接接口
    url(r'index/', csrf_exempt(views.index)),  # 小程序功能测试页面
]

