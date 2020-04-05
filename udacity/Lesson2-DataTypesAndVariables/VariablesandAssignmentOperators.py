#Variables
x = 2
y = x
print(y)

mv_population = 74728
mv_area = 11.995
mv_density = mv_population/mv_area

print(mv_density)

#Assign and Modify Variables
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 444500000.0
# The amount of rainfall from a storm (in cubic metres)
rainfall = 500000.0

# decrease the rainfall variable by 10% to account for  
runoff = rainfall*0.9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume = reservoir_volume + runoff 

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume = reservoir_volume + reservoir_volume*0.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume - reservoir_volume*0.05

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume = reservoir_volume - 250000.0
# print the new value of the reservoir_volume variable
print("Assign and Modify Variables",reservoir_volume)

#Changing Variable Values
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
rabbits = 12

print("Changing Variable Values",crs_per_rab)

#Integers and Floats
print(3/4)
print(3+2.5)
print(int(49.7))
print(int(16/4))
print(16/4)
print(0.1+0.1+0.1)
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
print(type(x))
print(4+5)
print(4   +   5)

print("Integers and Floats")

#Booleans, Comparison Operators, and Logical Operators
x = 42 > 43
print(x)
age = 14
is_teen = age >12 and age < 20
not_teen = not (age>12 and age <20)
print(not_teen)
print(is_teen)
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
is_denser = san_francisco_pop_density > rio_de_janeiro_pop_density
print(is_denser)

print("Booleans, Comparison Operators, and Logical Operators")

#string
print("hello in double quotes")
print('hello in single quotes')
msg = 'I am learning in Udacity'
print('Hello there-',msg)
first_name='hello'
last_name='there'
full_name = first_name +' '+ last_name
print(full_name)
print(first_name*5)
print(len(first_name))
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username+' '+'accessed the site'+' '+url+' '+'at'+' '+ timestamp+ '.')

print("string")

#Type And Type Conversion
print(type(633))
print(type(23.9))
print(type("string"))

count = int(4.0)
print(type(count))

house_number = 10
street_name = "street1"
town_name = 'mytown'

address = str(house_number)+' '+street_name+' '+town_name
string_count=len("my_string")
print(type(string_count))
print(address)
mon_sales = "121"
tues_sales = "105"
wed_sales = "55"
thurs_sales = "98"
fri_sales = "95"
sum= int(mon_sales) + int(tues_sales)+ int(wed_sales)+ int(thurs_sales)+int(fri_sales)

print(sum)
print("Type And Type Conversion")

#string methods

print(full_name.title())
print(full_name.islower())
print(full_name.isupper())
fish_type = 'blue fish,red fish,black fish,white fish'
print(fish_type.count('fish'))
print("Mohammed has {} balloons".format(27))
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))
just_flaot = '13.37'
print(just_flaot.islower)
virus_name = 'coronoavirus has outbreak in {}'
print(virus_name.format(2019))
new_str = "The cow jumped over the moon."
print(new_str.split())
print(new_str.split(' ', 3))
print(new_str.split('.'))
print(new_str.split(None, 3))
print('string methods')
