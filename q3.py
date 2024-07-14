# creating a class and object program with class name as Circle

# class defination
class Circle():

    def __init__(self,x,y,r): # init method
        
        self.x_coordinate=x
        self.y_coordinate=y
        self.radius=r

    def get_area(self): # area function

        self.area= ((22/7)) * (self.radius**2)
        return self.area
    
    def get_perimeter(self): # perimeter function

        self.perimeter= 2* (22/7) * self.radius
        return self.perimeter
    
    def get_circumference(self): # circumference function
        return self.get_perimeter()

# input from user
x_=int(input("Enter the X-cooridnate of center of circle: "))
y_=int(input("Enter the Y-cooridnate of center of circle: "))
r=float(input("Enter the radius of circle: "))    

#object declaration
circle=Circle(x_,y_,r)

# displaying the area of circle
area=circle.get_area()
print("The area of circle= ",area)

# displaying the perimeter of circle
perimeter=circle.get_perimeter()
print("The Perimeter of circle= ",perimeter)

# displaying the circumference of circle
circumference=circle.get_circumference() 
print("The Circumference of circle= ",circumference)
