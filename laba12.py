import tkinter as tk


def z1():
    class Rest:
        def __init__(self, rname, ctype):
            self.rname = rname
            self.ctype = ctype

        def describe_restaurant(self):
            print(f'Название: {self.rname} Тип кухни: {self.ctype}')

    class IceCreamStand(Rest):
        def __init__(self,rname, ctype, flavors):
            super().__init__(rname, ctype)
            self.flavors = flavors

        def iflavors(self):
            print('Виды мороженного:')
            print(*self.flavors, sep='\n')

    s = IceCreamStand("Муравей", 'кафе', ['ваниль', 'клубника', 'шоколад'])
    s.iflavors()

def z2():
    class Rest:
        def __init__(self, rname, ctype):
            self.rname = rname
            self.ctype = ctype

        def describe_restaurant(self):
            print(f'Название: {self.rname} Тип кухни: {self.ctype}')


    class IceCreamStand(Rest):
        def __init__(self, rname, ctype, flavors, place, time):
            super().__init__(rname, ctype)
            self.flavors = flavors
            self.place = place
            self.time = time

        def iflavors(self):
            print('Виды мороженного:')
            print(*self.flavors, sep='\n')

        def plus(self):
            self.flavors.append(input('Введите новое мороженое '))

        def minus(self):
            self.flavors.remove(input('удалить мороженое '))

        def poisk(self):
            if input('Какой вкус хотите найти? ') in self.flavors:
                print('Eсть')
            else:
                print('Нет')

    class paZlochke(IceCreamStand):
        def __init__(self, rname, ctype, flavors, place, time, material):
            super().init(rname, ctype, flavors, place, time)
            self.material = material

        def palochka(self):
            print('Материал палочки: ', self.material)

    class sVtakane(IceCreamStand):
        def __init__(self, rname, ctype, flavors, place, time, sale):
            super().init(rname, ctype, flavors, place, time)
            self.sale = sale

        def stakan(self):
            print('Размер стакана: ', self.sale)

    s = IceCreamStand("Муравей", 'кафе', ['ваниль', 'клубника', 'шоколад'], 'ул. Есть', '8:00-21:00')
    s.describe_restaurant()
    s.plus()
    s.iflavors()
    s.minus()
    s.iflavors()
    s.poisk()

    g = paZlochke("Муравей", 'кафе', ['ваниль', 'клубника', 'шоколад'], 'ул. Есть', '8:00-21:00', 'дерево')
    g.palochka()

def z3():
    class IceCreamStand:
        def __init__(self):
            self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Coffee', 'Rocky Road'] # сразу даем значение и делаем список
            self.prices = [1.99, 2.99, 2.99, 3.99, 3.99, 4.99] # тут тоже самое

        def get_flavors(self):
            return self.flavors # вернем 1

        def get_prices(self):
            return self.prices # вернем 2

    class IceCreamStandGUI:
        def __init__(self, master):
            self.master = master # надо сделать окошко
            master.title("Ice Cream Stand") # даем название

            self.ice_cream_stand = IceCreamStand()

            self.flavors_label = tk.Label(master, text='Flavors', font='Helvetica 12 bold') # название мороженого + настройка шрифта

            self.flavors_listbox = tk.Listbox(master, font='Helvetica 12', height=len(self.ice_cream_stand.get_flavors())) # название мороженого лист + настройка шрифта + делае строки по вертикал

            for flavor in self.ice_cream_stand.get_flavors():
                self.flavors_listbox.insert(tk.END, flavor) # заполнить в конце после создания

            self.prices_label = tk.Label(master, text='Prices', font='Helvetica 12 bold')# название цен + настройка шрифта

            self.prices_listbox = tk.Listbox(master, font='Helvetica 12', height=len(self.ice_cream_stand.get_prices())) # название цен лист + настройка шрифта + делае строки по вертикал

            for price in self.ice_cream_stand.get_prices():
                self.prices_listbox.insert(tk.END, price) # заполнить в конце после создания

            self.flavors_label.grid(row=0, column=0) # 1 строка 1 столбец
            self.flavors_listbox.grid(row=1, column=0) # 2 строка 1 столбец
            self.prices_label.grid(row=0, column=1) # 1 строка 2 столбец
            self.prices_listbox.grid(row=1, column=1) # 2 строка 2 столбец

    root = tk.Tk() # окно
    a = IceCreamStandGUI(root) # окно в переменую
    root.mainloop() # покаи окно


z3()