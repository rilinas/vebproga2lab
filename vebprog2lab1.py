def func1():
    list2 = []
    list3 = []
    list5 = []
    print('Эта программа позволяет узнать, какие из введенных чисел делятся на 2, 3 и 5')
    print('Для начала введите количество чисел, которое вы хотите протестировать')
    count = input()
    print('Теперь через enter введите числа')
    i = 0
    while i < int(count):
        a = int(input())
        if (a % 2) == 0:
            list2.append(a)
        if (a % 3) == 0:
            list3.append(a)
        if (a % 5) == 0:
            list5.append(a)
        i+=1
    return list2, list3, list5

res = func1()
print('В первом списке находятся элементы кратные 2, во втором - кратные 3, в третьем - кратные 5')
print(res)
