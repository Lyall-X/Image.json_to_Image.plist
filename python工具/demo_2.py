#ly--------------2017.12.12
# -*- coding: utf-8 -*
#签到，物品修改未完工
import re
# FileName = r"H:\xljs\design\dhtx\server_runtime\gameworld\data\config\vip\sign_reward_config.txt"
print('ly----------------start')
FileName = "demo_2.txt"

a = 1	#补签系数
b = 5	#元宝系数
c = 3   #除了绑定元宝其他物品系数
#c = 10	#物品系数
x = "2"	#元宝id
y = "0"	#预留
z = "0"	#预留

bqStr = 'ExtraSignCost = '#补签字段
ybStr = 'reward ='#元宝字段
re_ybStr = '			reward = {3}type={0},id={1},count={2}{4},\n'#修改元宝字段

pattern = ""	#规则
result = ""

f = open(FileName,"r")
lines = f.readlines()
for line in lines:
	if bqStr in line:
		pattern = "ExtraSignCost = (.*),"
		list = re.findall(pattern,line)
		cost = list[0]
		NewPattern = pattern.replace("(.*)",str(int(cost)*a))
		TempStr = re.sub(pattern,NewPattern,line)
		result = result + TempStr
	elif ybStr in line:
		pattern = r"reward = {{type=(.+),id=(.+),count=(.*)}},"
		# pattern = "[0-9]+"
		list = re.findall(pattern,line)
		if x == list[0][1]:
			# NewPattern = pattern.replace("(.*)",str(int(list[0][2])*b))
			# TempStr = re.sub(pattern,NewPattern,line) 
			TempStr = re_ybStr.format(list[0][0],list[0][1],str(int(list[0][2])*b),r'{{',r'}}')
			result = result + TempStr
		else:
			TempStr = re_ybStr.format(list[0][0],list[0][1],str(int(list[0][2])*c),r'{{',r'}}')
			result = result + TempStr
	else:
		result = result + line
f = open(FileName,"w")
f.write(result)
f.close()
print('ly----------------finish')