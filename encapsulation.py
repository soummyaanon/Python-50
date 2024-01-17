class car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"this is a {self.brand} {self.model}. ")

tesla = car ("Tesla", "CyberTruck")

tesla.display_info()