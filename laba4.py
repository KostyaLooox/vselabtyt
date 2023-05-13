def z1():
    try:
        a = int(input("число сюда: "))
        b = a % 3
    except ValueError:
        print("Число надо")
    else:
        if b == 0 and a != 0:
            print("ес сэр")
        elif a == 0:
            print("Какой ноль")
        else:
            print("ноу сэр")
def z2():
    try:
        a = int(input("число сюда: "))
        b = 100 / a
    except ValueError:
        print("Число надо")
    except ZeroDivisionError:
        print("какой ноль")
    else:
        print(f"{b}")

def z3():
    a = input("дату сюда в форме дд.мм.гггг: ")
    a = a.split('.')
    if int(a[0]) * int(a[1]) == int(a[2][2:4]):
        print("yes")
    else:
        print("no")

def z4():
    a = input("номер билета сюда: ")
    if len(a) % 2 == 0:
        b = len(a)
        c = b // 2
        f = 0
        r = 0
        t =0
        g = c
        while f <= c:
            if f == (c+1):
                break
            d = f
            y = int(a[d])
            r += y
            f += 1
            if f == c:
                break
            continue
        while g <= (c+c):
            h = g
            u = int(a[h])
            t += u
            g += 1
            if g == (c + c):
                break
            continue
        if r == t:
            print("Да билет счасливый", r , t)
        else:
            print("о нет билет такой себе не красивый", r , t)
    else:
        print("что такое число делить на 2 ахахахах")
z1()
z2()
z3()
z4()