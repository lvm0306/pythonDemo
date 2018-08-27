# -*- coding: utf-8 -*-
import os
import sys
from itertools import islice

import oss2

#上传文件
def updatafile():
    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth('LTAIx8OOkGg1SRrg', '0ooqAg6j97saM7rI8SrgAAB875cYg4')
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'https://oss-cn-beijing.aliyuncs.com', 'mdeandroid')
    # <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt
    s=bucket.put_object_from_file('Test/local01.jpg', "/Users/lovesosoi/Desktop/git_01.jpg")
    print(s)

#下载文件

def downloadfile():
    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth('LTAIx8OOkGg1SRrg', '0ooqAg6j97saM7rI8SrgAAB875cYg4')
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'https://oss-cn-beijing.aliyuncs.com', 'mdeandroid')
    # 下载OSS文件到本地文件。如果指定的本地文件存在会覆盖，不存在则新建。
    bucket.get_object_to_file('Test/local01.jpg', '/Users/lovesosoi/Desktop/test01.jpg')

#进度条上传文件
def circleupdata():
    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth('LTAIx8OOkGg1SRrg', '0ooqAg6j97saM7rI8SrgAAB875cYg4')
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'https://oss-cn-beijing.aliyuncs.com', 'mdeandroid')

    # 当无法确定待上传的数据长度时，total_bytes的值为None。
    def percentage(consumed_bytes, total_bytes):
        if total_bytes:
            rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
            print('\r{0}% '.format(rate), end='')
            sys.stdout.flush()

    # progress_callback为可选参数，用于实现进度条功能。
    bucket.put_object('Test/local02.txt', 'a' * 1024 * 1024, progress_callback=percentage)

def listfile():
    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth('LTAIx8OOkGg1SRrg', '0ooqAg6j97saM7rI8SrgAAB875cYg4')
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'https://oss-cn-beijing.aliyuncs.com', 'mdeandroid')
    for b in islice(oss2.ObjectIterator(bucket), 100):
        print(b.key)

if __name__ == '__main__':
    print('hehe')
    # updatafile()
    # downloadfile()
    # circleupdata()
    listfile()



