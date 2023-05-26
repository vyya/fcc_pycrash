class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_res(self):
        print(f"You're welcome to the {self.name} restaurant with remarkable {self.cuisine} cuisine")

    def open_res(self):
        print(f"The {self.name} restaurant is now opened")

antler = Restaurant('Antler', 'Italian')
vista = Restaurant('Vista', 'Greek')
gold = Restaurant ('Golden touch', 'Arabic')
antler.describe_res()
antler.open_res()
gold.describe_res()
gold.open_res()
