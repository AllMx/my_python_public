# Лаборатория
# Создайте класс, осуществляющий подсчет и изменение числа книг. Названия книг, их количество считываются одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
# В классе должен быть реализован конструктор, деструктор, 
# методы просмотра числа,
# взятия и 
# возвращения книг.
# Реализовать вывод начальных значений, 
# взятие по 1 книге, 
# возвращение по 1 книге с выводом текущего числа после вызова каждого из методов, меняющих значение книг.
# Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'.

# Пример входных данных:
# Boogeyman 66 Battleground 50

# Пример выходных данных:
# Boogeyman 66 65 66 Battleground 50 49 50
# Вариант

class Book(object):
    count = ''
    name = ''
    def __init__(self, nam, cnt):
        self.count = int(cnt)
        self.name = nam
    def __del__(self):
        None
    def chislo(self):
        return(str(self.count))

    def take(self):
        self.count -= 1
        return(str(self.count))

    def vozvr(self):
        self.count += 1
        return(str(self.count))       

if __name__ == '__main__':    
    vh =input()
    books = vh.split()
    cl_book=[]
    for i in range(int(len(books)/2)):
        cl_book.append(Book(books[2*i], books[2*i+1]))
    res = []
    for j in cl_book:
        res.append(j.name + ' ' + j.chislo() + ' ' + j.take() + ' ' +j.vozvr())
    resj = ' '.join(res)
    print(resj)

