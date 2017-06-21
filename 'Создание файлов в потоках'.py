import threading

def docmaker(s,e):
    """Функция для создания файлов с изменяющимся именем и содержимым"""
    for i in range(s,e):
        with open('file{}.txt'.format(i),'w') as file:
            file.write('Hi Polly from thread{}!'.format(i))
        print('Создан file{}.txt'.format(i))

threads=[]
for i in range(1,11): # Создание 10 потоков, каждый из которых создает свой файл
   threadObj=threading.Thread(target=docmaker, args=(i, i+1))
   threads.append(threadObj)
   threadObj.start()
   threadObj.join() #Создание 2ого после завершения создания 1ого и тд

for thread in threads:
    thread.join() #Продолжение программы после завершения всех потоков

print('Готово!')
