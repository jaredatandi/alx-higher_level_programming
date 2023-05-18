#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if i > j:
            pass
        elif f'{i}{j}' == '89':
            print(f'{i}{j}')
        else:
            print(f'{i}{j}', end=", ")
