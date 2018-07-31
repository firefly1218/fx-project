"""
    工具函数
"""

import time
import datetime
from xiaochengxu.settings import *

import os

def verification_image(filePath):
    """
    验证图片大小
    :return: 图片大小,单位M
    """
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    print('原图大小:', fsize, 'M')
    return round(fsize, 2)
# file_path = BASE_DIR + '/static/images/007.jpg'
# res = verification_image(file_path)
# print(res,'M')


from utils.handle_image_px import *
def compress_image():
    """
        压缩图片大小
    :return:
    """
    dst_w = 600
    dst_h = 600
    # 保存的图片质量
    save_q = 80
    srcPath = BASE_DIR + '/static/images/007.jpg'
    savePath = BASE_DIR + '/static/compress_images/007.jpg'
    res = ImageCompressUtil().resizeImg(
        ori_img=srcPath,
        dst_img=savePath,
        dst_w=dst_w,
        dst_h=dst_h,
        save_q=save_q
    )
    if not res:
        return 0
    else:
        return 1

# compress_image()


def base64_encode(binary_image_data):
    """
    将图片数据进行base64编码
    :return:
    """
    # 将图片数据流改成base64位的
    import base64
    image_data = base64.b64encode(binary_image_data)  # 读取文件内容，转换为base64编码

    return 'data:image/jpeg;base64,'+ image_data.decode('utf-8')
