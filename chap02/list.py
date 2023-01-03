import enum


x = ['a', 'b', 'c', 'd']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')


for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
