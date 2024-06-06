#задача 1
class Selector:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_odds(self):
        return [num for num in self.numbers if num % 2 != 0]

    def get_evens(self):
        return [num for num in self.numbers if num % 2 == 0]

values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))

#задача 2
class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = ''
        for word in self.words:
            if len(line) + len(word) + 1 > self.width:
                print(line.strip())
                line = ''
            line += word + ' '
        if line:
            print(line.strip())
        self.words = []

class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = ''
        for word in self.words:
            if len(line) + len(word) + 1 > self.width:
                print(line.strip().rjust(self.width))
                line = ''
            line += word + ' '
        if line:
            print(line.strip().rjust(self.width))
        self.words = []

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()

#задача 3
class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f'{self.month:02d}.{self.day:02d}.{self.year}'

class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f'{self.day:02d}.{self.month:02d}.{self.year}'

american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())

#задача 4
class MinStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        return min(self.values) if self.values else None

class MaxStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        return max(self.values) if self.values else None

class AverageStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        return sum(self.values) / len(self.values) if self.values else None

values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

#задача 5
class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            return self.table[row][col]
        return None

    def set_value(self, row, col, value):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            self.table[row][col] = value

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        return len(self.table[0])

tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()

#задача 6
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def intersection(self, other):
        x1 = max(self.x, other.get_x())
        y1 = max(self.y, other.get_y())
        x2 = min(self.x + self.w, other.get_x() + other.get_w())
        y2 = min(self.y + self.h, other.get_y() + other.get_h())

        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2 - x1, y2 - y1)
        return None

# Пример использования:
rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())

#задача 7
class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            return self.table[row][col]
        return None

    def set_value(self, row, col, value):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            self.table[row][col] = value

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        return len(self.table[0])

    def delete_row(self, row):
        if 0 <= row < len(self.table):
            del self.table[row]

    def delete_col(self, col):
        if 0 <= col < len(self.table[0]):
            for row in self.table:
                del row[col]

    def add_row(self, row):
        if 0 <= row <= len(self.table):
            self.table.insert(row, [0] * len(self.table[0]))

    def add_col(self, col):
        if 0 <= col <= len(self.table[0]):
            for row in self.table:
                row.insert(col, 0)

# Пример использования:
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

#задача 8
class Person:
    def __init__(self, first_name, middle_name, last_name, phones):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phones = phones

    def get_phone(self):
        return self.phones[0] if self.phones else None

    def get_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def get_work_phone(self):
        return self.phones[1] if len(self.phones) > 1 else None

    def get_sms_text(self):
        return f'Уважаемый {self.first_name} {self.middle_name}, примите участие в нашем беспроигрышном конкурсе для физических лиц!'

class Company:
    def __init__(self, name, type, phones, *args):
        self.name = name
        self.type = type
        self.phones = phones
        if self.type == 'OOO':
            self.last_name = args[0]
            self.first_name = args[1]
            self.middle_name = args[2]

    def get_phone(self):
        return self.phones[0] if self.phones else None

    def get_name(self):
        if self.type == 'OOO':
            return f'{self.name} {self.first_name} {self.middle_name} {self.last_name}'
        return self.name

    def get_work_phone(self):
        return self.get_phone()

    def get_sms_text(self):
        if self.type == 'OOO':
            return f'Уважаемый {self.first_name} {self.middle_name}, примите участие в нашем беспроигрышном конкурсе для физических лиц!'
        return f'Уважаемый руководитель {self.name}, примите участие в нашем беспроигрышном конкурсе для компаний!'

def send_sms(*args):
    for obj in args:
        phone = obj.get_phone()
        if phone:
            print(f'Отправлено СМС на номер {phone} с текстом: {obj.get_sms_text()}')

person1 = Person('Иван', 'Иванович', 'Иванов', ['89001234567', '89007654321'])
company1 = Company('Рога и копыта', 'ООО', ['89001234567'], 'Петр', 'Петрович', 'Петров')
company2 = Company('Рога и копыта', 'АО', ['89001234567'])
send_sms(person1, company1, company2)

#задача 9
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_width(self):
        return self.w

    def get_height(self):
        return self.h

    def get_bottom_left(self):
        return Point(self.x, self.y)

    def get_top_right(self):
        return Point(self.x + self.w, self.y + self.h)

    def get_bottom_right(self):
        return Point(self.x + self.w, self.y)

    def get_top_left(self):
        return Point(self.x, self.y + self.h)

rect = Rectangle(0, 0, 10, 5)
print(rect.get_bottom_left())  # Output: Point(0, 0)
print(rect.get_top_right())    # Output: Point(10, 5)
print(rect.get_bottom_right()) # Output: Point(10, 0)
print(rect.get_top_left())     # Output: Point(0, 5)

#задача 10
class OddEvenSeparator:
    def __init__(self):
        self.odds = []
        self.evens = []

    def add_number(self, number):
        if number % 2 == 0:
            self.evens.append(number)
        else:
            self.odds.append(number)

    def odds(self):
        return self.odds

    def evens(self):
        return self.evens

# Пример использования:
separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(2)
separator.add_number(3)
separator.add_number(4)
separator.add_number(5)
print(separator.odds)
print(separator.evens)
