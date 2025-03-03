class Flowers:
    def __init__(self,name,color,place,smell):
        self.name = name
        self.color = color
        self.place = place
        self.smell = smell

    def like_flower(self):
        print(f"i like the {self.name}")
    def color_flower(self):
        print(f"The color of {self.name} is {self.color}")