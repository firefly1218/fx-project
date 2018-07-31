""""
参考: https://www.cnblogs.com/chimeiwangliang/p/7130434.html
"""

from PIL import Image
#
# __author__ = 'admin'
#
# '''
#     在原图上加入缩略图
# '''
#
#
# def thumbnail(im):
#     #   缩略图大小
#     size = (200, 200)
#     try:
#         #   创建后的缩略图大小不一定就是200x200的，是按照原图比例来的
#         im.thumbnail(size)
#         return im
#     except IOError:
#         print(u"无法创建缩略图！")
#
#
# def mosaic(im):
#     im0 = Image.open('/home/python/Desktop/python_code/test/xiaochengxu/static/loca_image/图像处理专用章.png')
#     width_im, height_im = im0.size
#     #   调用thumbnail创建缩略图
#     im_thumbnail = thumbnail(im0)
#     #   获取缩略图大小
#     # width_thumbnail, height_thumbnail = im_thumbnail.size
#     width_thumbnail, height_thumbnail = im0.size
#     #   避免出现原图比缩略图尺寸还小的情况
#     if width_im > width_thumbnail and height_im > height_thumbnail:
#         im.paste(im0, (0, 0, width_thumbnail, height_thumbnail))
#     return im
#
#
# im = Image.open('/home/python/Desktop/python_code/test/xiaochengxu/static/images/007.jpg')
# mosaic(im).show()

im = Image.open(r'/home/python/Desktop/python_code/test/xiaochengxu/static/images/007.jpg')
# im.show()
im1 = Image.open(r'/home/python/Desktop/python_code/test/xiaochengxu/static/loca_image/图像处理专用章.png')
print(im1)
# im1 = im1.point(lambda i: i*0 if i<100 else i*0)
im2 = im1.copy()
im2.show()
# cropedIm = im.crop((700, 100, 1200, 1000))

# im.paste((256,256,256,256),(200,100,500,200))
# im.show()

box = [100,100,200,200]
im_crop = im1.crop(box)
print(im_crop)

r,g,b = im_crop.split()
im.paste(im_crop,(200,100,300,200),b)
im.show()

im.paste(im2, (200, 200))
# im.convert('RBGA')
# im.save('/home/python/Desktop/python_code/test/xiaochengxu/static/images/0072.png')
im.show()




