class Animal:
    all_animals = {}
    state = 'Голоден'
    harvested = 'Готов к сбору урожая'
    voice = 'Голос животного'
    feed_type = 'Корм'
    name = 'Имя'

    def feed(self):
        self.state = 'Сыт и доволен'
        print('Животное накормлено')

    def harvest(self):
        if self.state == 'Сыт и доволен':
            self.harvested = 'Урожай собран'
            self.state = 'Голоден'
            print(f'Урожай собран ({self.yield_type})')
        else:
            print('Сначала животное нужно накормить')

    def weight_sum(self):
        all_animal_weight = sum(Animal.all_animals.values())
        print(f'Общий вес животных: {all_animal_weight}кг')

    def max_weight(self):
        max_weight_animal = max(Animal.all_animals.keys(), key = lambda x: Animal.all_animals[x])
        print(f'Самое тяжелое животное: {max_weight_animal}')

class MilkAnimals(Animal):
    yield_type = 'молоко'

    def harvest(self):
        if self.state == 'Сыт и доволен':
            self.harvested = 'Урожай собран'
            self.state = 'Голоден'
            print('Животное подоено')
        else:
            print('Сначала животное нужно накормить')

class Cow(MilkAnimals):
    voice = 'Mo-o'
    animal_type = 'Корова'

    def __init__(self, name='Манька', weight=100):
        self.name = name
        self.weight = weight
        Animal.all_animals[name] = weight

class Goat(MilkAnimals):
    voice = 'Me-e'
    animal_type = 'Коза'

    def __init__(self, name='Рога', weight=50):
        self.name = name
        self.weight = weight
        Animal.all_animals[name] = weight

class WoolAnimals(Animal):
    yield_type = 'шерсть'

    def harvest(self):
        if self.state == 'Сыт и доволен':
            self.harvested = 'Урожай собран'
            self.state = 'Голоден'
            print('Животное острижено')
        else:
            print('Сначала животное нужно накормить')

class Sheep(WoolAnimals):
    voice = 'Me-e'
    animal_type = 'Овца'

    def __init__(self, name='Барашек', weight=50):
        self.name = name
        self.weight = weight
        Animal.all_animals[name] = weight

class Bird(Animal):
    yield_type = 'яйца'

    def harvest(self):
        if self.state == 'Сыт и доволен':
            self.harvested = 'Урожай собран'
            self.state = 'Голоден'
            print('Яйца собраны')
        else:
            print('Сначала животное нужно накормить')

class Goose(Bird):
    voice = 'Ga-ga'
    animal_type = 'Гусь'

    def __init__(self, name='Серый', weight=5):
        self.name = name
        self.weight = weight
        Animal.all_animals[name] = weight

class Duck(Bird):
    voice = 'Quack'
    animal_type = 'Утка'

    def __init__(self, name='Кряква', weight=3):
        self.name = name
        self.weight = weight
        Animal.all_animals[name] = weight

class Han(Bird):
    voice = 'Ko-ko'
    animal_type = 'Курица'

    def __init__(self, name='Кукареку', weight=3):
        self.name = name
        self.weight = weight
        Animal.all_animals[name] = weight

cow1 = Cow(weight=102)
goose1 = Goose()
goose2 = Goose(name='Белый', weight=8)
sheep1 = Sheep(weight=73)
sheep2 = Sheep(name='Кудрявый', weight=56)
han1 = Han(name='Ко-ко',weight=5)
han2 = Han()
goat1 = Goat(weight=43)
goat2 = Goat(name='Копыта')
duck1 = Duck()

cow1.feed()
cow1.harvest()

goose1.harvest()
goose1.feed()
goose1.harvest()

goose2.feed()
goose2.harvest()

sheep1.feed()
sheep1.harvest()

sheep2.feed()
sheep2.harvest()

han1.feed()
han1.harvest()

han2.feed()
han2.harvest()

goat1.feed()
goat1.harvest()

goat2.feed()
goat2.harvest()

duck1.feed()
duck1.harvest()

animal_list = Animal()

animal_list.max_weight()
animal_list.weight_sum()
print(Animal.all_animals)
