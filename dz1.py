class cat:
    count_of_cat = 0
    def __init__(self, name, age=3, live=7):
        self.name = name
        self.age = age
        self.live = live
        print("Mau!")
        cat.count_of_cat += 1

    def __str__(self):
        return f"Я кіт {self.name}, мені {self.age} років і в мене {self.live} житів"

    # def info(self):
    #     print(f"Я {self.name}, мені {self.age} років")



    def __len__(self):
        return self.age



    def grow(self, delta=1):
        if self.age + delta > 20:
            print("Error Age")
            return
        self.age += delta

    def evil(self, cot=1):
        if self.live + cot > 9:
            print("Error live")
            return
        self.live += cot
        if self.live + cot < 1:
            print(f"кіт {self.name} пішов")
        self.live += cot



Barni = cat(name="Barni", live=4)
print(Barni.age)
Barni.grow(6)
Tom = cat(name="Tom", age=5)
Tom.evil(4)
print(Barni)
print(Tom)
print(cat.count_of_cat)