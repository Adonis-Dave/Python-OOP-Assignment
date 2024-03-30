class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old. My gender is {self.gender} ")
        
someone = Person("David", 22, "Male")

someone.introduce()