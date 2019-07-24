#Start - Arithmetic operators
totalApple = 12
totalOrange = 18

print("total fruits:", totalApple + totalOrange)
print("totalOrange - totalApple",totalOrange-totalApple)
print("totalOrange * totalApple",totalOrange*totalApple)
print("totalOrange / totalApple",totalOrange/totalApple)
#end - Arithmetic operators 
#Start - Comparison operators
isSunday = True
isHoliday = True
isMonday = True
isTuesday = False

if isHoliday and isSunday:
	print('Sunday is holiday')
else:
	print('Sunday is not holiday')

if isMonday or isTuesday:
	print('Its working day')
else:
	print('Its not working day')

if not isTuesday:
	print('Tuesday is working day')
else:
	print("Tuesday is not working day")	
#end - Comparison operators