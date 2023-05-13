def z1():
    a = input("Введите цвета в форме (красный и синий = rb) （красный и желтый = rj） （синий и желтый = bj): ")
    if (a == "rb") or (a == "br"):
        print("фиолетовый")
    elif  (a == "rj") or (a == "jr"):
        print("оранжевый")
    elif (a == "bj") or (a == "jb"):
        print("зеленый")

def z2():
    god = int(input("введите год: "))

    if (god % 4 == 0) and (god % 100 != 0):
        print("високосный")
    else:
        print("нет")

def z3():
    s = int(input("кол слов"))
    n = str("")
    word = str("")
    for i in range(s):
        word = input("СЛОВА")
        n = n + " " + word
    print(n)

def z4():
    a = input("пароль: ")
    if len(a) < 5:
        if a[0:6] == "qwerty":
            b = input("повтор пароль: ")
            if a == b:
                print("да совпал")
            else:
                print("нет")
    else:
        print("проверь лайн and easy")

def z5():
    n = int(input('Введите номер вашего места в плацкартном вагоне: '))
    print()
    if n > 36:
        print('Ваше место - боковое.')
    elif n % 2:
        print('Ваше место в купе внизу.')
    else:
        print('Ваше место в купе наверху.')

z1()
z2()
z3()
z4()
z5()