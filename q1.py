# creating a class and object program with class name as Person

# class defination
class Person:

    def __init__(self,name,age,gender): # init method
        # intance variable
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self): # introduce function
        print(f"Hello, Everyone My name is: {self.name} and I am {self.age} years old and I am a {self.gender}")

# input from user
name=input("Enter a name: ") 
age=int(input("Enter the age: "))
gender=input("Enter the gender: ")

# object declaration
obj=Person(name,age,gender)
obj.introduce() # function calling by object