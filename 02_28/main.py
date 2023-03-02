from datetime import date
import datetime

# today = date.today()
# print("Today's date:", today)


class Person:
    description: str = "A simple human being"


    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    # Hello, my name is <name>
    def greet(self):
        return f"Hello my name is {self.name}"
    
    def walk_away(self):
        return f"{self.name} is walking away..."
    
    def calculate_days_left_till_black_friday(self) -> int:
        # get todays date
        # initialise black friday date
        # black_friday_date - todays_date
        today = date.today()
        balck_friday_day = datetime.date(2023, 11, 24)
        delta = balck_friday_day - today
        return delta.days
    
    def get_eye_color(self, eye_color: str):
        return eye_color
    
    def __repr__(self):
        return f"Person: {self.name}-{self.surname}"
    
    def __str__(self):
        return f"P: {self.name}-{self.surname}"
    

person = Person("Vytautas", "Sluckas")
print(person)
print(repr(person))
# print(person.get_eye_color("Blue"))
# print(person.calculate_days_left_till_black_friday())
# person2 = Person("Antanas", "Fontanas")


# print(Person.description)
# print(person.greet())
# print(person.walk_away())
# print(person2.greet())
