from datetime import datetime
print('Start - Control Flow')

now = datetime.now()
phone_balance = 3
bank_balance = 100

season = 'winter'
seasons = {'spring':'plant the garden',
           'summer':'water the garden',
		   'fall':'harvest the garden',
		   'winter':'stay indoors',
		   'outofrange':'unknow season'}
#Ex1

print(phone_balance,bank_balance)

if phone_balance < 5 :
	phone_balance += 10
	bank_balance -= 10
else:
	print('phone_balance is more then:{}'.format(phone_balance))
print(phone_balance,bank_balance)
#Ex2

if bank_balance % 2 == 0 :
	print('{} is even.'.format(bank_balance))
	print(now)
else:
	print('{} is odd.'.format(bank_balance))

#EX3

if season == 'spring':
	print(seasons['spring'])
elif season == 'winter':
	print(seasons['winter'])
elif season == 'summer':
	print(seasons['summer'])
elif season == 'fall':
	print(seasons['fall'])
else :
	print(seasons['outofrange'])

#EX4

points = 174  # use this input to make your submission

# write your if statement here
prize = {'wooden rabbit':'wooden rabbit',
         'no prize':'no prize',
		 'wafer-thin mint':'wafer-thin mint',
		 'penguin':'penguin'}
if points <=50 :
    result = "Congratulations! You won a {}!".format(prize['wooden rabbit'])
elif points <= 150 :
	result = "Congratulations! You won a {}!".format(prize['no prize'])
elif points <= 180:
	result = "Congratulations! You won a {}!".format(prize['wafer-thin mint'])
elif points <= 200 :
	result = "Congratulations! You won a {}!".format(prize['penguin'])
else:
	result = 'out of range'
print(result)

#EX5
# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 4
guess = 6
message = 'Oops!  Your guess was too' + ' '
if guess < answer :
    result = str(message) + "low."
elif guess > answer :
    result = str(message) + "high."
elif guess == answer :
    result = "Nice!  Your guess matched the answer!"

print(result)

#EX6
# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'CA'
purchase_amount = 100
message = "Since you're from {}, your total cost is {}."
if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = message.format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = message.format(state, total_cost)

elif state ==  'NY' :
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = message.format(state, total_cost)

print(result)

#EX7

height = 5
weight = 160

if 18.5 <= weight/height**2 < 25:
	print("BMI is normal")
else:
	print('BMI is not normal')

#EX7
altitude = 10000
speed = 250
propulsion = "Propeller"

if altitude < 1000 and speed > 100:
	print('true')
else:
	print('false')

if (propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000:
	print('jet')
else:
	print('nonjet')
if not (speed > 400 and propulsion == "Propeller"):
	print('speed')
else:
	print('nonspeed')

if (altitude > 500 and speed > 100) or not propulsion == "Propeller":
	print('true')
else:
	print('false')

#EX8 FOR LOOPS
cities = ['new york city', 'mountain view','chicago','los angeles']
capitalized_city = []
msg = 'City is: {}'
for city in cities:
	print(msg.format(city.title()))
	capitalized_city.append(city.title())
print('Capitalized Cities : {}'.format(capitalized_city))

for index in range(len(cities)):
	print('Citiy based on range:{}'.format(cities[index].title()))

#EX9
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
	print('Sentence is :{}'.format(word))

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive


for num in range(5,35,5):
    print(num)

#EX10
#Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for name in names:
	usernames.append(name.lower().replace(" ", "_"))
	
print('Usernames are :{}'.format(usernames))

#EX11
tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

#EX12 Building Dictionaries
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
#Iterate through each element in the list. If an element is already included in the dictionary, add 1 to its value. If not, add the element to the dictionary and set its value to 1.
for word in book_title:
	if word not in word_counter:
		word_counter[word] = 1
	else:
		word_counter[word] +=1

print(word_counter)

#EX12 Key values
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key in cast:
	print('Cast are :',key)
for key,valu in cast.items():
	print('Actor:{} is in role:{}'.format(key,valu))
#EX13
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result1 = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add the value (number of fruits) to result
for item, count in basket_items.items():
	if item in fruits:
		result1 += count
	else:
		print('items dont exists')
print('Total fruits in the basket:{}'.format(result1))

#EX14
#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for item, count in basket_items.items():
	if item in fruits:
		result += count

print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for item, count in basket_items.items():
	if item in fruits:
		result += count

print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for item, count in basket_items.items():
	if item in fruits:
		result += count

print(result)

#EX15
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add to fruit_count.
for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count
#if the key is not in the list, then add to the not_fruit_count
print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))

#EX 16 While loops

card_deck = [4,11,8,5,13,2,8,10]
hand = []

while sum(hand) <= 17:
	hand.append(card_deck.pop())

print('hand', hand)

#EX17
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here

    # multiply the product so far by the current number
    
    
    # increment current with each iteration until it reaches number

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

#EX18
start_num = 5
end_num = 100
count_by = 2 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while start_num < end_num:
	  start_num += count_by

print('countby:',start_num)

#EX19
start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

#EX20
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

#EX21
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for str in headlines:
    news_ticker += str + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        
    else:
        print("cont loop")

print(news_ticker)

#EX21 Zip and Enumerate
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
print('end - Control Flow')

