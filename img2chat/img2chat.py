# coding:utf-8
# 导入Image，图片处理
from PIL import Image
# 导入argparse 命令行参数
import argparse


# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('filename') # 输入文件
parser.add_argument('-o','--output') # 输出文件
parser.add_argument('--width',type=int,default=50) # 输出字符画宽
parser.add_argument('--height',type=int,default=30) # 输出字符画高
# 获取参数
args = parser.parse_args()
# 定义相关的参数
IMG= args.filename
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height
# list中第一个元素是$.表示将使用$来道题原图中灰度值最低的像素点，其余依此类推
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 将256个字符映射到70个字符上
def get_char(r,g,b,apcha = 256):
    if apcha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) # RGB-灰度值 转换公式
    unit = (256.0 + 1) /length # ascii_char中的一个字符所能表示的灰度值区间
    return ascii_char[int(gray/unit)]
if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
            txt += '\n'
    print (txt)
    # 将字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('/Users/lovesosoi/Desktop/output.txt','w') as f:
            f.write(txt)