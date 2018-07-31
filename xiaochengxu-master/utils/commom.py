from django.shortcuts import render
from django.http import JsonResponse
from utils.code_status import *


def success_resp(result, message='successful'):
    """
        封装请求成功响应体
    :return:
                {
        “code”:200,
        “result”:data,
        “message”:’successful’
        }
    """
    response_dict = {
        "code":200,
        "result":result,
        "message": message,
        'APIName':'图像识别/处理-小程序应用接口.'
    }
    return JsonResponse(response_dict)


def faild_resp(result, message='faild'):
    """
        封装请求失败响应体
    :return:
        {
        “code”:400,
        “result”:data,
        “message”:’faild’
        }
    """
    response_dict = {
        "code": 404,
        "result": result,
        "message": message,
    }
    return JsonResponse(response_dict)
