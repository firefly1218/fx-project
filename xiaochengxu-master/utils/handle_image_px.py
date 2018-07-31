"""
    批量压缩文件(缩小文件大小)
"""
from xiaochengxu.settings import *
from PIL import Image
import os

#图片压缩批处理
def compressImages(srcPath,dstPath):
    for filename in os.listdir(srcPath):
        #如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)

        #拼接完整的文件或文件夹路径
        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename)
        print(srcFile)
        print(dstFile)

        #如果是文件就处理
        if os.path.isfile(srcFile):
            #打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            sImg=Image.open(srcFile)
            w,h=sImg.size
            print(w,h)
            dImg=sImg.resize((int(w/2),int(h/2)),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
            dImg.save(dstFile) #也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
            print(dstFile+" compressed succeeded")

        #如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImages(srcFile,dstFile)

# if __name__=='__main__':
#     compressImages(BASE_DIR+"/static/images",BASE_DIR+"/static/compress_images")

def compressImage():
    import os.path
    import sys
    path = sys.argv[1]
    small_path = (path[:-1] if path[-1] == '/' else path) + '_small'
    if not os.path.exists(small_path):
        os.mkdir(small_path)
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            img = Image.open(fp)
            w, h = img.size
            img.resize((w / 2, h / 2)).save(os.path.join(small_path, f), "JPEG")
            print(f)



class ImageCompressUtil(object):
    """
        # 目标图片大小
        dst_w = 600
        dst_h = 600
        # 保存的图片质量
        save_q = 80
        srcPath = os.getcwd() + '\\image\\src\\src.jpg'
        savePath = os.getcwd() + '\\image\\src\\save.jpg'
        ImageCompressUtil().resizeImg(
            ori_img=srcPath,
            dst_img=savePath,
            dst_w=dst_w,
            dst_h=dst_h,
            save_q=save_q
            )
    """
    # 等比例压缩
    def resizeImg(self, **args):
        try:
            args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 100}
            arg = {}
            for key in args_key:
                if key in args:
                    arg[key] = args[key]
            im = Image.open(arg['ori_img'])
            if im.format in ['gif', 'GIF', 'Gif']:
                return
            ori_w, ori_h = im.size
            widthRatio = heightRatio = None
            ratio = 1
            if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
                if arg['dst_w'] and ori_w > arg['dst_w']:
                    widthRatio = float(arg['dst_w']) / ori_w  # 正确获取小数的方式
                if arg['dst_h'] and ori_h > arg['dst_h']:
                    heightRatio = float(arg['dst_h']) / ori_h
                if widthRatio and heightRatio:
                    if widthRatio < heightRatio:
                        ratio = widthRatio
                    else:
                        ratio = heightRatio
                if widthRatio and not heightRatio:
                    ratio = widthRatio
                if heightRatio and not widthRatio:
                    ratio = heightRatio
                newWidth = int(ori_w * ratio)
                newHeight = int(ori_h * ratio)
            else:
                newWidth = ori_w
                newHeight = ori_h
            if len(im.split()) == 4:
                # prevent IOError: cannot write mode RGBA as BMP
                r, g, b, a = im.split()
                im = Image.merge("RGB", (r, g, b))
            im.resize((newWidth, newHeight), Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])
        except Exception as e:
            # LogDao.warn(u'压缩失败' + str(e), belong_to='resizeImg')
            print('图片压缩失败原因:',e)
            print('图片压缩失败!')
            return 0
        else:
            return 1

