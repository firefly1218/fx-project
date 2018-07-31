"""
    主要接收图片识别,处理,返回处理后的图片数据以及相关infomations
    face++API图片要求:
        图片格式：JPG(JPEG)，PNG
        图片像素尺寸：最小 48*48 像素，最大 4096*4096 像素
        图片文件大小：2 MB
        最小人脸像素尺寸： 系统能够检测到的人脸框为一个正方形，正方形边长的最小值为图像短边长度的 48 分之一，最小值不低于 48 像素。 例如图片为 4096*3200 像素，则最小人脸像素尺寸为 66*66 像素。
"""
import time
from django.shortcuts import render
from utils.commom import *
from utils.faceAPI import *
from utils.baiduAPI import *

from utils.handle_image_px import *
from django.http import HttpResponse
import time
from qiniu import Auth, put_file, etag
import qiniu.config
from xiaochengxu.settings import *
from .functions import *



def index(request):
    """
    主页,对url的测试
    :param request:
    :return:
    """
    return render(request, 'index.html', locals())


def yanzhi_api(request):
    """
    颜值测试目前使用的是第三方接口: face++
    功能: 接收用户上传的照片数据,然后经过处理后通过一种渠道返回给用户(前端)
    接口测试 : http://172.17.36.119:8080/xcxapi/test/
    :param request:
    :return:
    """
    print('\n\n来了一个请求...',request.request_type)
    start_time = time.time()
    # 接收用户上传的图片并保存下来
    try:
        print('网络状态不佳,正在接收文件中...')
        file = request.FILES['image_file']
    except:
        print('获取图片失败!')
        return faild_resp(None, '未携带图片数据或者图片格式不正确!')

    print('file_name:',file.name)
    # print('file:', type(file))
    # 将接收到的图片数据保存到本地
    image_path = BASE_DIR + '/static/images/'+'007'+'.jpg'

    with open(image_path, 'wb') as f:   # str(time.time())
        for data in file.chunks():
            f.write(data)
        else:
            print('已成功持久化!')
    # 读取用户保存到本地的图片数据(二进制)
    # return success_resp({'status':1})
    # image_path = '/home/python/Desktop/workplace/xiaochengxu/static/images/007.jpg'

    # 将上传过来的图片进行base64编码,返回的private_url就是编码过后的字符串
    binary_image_data = open(image_path, 'rb').read()
    private_url = base64_encode(binary_image_data)
    # 初始化返回数据
    response_data = {'data': private_url}

    """
    在图片上传到face++API识别之前需要对不合格的图片进行压缩处理
    """
    # 先验证图片大小
    file_path = BASE_DIR + '/static/images/007.jpg'
    res = verification_image(file_path)

    if res >=1:
        # 进行图片压缩
        print('图片大小超过2M,不符合faceAPI的要求!')
        com_res = compress_image()
        if com_res:
            print('图片压缩成功!')
            # 成功压缩后更改新的图片路径
            file_path = BASE_DIR + '/static/compress_images/007.jpg'
        else:
            print('图片压缩失败!')
            return faild_resp(None, '图片压缩失败!')
    else:
        print('图片大小符合要求!即将转入识别系统...')

    try:
        face_time = time.time()
        # 处理用户保存的数据
        import json
        res = face_api(file_path)  # 有两个参数image_name, image_url
        print('face++api识别结果:',res)
        # print(res.content.decode('utf-8'))
        attributes = json.loads(res.content.decode('utf-8'))['faces'][0]['attributes']
        # print('attributes:', attributes)
        emotion = attributes['emotion']
        beauty = attributes['beauty']
        gender = attributes['gender']['value']
        beauty_score = int((beauty['female_score'] + beauty['male_score'])/2)
        if beauty_score >= 85 and gender == 'Female':
            beauty_score = '哇! 厉害了小仙女,你的颜值超过了'+ str(beauty_score) +'%的女性!遇见你,真开心!^_^'
        elif beauty_score >= 85 and gender == 'Male':
            beauty_score = '哇! 厉害了帅哥,你的颜值超过了'+ str(beauty_score) +'%的男性!遇见你,真开心!^_^'

        elif 70 <= beauty_score < 85 and gender == 'Female':
            beauty_score = '哇! 美女,你的颜值超过了'+ str(beauty_score) +'%的女性!遇见你,真开心!'
        elif 70 <= beauty_score < 85 and gender == 'Male':
            beauty_score = '哇! 帅哥,你的颜值超过了'+ str(beauty_score) +'%的男性!遇见你,真开心!'

        elif 60 <= beauty_score < 70 and gender == 'Female':
            beauty_score = '哇! 你的颜值超过了'+ str(beauty_score) +'%的女性!传说,提升颜值的最好办法就是加美颜!'
        elif 60 <= beauty_score < 70 and gender == 'Male':
            beauty_score = '哇! 你的颜值超过了'+ str(beauty_score) +'%的男性!传说,提升颜值的最好办法就是加美颜!'

        else:
            beauty_score = '亲, 你的颜值超过了'+ str(beauty_score) +'%的人!换个姿势再拍一张吧!'

        print('the people emotion info:',emotion)
        value_list = []
        for item in emotion.items():
            value_list.append(item[1])
        else:
            value_list.sort(reverse=True)
            emotion_value = value_list[0]  # 先将列表中的值排序,取其最大的
            # print('max_value', emotion_value)
            peoson_emotion = list(emotion.keys())[list(emotion.values()).index(emotion_value)]  # 获取字典中最大值对应的键名
    except Exception as r:
        print(r)
        print('图片识别出现异常!')
        return faild_resp(None, '图片识别出现异常!')
    else:
        # return HttpResponse(image_data, content_type='image/jpeg')
        # 如果识别成功,则在返回json中添加识别结果,然后再返回
        response_data['person_emotion'] = peoson_emotion
        response_data['emotion_value'] = emotion_value
        response_data['beauty_value'] = beauty_score
        print('识别耗时:', round(time.time()-face_time, 3),'秒')
        print('总共耗时:', round(time.time()-start_time, 3),'秒')

    return success_resp(response_data)



def pipei_api(request):
    """
    匹配度测试目前使用的是百度AI接口
    这个api是用于接收两张图片(或者是一张图片的两个人的合影)来测试来个人的匹配度的api
    :param request:
    :return:
    """
    print('\n\n来了一个请求...',request.request_type)
    try:
        print('网络状态不佳,正在接收文件中...')
        pic1 = request.FILES['image_file1']
        pic2 = request.FILES['image_file2']
    except:
        print('获取图片失败!')
        return faild_resp(None, '未携带图片数据或者图片格式不正确!')
    else:
        pic1_data = pic1.read()
        pic2_data = pic2.read()

    print('即将进入识别模块!')
    result = face_match(pic1_data, pic2_data)  # 将发送到服务器的图片缓存数据直接传送到识别模块,并接收识别结果
    print('result:', result)
    if result:
        try:
            score = result['result']['score']
            print('score:', score)
        except:
            print('识别失败!刘姥姥来了')
            return faild_resp(None, '图片识别失败!')
        else:
            private_url_dic = {}
            private_url_dic['image1'] = base64_encode(pic1_data)
            private_url_dic['image2'] = base64_encode(pic2_data)

            response_data = {'match_value':score, 'images':private_url_dic}
            return success_resp(response_data)
    else:
        print('没有result')
        return faild_resp(None, '图片识别失败!')
