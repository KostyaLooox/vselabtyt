from PIL import Image, ImageDraw

def z1():
     i = Image.open('photo_2023-04-13_12-54-37.jpg')
     i_c = i.crop((100, 75, 500, 550))
     i_c.save('uu.jpg')

def z2():
     f = { '1': 'photo_2023-04-13_12-54-30.jpg',
           '2': 'photo_2023-04-13_12-54-37.jpg',
           '3': 'photo_2023-04-12_23-03-45.jpg'
     }
     h = input("gjjhjj: ")
     if h in f:
          z = f[h]
          g = Image.open(z)
          g.show()

def z3():
     i = Image.open('photo_2023-04-13_12-54-30.jpg')
     y = ImageDraw.Draw(i)
     y.text((50, 100), "Hello World!", fill='black')
     i.save('hi.jpg')

z3()