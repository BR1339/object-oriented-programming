#задание 1
class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return [self.x, self.y, self.z]

class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None

class Entity(BaseObject):
    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Thing(BaseObject):
    pass

# Пример использования:
block = Block(1, 2, 3)
entity = Entity(4, 5, 6)
thing = Thing(7, 8, 9)

print(block.get_coordinates())  # [1, 2, 3]
block.shatter()
print(block.get_coordinates())  # [None, None, None]

print(entity.get_coordinates())  # [4, 5, 6]
entity.move(7, 8, 9)
print(entity.get_coordinates())  # [7, 8, 9]

print(thing.get_coordinates())  # [7, 8, 9]

#задание 2
class Acellularia:
    pass

class Cellularia:
    pass

class Prokaryota(Cellularia):
    pass

class Eukaryota(Cellularia):
    pass

class Unicellularia(Eukaryota):
    pass

class Fungi(Eukaryota):
    pass

class Plantae(Eukaryota):
    pass

class Animalia(Eukaryota):
    pass

# Пример использования:
virus = Acellularia()
bacteria = Prokaryota()
amoeba = Unicellularia()
mushroom = Fungi()
tree = Plantae()
dog = Animalia()

#задание 3
class User:
    def solve(self, n):
        pass

class Student(User):
    pass

class Teacher(User):
    def check_solution(self, user, n):
        pass

class Admin(User):
    def edit(self, n):
        pass

class SuperAdmin(Admin):
    def grant(self, user):
        pass

# Пример использования:
student = Student()
teacher = Teacher()
admin = Admin()
super_admin = SuperAdmin()

student.solve(1)
teacher.check_solution(student, 1)
admin.edit(1)
super_admin.grant(teacher)

#задание 4
class User:
    def __init__(self, name):
        self.name = name
        self.wall = []

    def send_message(self, user, message):
        print(f'Сообщение для {user.name}: {message}')

    def post(self, message):
        self.wall.append(message)
        print(f'{self.name} отправил сообщение на стену: {message}')

    def info(self):
        return ""

    def describe(self):
        print(f'{self.name} {self.info()}')

class Person(User):
    def __init__(self, name, birth_date):
        super().__init__(name)
        self.birth_date = birth_date

    def info(self):
        return f'Дата рождения: {self.birth_date}'

    def subscribe(self, user):
        print(f'{self.name} подписался на {user.name}')

class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f'Описание: {self.description}'

# Пример использования:
person = Person("Иван", "01.01.1990")
community = Community("Геймеры", "Сообщество любителей игр")

person.describe()
community.describe()

person.send_message(community, "Привет!")
community.post("Добро пожаловать в наше сообщество!")
person.subscribe(community)

#задание 5
class Animal:
    def breathe(self):
        pass

    def eat(self):
        pass

class Fish(Animal):
    def swim(self):
        pass

class Bird(Animal):
    def lay_eggs(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        pass

# Пример использования:
fish = Fish()
bird = Bird()
flying_bird = FlyingBird()

fish.swim()
bird.lay_eggs()
flying_bird.fly()

#задание 6
class Transport:
    pass

class WaterTransport(Transport):
    pass

class AirTransport(Transport):
    pass

class Aviation(AirTransport):
    pass

class Airship(AirTransport):
    pass

class Balloon(AirTransport):
    pass

class LandTransport(Transport):
    pass

class RailwayTransport(LandTransport):
    pass

class AutomobileTransport(LandTransport):
    pass

class BicycleTransport(LandTransport):
    pass

class AnimalDrivenTransport(LandTransport):
    pass

class SpaceTransport(Transport):
    pass

# Пример использования:
boat = WaterTransport()
plane = Aviation()
dirigible = Airship()
balloon = Balloon()
train = RailwayTransport()
car = AutomobileTransport()
bike = BicycleTransport()
horse_cart = AnimalDrivenTransport()
spaceship = SpaceTransport()

#задание 7
class Shape:
    pass

class Polygon(Shape):
    pass

class Triangle(Polygon):
    pass

class IsoscelesTriangle(Triangle):
    pass

class EquilateralTriangle(Triangle):
    pass

class Quadrilateral(Polygon):
    pass

class Parallelogram(Quadrilateral):
    pass

class Rectangle(Parallelogram):
    pass

class Square(Rectangle):
    pass

#задание 8
class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(n) for n in range(1, N + 1))

class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2

class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3

# Пример использования:
summator = Summator()
square_summator = SquareSummator()
cube_summator = CubeSummator()

print(summator.sum(5))  # 15
print(square_summator.sum(5))  # 55
print(cube_summator.sum(5))  # 225

#задание 9
class Profile:
    def __init__(self, profession):
        self.profession = profession

    def info(self):
        return ""

    def describe(self):
        print(f'{self.profession} {self.info()}')

class Vacancy(Profile):
    def __init__(self, profession, salary):
        super().__init__(profession)
        self.salary = salary

    def info(self):
        return f'Предлагаемая зарплата: {self.salary}'

class Resume(Profile):
    def __init__(self, profession, experience):
        super().__init__(profession)
        self.experience = experience

    def info(self):
        return f'Стаж работы: {self.experience}'

# Пример использования:
vacancy = Vacancy("Программист", 5000)
resume = Resume("Программист", 3)

vacancy.describe()
resume.describe()

#задание 10
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

# Пример использования:
triangle = Triangle(3, 4, 5)
equilateral_triangle = EquilateralTriangle(3)

print(triangle.perimeter())  # 12
print(equilateral_triangle.perimeter())  # 9

#задание 11
class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(n) for n in range(1, N + 1))

class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b

class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)

class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)

# Пример использования:
summator = Summator()
square_summator = SquareSummator()
cube_summator = CubeSummator()

print(summator.sum(5))  # 15
print(square_summator.sum(5))  # 55
print(cube_summator.sum(5))  # 225
