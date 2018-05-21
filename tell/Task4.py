# coding=utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

callbo = set()
callshou = set()
textreceiver = set()
textsender = set()
tuixiao=set()
#
for call in calls:
    callbo.add(call[0])
    callshou.add(call[1])
for text in texts:
    textreceiver.add(1)
    textsender.add(0)
lenshou = len(callshou)
lenreceiver = len(textreceiver)
lensender = len(textsender)
for call in callbo:
    callshou.add(call)
    if (len(callshou) == lenshou):
        continue
    else:
        lenshou=len(callshou)
        tuixiao.add(call)
    textreceiver.add(call)
    if (len(textreceiver) == lenreceiver):
        continue
    else:
        lenreceiver=len(textreceiver)
        tuixiao.add(call)
    textsender.add(call)
    if (len(textsender) == lensender):
        continue
    else:
        lensender=len(textsender)
        tuixiao.add(call)
l=list(tuixiao)
l.sort()
for tui in l:
    print("These numbers could be telemarketers: {}".format(tui))