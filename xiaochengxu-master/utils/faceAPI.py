"""
    站点: face++
    Detect API 测试
    文档地址:https://console.faceplusplus.com.cn/documents/4888373
    api_key = u1J22B8-bBXdMzlXDQ0kvUeDW6CaD1cA
    API Secret = rnTucxX32urrZT37uTidTswnS30Pnrht
    调用url [post]: https://api-cn.faceplusplus.com/facepp/v3/detect
"""


from requests_toolbelt import MultipartEncoder  # 需要上传文件中的数据
import requests


def face_api(image_path):
    api_key = 'u1J22B8-bBXdMzlXDQ0kvUeDW6CaD1cA'
    tar_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    #
    # data = {
    #     'api_key':api_key,
    #     'api_secret':'rnTucxX32urrZT37uTidTswnS30Pnrht',
    #     # 'image_url':'https://qcloudtest-1257020556.cos.ap-guangzhou.myqcloud.com/1530517069597-B1IILUPzQ.jpg',
    #         'image_url':'https://qcloudtest-1257020556.cos.ap-guangzhou.myqcloud.com/1530518138392-SJfY9UDfX.jpg',
    #     'return_landmark':2,
    #     'return_attributes':'gender,age,smiling,headpose,blur,eyestatus,emotion,ethnicity,beauty,eyegaze,skinstatus'
    # }
    #
    # res = requests.post(tar_url, data=data, timeout=3)
    #
    # print('res: ', res.content.decode('utf-8'))


    # import struct  # 打包二进制文件

    # 使用python的requests 发送multipart/form-data 请求  参考:https://blog.csdn.net/win_turn/article/details/77744687


    m = MultipartEncoder(
        fields={
        'api_key': api_key, 'api_secret': 'rnTucxX32urrZT37uTidTswnS30Pnrht',
            'return_landmark':'2',
            'return_attributes':'gender,age,smiling,headpose,blur,eyestatus,emotion,ethnicity,beauty,eyegaze,skinstatus',
            'image_file': (image_path, open(image_path, 'rb'),'image/jpeg')} # 'image/jpeg'content-type可以忽略, 这个地方是需要
        )

    res = requests.post(tar_url, data=m,headers={'Content-Type':m.content_type})

    print('res:', res.content.decode('utf-8'))  # 查看返回结果

    # print(type(open('chenduling.jpg', 'rb').read()))
    return res

image_path = '/home/python/Desktop/workplace/xiaochengxu/static/images/008.jpg'
face_api(image_path)