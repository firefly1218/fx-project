"""
    2018年7月5日 13:43:26
    这个文档是测试百度AI人脸识别使用的
    关于人脸识别Python SDK文档: http://ai.baidu.com/docs#/Face-Python-SDK/b9c843ac
                                https://ai.baidu.com/docs#/Face-Python-SDK/top
"""

from aip import AipFace   # 百度aip-python-sdk-2.2.4 安装后的 baidu-aip (2.2.4.0)
import base64
from PIL import Image, ImageDraw  # 根据特征点划线


api_id = '11577366'
api_key = 'sUGr2MyaMj8PGBUV0I8iuNdx'
secret_key = 'FRO27yCBatWMYtN3YoMe72GMIrBAeauR'




""" 你的 APPID AK SK """
APP_ID = api_id
API_KEY = api_key
SECRET_KEY = secret_key

client = AipFace(APP_ID, API_KEY, SECRET_KEY)  # 创建应用实例


# 开始使用识别功能


def face_match(pic1, pic2):
    """
        人脸对比
        接口能力: 评测两张图片的相似度/ 活体检测/ 多种图片类型/ 质量检测/
    """
    try:
        result = client.match([
            {
                'image': base64.b64encode(pic1).decode('utf-8'),  # # open(pic2, 'rb').read()  # 相当于前面的pic
                'image_type': 'BASE64',
            },
            {
                'image': base64.b64encode(pic2).decode('utf-8'),  # open(pic2, 'rb').read()
                'image_type': 'BASE64',
            }
        ])
    except Exception as re:
        print('识别模块出现故障:', re)
        return 0
    # print('res:', result)  # 对相似度测评打分,百分制
    return result




# # 检测图片中的人脸并标记出位置信息(接口测试)
# image = base64.b64encode(open('moni.jpg','rb').read()).decode('utf-8')  # 读取图片后base64加密，并解密成字符串形式
#
# imageType = "BASE64"
#
# """ 调用人脸检测 """
# client.detect(image, imageType)
#
# """ 如果有可选参数 """
# options = {}
# options["face_field"] = "age"
# options["max_face_num"] = 2
# options["face_type"] = "LIVE"
#
# """ 带参数调用人脸检测 """
# res = client.detect(image, imageType, options)
# # 人脸数据字典集合
# face_dic = res['result']['face_list'][0]['location']
#
# image_path = 'moni.jpg'
# image = Image.open(image_path)
# # 创建一个可以在给定图像上绘图的对象
# draw = ImageDraw.Draw(image)
#
# right = face_dic['left']+face_dic['width']
# bottom = face_dic['top']+face_dic['height']
#
# draw.polygon([(face_dic['left'], face_dic['top']),
#               (right, face_dic['top']),
#               (right, bottom),
#               (face_dic['left'], bottom)], outline=(255, 0, 0))
# image.show()

