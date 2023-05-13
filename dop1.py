#массив с данными
f = open("synonyms.txt")
massiv = []
for line in f:
    line=str(line)
    b=''.join(line.split()) #убираю пробелы
    massiv.append(b)


print("Введите ваше слово")
c=str(input())
l=len(c)
k=0

for dva in massiv:
    if dva.find(c, 0, l)!=-1: #проверка есть ли в строке это слово
        ll=len(dva)
        synon=dva[l+1:ll] #обрезаю синоним к слову
        print(synon)
        k=1

if k == 0:
    print("Вы ввели некорректное слово")

print("Синоним верный?(Да/Нет)")
otvet=str(input())
if otvet=='Да':
    print("Шикарно")
if otvet=='Нет':
    print("Введите свой вариант")
    var=str(input())
    with open ("synonyms.txt", "a") as file:
        file.write(c+"-"+var+'\n')
        file.close()
    print("Слово добавлено в словарь")



