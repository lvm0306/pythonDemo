from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 图片缩小比例
# 参数：图地址，宽缩小比例，高缩小比例
# 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('cat.png')
# # 获得图像尺寸:
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('thumbnail.png', 'png')


# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('people.jpg')
# 应用模糊滤镜:
im2 = im.convert('RGB').filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')


# 随机生成验证码
# 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
#
#
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
#
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
#
# # 240 x 6www0:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     s = rndChar()
#     print(s)
#     draw.text((60 * t + 10, 10), s, font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')


#旋转验证码
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
#
# import random
#
# # 旋转
# def rndCharImg():
#     img1 = Image.new('RGB', (60, 60), (0,0,0,0))
#     fnt = ImageFont.truetype('Arial.ttf', 36)
#     drw1 = ImageDraw.Draw(img1)
#     k = rndChar()
#     print(k)
#     drw1.text((10,10), k, random.randint(127, 200), font=fnt)
#     img1 = img1.rotate(random.randint(0, 90))
#     img1.save('code1.jpg', 'jpeg')
#     return img1
#
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
#
# # 随机颜色1:
# def rndColor():
#     return (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
#
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (0,0,0,0))
#
# # 创建Font对象:
# font = ImageFont.truetype('Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 依次生成四个旋转字母，并且把图层通道分离，然后粘贴
# for t in range(4):
#     im1 = rndCharImg()
#     r,g,b= im1.split()
#     image.paste(im1, (60 * t + 10, 0), r)
# # 模糊和存盘
# image = image.filter(ImageFilter.BLUR)
# image.save('code2.jpg', 'jpeg')