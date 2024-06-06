from abc import ABC, abstractmethod

# 1. Абстрактный класс Animal
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# 2. Конкретные классы животных
class Lion(Animal):
    def make_sound(self):
        return "Рычание!"

class Monkey(Animal):
    def make_sound(self):
        return "Визг!"

class Elephant(Animal):
    def make_sound(self):
        return "Трубление!"

# 3. Абстрактная фабрика AnimalFactory
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# 4. Конкретные фабрики для каждого вида животных
class LionFactory(AnimalFactory):
    def create_animal(self):
        return Lion()

class MonkeyFactory(AnimalFactory):
    def create_animal(self):
        return Monkey()

class ElephantFactory(AnimalFactory):
    def create_animal(self):
        return Elephant()

# 5. Функция для взаимодействия с животным
def interact_with_animal(factory: AnimalFactory):
    animal = factory.create_animal()
    sound = animal.make_sound()
    print(f"Звук: {sound}")


lion_factory = LionFactory()
monkey_factory = MonkeyFactory()
elephant_factory = ElephantFactory()

interact_with_animal(lion_factory)     # Вывод: Звук: Рычание!
interact_with_animal(monkey_factory)   # Вывод: Звук: Визг!
interact_with_animal(elephant_factory) # Вывод: Звук: Трубление!

