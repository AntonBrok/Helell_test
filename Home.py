#name = input("Enter your name: ")
#print("Hellow", name)
#source_file = open("test.txt" , "w")
#print('Priviau', file=source_file)
#source_file.close()
#a = divmod(30, 5)
#print(a)
#a, b, c, d = "1234"
#print(a, b, c, d)

name1 = 'banana'
value2 = 12
name3 = 'Lemon'
value4 = 15

import datetime
now = datetime.datetime.now()
print('Hello, %s  - %d ps and %s  - %d ps' % (name1, value2, name3, value4))
#print("Як тебе звати?", 'Скільки тобі років?', 'Хулі тут забув?' , sep = '\n' )
#print("Як тебе звати?")

name = input("Як тебе звати?")
#print("Скільки тобі років?")
age = input("Скільки тобі років?")


print('Мене звати {0} , мені {1} років ,{0} либить кодити'.format(name, age))
print(f'Мене звати {name.upper():.1} , мені {age} років ,{name} либить кодити')
print("час :", datetime.datetime.now() - now)