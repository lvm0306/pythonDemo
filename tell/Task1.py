#coding=utf-8
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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
photonum= set()
for i in range(len(calls)):
    photonum.add(calls[i][0])
    photonum.add(calls[i][1])

for i in range(len(texts)):
    photonum.add(texts[i][0])
    photonum.add(texts[i][1])

print("There are {} different telephone numbers in the records.".format(len(photonum)))

# testset=set(calls)
# print(testset)
