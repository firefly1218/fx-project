# 上传图片到七牛云
"""上传文件"""
# from qiniu import Auth, put_file, etag
# # 需要填写你的 Access Key 和 Secret Key
# access_key = 'aIavMGtmD-MjSUk-F7ZykNrLXPrRfNTl9PaYP8R_'
# secret_key = 'jvM8JWU5-2m8R7SSFcFXahNUuIfGQ4XspKS4Hqmc'
# # 构建鉴权对象
# q = Auth(access_key, secret_key)
# # 要上传的空间
# bucket_name = 'xiaochengxuimage'
# # 上传到七牛后保存的文件名
# key = 'my-python-logo1.png'
# # 生成上传 Token，可以指定过期时间等
# token = q.upload_token(bucket_name, key, 3600)
# # 要上传文件的本地路径
# localfile = '001.jpg'
# ret, info = put_file(token, key, localfile)
# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)
# 获取七牛云下载url
# import requests
# from qiniu import Auth
# access_key = 'aIavMGtmD-MjSUk-F7ZykNrLXPrRfNTl9PaYP8R_'
# secret_key = 'jvM8JWU5-2m8R7SSFcFXahNUuIfGQ4XspKS4Hqmc'
# q = Auth(access_key, secret_key)
# # 有两种方式构造base_url的形式
# bucket_domain = 'pbsbxy7id.bkt.clouddn.com'
# key = 'my-python-logo.png'
# base_url = 'http://%s/%s' % (bucket_domain, key)
# # 或者直接输入url的方式下载
# # base_url = 'http://domain/key'
# # 可以设置token过期时间
# private_url = q.private_download_url(base_url, expires=3600)
# print(private_url)
# return success_resp({'data':private_url})
