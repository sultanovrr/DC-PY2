import doctest

class Country():
    """описание страны"""
    def __init__(self, name:str, population: int, area:int):
        if not isinstance(name, str):
            raise TypeError
        self.name = name
        if not isinstance(population, int):
            raise TypeError
        self.population = population
        if not isinstance(area, int):
            raise TypeError
        if area <= 0:
            raise ValueError
        self.area = area
    def size_of_population(self):
        if self.population >= 100000000:
            print ("страна" + self.name + "имеет большое население")
    def size_of_area(self):
        if self.area > 500000:
            print("Страна" + self.name + "большая")
country1 = Country("Russia", 145000000, 17100000)

class school():
    """описание школы """
    def __init__(self, street:str, number:int):
        if not isinstance(street, str):
            raise TypeError
        self.street = street
        if not isinstance(number, int):
            raise TypeError
        self.number = number
    def built(self):
        print("Школа №" + self.number + "расположена на улице" + self.street)
    def notbuilt(self):
        if self.number > 60:
            print("Школа №" + self.number + "не построена")
school_ = school("Мира", 10)

class film():
    """описание фильма """
    def __init__(self, name:str, year:int):
        if not isinstance(name, str):
            raise TypeError
        self.name = name
        if not isinstance(year, int):
            raise TypeError
        self.year = year
    def film_(self):
        print("Фильм" + self.name + "вышел в" + self.year + "году")
    def film_(self):
        if self.year > 2023:
            print("Фильм" + self.name + "ожидает премьеры в" + self.year + "году")
film1 = film("Интерстеллар",2013)