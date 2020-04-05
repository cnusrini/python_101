print("Start - List and Membership Operators")
month = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
greeting = 'Hello There'
VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']

print(month)
print(len(month))
print(month[3])
print('This is {} month'.format(month[2]))
print('School starts in {}'.format(month[-2]))

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things)
print(list_of_random_things[0])
print(list_of_random_things[len(list_of_random_things)-1])

print('First qtr:', month[0:3])
print('First Half:', month[:6])
print('Second Half:', month[6:])

print(len(month),len(greeting))
print(greeting[6:9],month[6:9])

print('her' in greeting, 'her' not in greeting)

print(VINIX[1])
print('GE' in VINIX)

#list methods
name = 'Coronovirus'
new_name = name
name = 'covid-19'
print(name)
print(new_name)

scores = ['B','C','A','D','B','A']
grades = scores
print(scores)
#before muting
print('scores:' + str(scores))
print('grades:' + str(grades))
scores[3] = 'B'
#After muting
print('scores:' + str(scores))
print('grades:' + str(grades))

#max()
batch_size = [15,6,89,34,65,35]
python_varieties = ['Burmese Python','Zfrican Rock Python', 'Ball Python','Retuculated Python','Angolan Python']
appended_python_varieties = python_varieties.append('Blood Python')


print('{} is the length of the batch_size list'.format(len(batch_size)))
print('{} is the max size of the batch_list'.format(max(batch_size)))

print('{} is the length of the python_varieties list'.format(len(python_varieties)))
print('{} is the max of the python_varieties list'.format(max(python_varieties)))

print('Sorted output of batch_size:'+ str(sorted(batch_size)))
print('Sorted out of python_varieties' + str(sorted(python_varieties)))

#join
directions = ['fore','aft','starboard','port']

updated_directions = '\n'.join(directions)
print(updated_directions)
print('-'.join(python_varieties))

print('appended_python_varieties:' + str(appended_python_varieties))

letters = ['a', 'b', 'c', 'd']
letters.append('e')
print(letters)

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(arr[2:6])
print(arr[0:3])
print(arr[4:])

#tuple
AngkorWat = (13.4125,103.866667)
dimension = 52,40,100
length,width,height = dimension
print(type(AngkorWat))
print(type(dimension))
print('AngkorWat is at a latitude of:{}'.format(AngkorWat[0]))
print('AngkorWat is at a longitude of:{}'.format(AngkorWat[1]))

print('Dimentions of the object are length,width,height:{},{},{}'.format(length,width,height))
tuple_a = 1, 2
tuple_b = (1, 2)
print(tuple_a == tuple_b)
print(tuple_a[1])

#sets
numbers = [1, 2, 6, 3, 1, 1, 6]
print('unique_nums are:{}'.format(set(numbers)))
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
print("watermelon" in fruit)
fruit.add("watermelon")  # add an element
print(fruit)
print("watermelon" in fruit)
print(fruit.pop())  # remove a random element
print(fruit)

#Dictionaries And Identity Operators
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print('Hydrogen is at position:{}'.format(elements['hydrogen']))
elements['lithium'] =3
print('lithium is at position:{}'.format(elements['lithium']))
print('mithril' in elements)
print(elements.get('dilithium'))
print(elements.get('helium'))

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)
animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals)

#Compound Data Structures
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print('hydrogen_weight is:{}'.format(hydrogen_weight))

print("End - List and Membership Operators")