# глобална променлива
port = 1521
# 1. дефиниция на функцията
def sum_numbers(a, b, d = None):
    # c - локална променлива
    c = a + b + d if d  else a + b
    return c
    

if __name__ == '__main__':
    # 2. извикване
    res = sum_numbers(5, 6)
    print(f'sum = {res}')

    x, y, z = 10, 22, 15
    res = sum_numbers(x, y, z)
    print(f'{x} + {y} + {z} = {res}')

    print('--- ---')    