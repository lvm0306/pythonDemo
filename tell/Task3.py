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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
becall = set()
fenzi = 0
fenmu = 0
for call in calls:
    if (call[0][0:5] == '(080)'):
        if (call[1][0] == '('):
            str = ''
            for s in call[1][1:]:
                str = str + s
                if (s == ')'):
                    str = str[0:len(s) - 2]
                    becall.add(str)
                    break
        elif (call[1][5] == ' ' and (call[1][0] == '7' or call[1][0] == '8' or call[1][0] == '9')):
            becall.add(call[1][0:4])
        # elif (call[1][5] != ' ' and call[1][0:3] == '140'):
        #     becall.add(call[1][0:3])

print("The numbers called by people in Bangalore have codes: ")
for call in sorted(becall):
    print(call)

for call in calls:
    if (call[0][0:5] == '(080)' and call[1][0:5] == '(080)'):
        fenzi += 1

for call in calls:
    if (call[0][0:5] == '(080)'):
        fenmu += 1

baifenbi = "%.2f" % ((float(fenzi) / float(fenmu)) * 100) + '%'
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(baifenbi))
