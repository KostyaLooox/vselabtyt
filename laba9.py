import csv
import os
from PIL import Image

def z1():
    i = 'путь до папки 1'

    if not os.path.exists('путь для создаия папки 2'):
        os.mkdir('папка 2 путь ')

    for f in os.listdir(i):
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            im = Image.open(os.path.join(i,f))
            im = im.resize((500, 500))
            im.save(os.path.join('папка 2 путь', f))
def z2():
    with open("data.csv") as f:
        t_readed = csv.reader(f, delimiter = ",")

        c = 0
        print("Нужно купить")

        for row in t_readed:
            print(f'{row[0]} - {row[1]} шт. за {row[2]} руб.')
            c += 1
        print(f'Всего в файле {c} строк.')


z1()
