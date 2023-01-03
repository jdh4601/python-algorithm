# x = [15, 64, 3, 5.33, [33, 44], 'ABC']

# for i in range(len(x)):
#     print(f'x[{i}] = {x[i]}')

import copy

x = [[1, 2], [3, 4]]

# y = x.copy() # 얕은 복사
y = copy.deepcopy(x)  # 깊은 복사

x[0][1] = 9

print(id(x))  # [[1, 9], [3, 4]]

print(id(y))  # [[1, 2], [3, 4]]
