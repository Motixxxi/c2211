class Animal:
    """Клас 'Тварина' — описує спільні властивості всіх тварин."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        """Метод, який має перевизначатися у підкласах."""
        return "Тварина видає звук."

    def info(self):
        """Повертає загальну інформацію про тварину."""
        return f"Ім'я: {self.name}, Вік: {self.age} років"



class Dog(Animal):
    """Клас 'Собака' — успадковує властивості від 'Тварина'."""
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "Гав-гав!"

    def info(self):
        return f" Собака: {self.name}, {self.age} років, порода — {self.breed}"



class Cat(Animal):
    """Клас 'Кіт' — успадковує властивості від 'Тварина'."""
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Мяу-мяу!"

    def info(self):
        return f" Кіт: {self.name}, {self.age} років, колір — {self.color}"



if __name__ == "__main__":
    dog = Dog("Рекс", 4, "Німецька вівчарка")
    cat = Cat("Мурчик", 2, "сірий")

    print(dog.info())
    print("Звук:", dog.speak())

    print()
    print(cat.info())
    print("Звук:", cat.speak())
