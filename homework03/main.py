from MyQueue import *
from Country import *

my_queue_of_ints = MyQueue()

for i in range(3):
    for j in range(4):

        my_queue_of_ints.add(i * 10 + j)

print('full queue fo ints:', my_queue_of_ints)

my_queue_of_ints.remove(0)
print('remove 0:', my_queue_of_ints)

my_queue_of_ints.pop()
print('pop:', my_queue_of_ints)

my_queue_of_ints.remove(9)
print('remove 9:', my_queue_of_ints)

my_queue_of_ints.remove(5)
print('remove 5:', my_queue_of_ints)

print('error expected:')
try:
    my_queue_of_ints.remove(10)
except ValueError as error:
    print(error)

print('\n')


my_queue_of_countries = MyQueue()

for i in range(2):
    for j in range(2):
        country = Country('capital: ' + str((i + 1) * 9), 'population: ' + str((j + 2) * (i + 1) * 31))
        my_queue_of_countries.add(country)

print('my_queue of countries:', my_queue_of_countries)
