#ly--------------2017.12.12
# -*- coding: utf-8 -*
#商城
import re
# FileName = r"H:\xljs\design\dhtx\server_runtime\gameworld\data\config\store\classes\other.txt"
print('ly----------------start')
FileName = "demo_1.txt"

a = 5	#现价系数
b = 5	#原价系数

PriceStr = '{ spid = '#修改行
re_ybStr = '		{3} spid = "*", type = {1}, price = {0}, bind = false, oldPrice = {2} {4}, \n'#修改元宝字段
# re_ybStr = '				{3} spid = "*", type = {1}, price =	{0}	, bind = true,oldPrice=	{2}	 {4}, \n'#修改限时抢购

pattern = r"type=(.+),price=(.+),bind=(.+),oldPrice=(.+)},"	#规则
result = ""
f = open(FileName,"r")
lines = f.readlines()
for line in lines:
	if PriceStr in line:
		# print('kyo--------------Oline:' + line)
		line = line.replace(" ","")
		list = re.findall(pattern,line)
		# print('kyo--------------line:' + line)
		print(list)
		TempStr = re_ybStr.format(str(int(list[0][1])*a),str(int(list[0][0])),str(int(list[0][3])*b),r'{',r'}')
		# TempStr = re_ybStr.format(str(500),str(5000),r'{',r'}')
		result = result + TempStr
	else:
		result = result + line
f = open(FileName,"w")
f.write(result)
f.close()
print('ly----------------finish')