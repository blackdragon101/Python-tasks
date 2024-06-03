class Chair:
    def __init__(self, color, height, material):
        self.color = color
        self.height = height
        self.material = material

    def display(self):
        print(f"Chair Color: {self.color}")
        print(f"Chair Height: {self.height}")
        print(f"Chair Material: {self.material}")
