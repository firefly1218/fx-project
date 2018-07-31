"""
    这个脚本使用来测试项目api接口的
    功能接口:图片上传
"""
import os
import requests
from requests_toolbelt import MultipartEncoder


def yanzhi():
    # 测试一张图片的接口(test接口)
    m = MultipartEncoder(
        fields={
            'test': '接收照片接口测试!',
            'image_file': ('./images/002.jpg', open('./images/002.jpg', 'rb'), 'image/jpeg')
        }
    )

    res = requests.post('http://192.168.2.167:8080/xcxapi/test/', data=m, headers={'Content-Type': m.content_type})

    # print('res: ',res.content.decode('utf-8'))
    # print(res.content.decode('utf-8'))
    print(res.text)


def pipei():
    # 测试一张图片的接口(test接口)
    m = MultipartEncoder(
        fields={
            'test': '接收照片接口测试!',
            'image_file1': ('./images/002.jpg', open('./images/002.jpg', 'rb'), 'image/jpeg'),
            'image_file2': ('./images/002.jpg', open('./images/002.jpg', 'rb'), 'image/jpeg'),
        }
    )

    # res = requests.post('http://192.168.2.167:8888/xcxapi/match/', data=m, headers={'Content-Type': m.content_type})
    res = requests.post('http://172.17.36.119/xcxapi/match/', data=m, headers={'Content-Type': m.content_type})

    # print('res: ',res.content.decode('utf-8'))
    # print(res.content.decode('utf-8'))
    print(res.text)

pipei()



# 将图片数据转换成base64编码
# import base64
# f=open(r'./images/001.jpg','rb') #二进制方式打开图文件
# ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
# f.close()
# print(ls_f)
