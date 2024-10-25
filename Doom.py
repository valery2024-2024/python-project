class House:
    name = " "
    house = 0
    lenght = 0.0
    windth = 0.0

    def calculate_area(self):
        print("Area of House =", self.lenght*self.windth)
        
    
room = House()
room.lenght = 5
room.windth = 2

room.calculate_area()



