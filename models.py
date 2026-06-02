class Car:

    def __init__(self, brand, model, hp):
        self.brand = brand
        self.model = model
        self.hp = hp


    def get_full_name(self):
        return f"{self.brand} {self.model} ({self.hp} hp)"

    def is_powerful(self):
        if self.hp >= 150:
            return True
        else:
            return False