import constant

#tutorial for basic data types
'''
in this tutorial, I will be building very basic
data types which are simple is computation,
but covers all the desired fundamentals
'''
"""Function to double the value"""

#start - Python List
org = ['fullname' , 'dept', 'AA123', 34.5]
print(type(org),org)
#end - Python List
#start - Python Numbers
EmpNu = 100
pay = 7.9
revenue = 1+2j
print(type(EmpNu),type(pay),type(revenue)) 
a1 = 12345678901234567891234567890123456789
b = 0.1234567890123456789
print(a1,type(a1),b,type(b))
#end - Python Numbers
#start - Literal Collections
empName = ["apple", "mango", "orange"] #list Literal
empID = (1, 2, 3) #tuple(an immutable collection) Literal
empIDtoName = {'1':'apple', '2':'ball', '3':'cat'} #dictionary Literal
print(empName,empName[0],empID,empIDtoName)
#end - Literal Collections
#start - Special literals
foodPreference = True
drinksPreferences = None
def pref(preference):
	if preference == foodPreference:
		print(foodPreference)
	else: 
		print(drinksPreferences)
pref(foodPreference)
pref(drinksPreferences)
#end - Special literals
#start - Boolean literals
x = (1 == True)
y = True
a = y+ 5
print(x,y,a)
#end - Boolean literals
#start - String literals
language = "This is Python"
grade = 'A'
skillsDesc = """Student has attained GRADE A """
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"
print(language,grade,skillsDesc,unicode,raw_str)
#end - String literals
#start - Numeric Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal
d2 = 300
#Float Literal
float_1 = 10.5 
float_2 = 1.5e2
#Complex Literal 
x = 3.14j
print(a,b,c,d,d2,float_1,float_2,x)

#end - Numeric Literals
print(constant.PI,constant.GRAVETY)
#---------------
hrdeptid = findeptid = "ID1234"
print(hrdeptid,findeptid)
fname,lname,age,salary = "fname","lname",18,24.5
print(fname,lname,age,salary)

sum = 1 + 2 + 3 \
		+ 4 + \
		5
sum1 = (1 + 2 + 3
		+ 4 +
		5)
website = "apple.com"
print(website)
website = "msn.com"
print(website)
if True:
    print('Hello')
    a = 5
for i in range(1,11):
    print(i)
    if i == 3:
        break		
print(sum)
print(sum1)

