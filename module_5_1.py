class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        i = 1
        while i <= new_floor:
            if i <= self.number_of_floors:
                print(i)
                i+=1
            else:
                print('Такого этажа не существует')
                break

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
print()
h2.go_to(10)