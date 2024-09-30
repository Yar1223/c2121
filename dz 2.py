import random
class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print("Я навчаюсь")
        self.progress += 0.2
        self.gladness -= 4
    def to_sleep(self):
        print("Я пішов спати")
        self.progress += 0.02
        self.gladness += 3

    def to_chill(self):
        print("Я відпочиваю")
        self.gladness += 5
        self.gladness -= 0.1

    def to_traning(self):
        print("Я тренеруюся")
        self.gladness -= 4
        self.progress += 0.05

    def to_playing_computer(self):
        print("Я граю в компутер")
        self.gladness -= 3
        self.progress -= 0.5

    def info(self):
        print(f"Рівень навчання {self.progress}")
        print(f"Задоволення {self.gladness}")
        print()

    def is_alive(self):
        if self.progress > 7:
            print("Ми все вивчили і закінчили МКА ШАГ")
            self.alive = False
        if self.progress < -0.5:
            print("Ми втратили інтерес до навчання ....")
            self.alive =False
        if self.gladness <= 0:
            print("У мене депресія")
            self.alive = False

    def live(self, day):
        print(f"День {day} з  життя {self.name}")
        print("=====================================")
        choice = random.randint(1, 4)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_chill()
        elif choice == 4:
            self.to_traning()
        self.info()
        self.is_alive()
        choice2 = random.randint(1, 20)
        if choice2 == 15:
            self.to_playing_computer()

student = Student("Artem")
for day in range(366):
    if student.alive == False:
        break
    student.live(day)