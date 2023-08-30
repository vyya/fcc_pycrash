class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    def describe_res(self):
        print(f"You\'re welcome to the {self.name} restaurant with remarkable " 
                f"{self.cuisine} cuisine with more than {self.number_served:,} clients served")

    def open_res(self):
        print(f"The {self.name} restaurant is now opened")


    def increment_number_served(self, clients):
        self.number_served += clients

antler = Restaurant('Antler', 'Italian')
antler.number_served = 700000
antler.increment_number_served(120)
vista = Restaurant('Vista', 'Greek')
gold = Restaurant ('Golden touch', 'Arabic')
print(antler.name)
print(antler.cuisine)
antler.describe_res()
antler.open_res()
gold.describe_res()
gold.open_res()
