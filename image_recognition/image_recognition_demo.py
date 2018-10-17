import base64
import hashlib
import json
import time
import urllib
from urllib import parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
data={}
app_id=	'2108112439'
app_key='gLCVDJzzSvTb4De9'
url ='https://api.ai.qq.com/fcgi-bin/'+ 'face/face_detectface'

def setParams(key, value):
    data[key] = value

def genSignString(parser):
    uri_str = ''
    for key in sorted(parser.keys()):
        if key == 'app_key':
            continue
        uri_str += "%s=%s&" % (key, parse.quote(str(parser[key]), safe=''))
    sign_str = uri_str + 'app_key=' + parser['app_key']

    hash_md5 = hashlib.md5(sign_str.encode('utf-8'))
    return hash_md5.hexdigest().upper()

def invoke(params):
    url_data = urllib.parse.urlencode(params).encode("utf-8")
    req = urllib.request.Request(url, url_data)
    try:
        rsp = urllib.request.urlopen(req)
        str_rsp = rsp.read().decode('utf-8')
        dict_rsp = json.loads(str_rsp)
        return dict_rsp
    except Exception as e:
        print(e)
        return {'ret': -1}


# ret	是	int	返回码； 0表示成功，非0表示出错
# msg	是	string	返回信息；ret非0时表示出错时错误原因
# data	是	object	返回数据；ret为0时有意义
# + image_width	是	int	请求图片的宽度
# + image_height	是	int	请求图片的高度
# + face_list	是	array	被检测出的人脸列表
# + + face_id	是	string	人脸（Face）ID
# + + x	是	int	人脸框左上角x
# + + y	是	int	人脸框左上角y
# + + width	是	int	人脸框宽度
# + + height	是	int	人脸框高度
# + + gender	是	int	性别 [0~100]（越接近0越倾向为女性，越接近100越倾向为男性）
# + + age	是	int	年龄 [0~100]
# + + expression	是	int	微笑[0~100] （0-没有笑容，50-微笑，100-大笑）
# + + beauty	是	int	魅力 [0~100]
# + + glass	是	int	是否有眼镜 [0, 1]
# + + pitch	是	int	上下偏移[-30,30]
# + + yaw	是	int	左右偏移[-30,30]
# + + roll	是	int	平面旋转[-180,180]
# + + face_shape	是	object	人脸配准坐标
def main():
    with open('face1.jpg', 'rb') as bin_data:
        imagedata = bin_data.read()

    setParams( 'app_id',app_id)
    setParams('app_key', app_key)
    setParams('mode', 0)
    setParams('time_stamp', int(time.time()))
    setParams( 'nonce_str', int(time.time()))
    image_data = base64.b64encode(imagedata)
    setParams('image', image_data.decode("utf-8"))
    sign_str = genSignString(data)
    setParams( 'sign', sign_str)
    json=invoke(data)
    print(json)
    print('您的预估年龄:'+str(json['data']['face_list'][0]['age']))
    print('您的颜值为:'+str(json['data']['face_list'][0]['beauty']))
    face= json['data']['face_list'][0]
    face_area = (face['x'], face['y'], face['x'] + face['width'], face['y'] + face['height'])
    print(face_area)

if __name__=='__main__':
    main()