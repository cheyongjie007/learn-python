# -*- encoding:utf-8 -*-


######学生基本信息###########
#姓名:车永杰
#学号:1403050101
#班级:通风1班

xuehao=raw_input('请输入学号:')

name=raw_input('请输入姓名:')

age=input('请输入年龄:')

gs=input('请输入高数成绩:')

yy=input('请输入英语成绩:')

yw=input('请输入语文成绩:')

jq=gs*0.6+yy*0.3


print'学号:',xuehao,'姓名:',name,'年龄:',age
print'高数:',gs,'英语:',yy

print'加权平均数:',jq
