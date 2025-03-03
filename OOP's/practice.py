class Cars:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} is my favourite car"

car1 = Cars("defender","black")

print(car1)