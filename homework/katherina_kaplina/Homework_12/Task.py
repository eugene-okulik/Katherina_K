class Flowers:
    flower = True

    def __init__(self, name, color, height, smell, average_lifetime, cost):
        self.__name = name
        self.__color = color
        self.__height = height
        self.__smell = smell
        self.__average_lifetime = average_lifetime
        self.__cost = cost

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def height(self):
        return self.__height

    @property
    def smell(self):
        return self.__smell

    @property
    def average_lifetime(self):
        return self.__average_lifetime

    @property
    def cost(self):
        return self.__cost


class ForestFlowers(Flowers):
    place_of_growth = 'forest'

    def __init__(self, name, color, height, smell, average_lifetime, cost, poisonous):
        super().__init__(name, color, height, smell, average_lifetime, cost)
        self.poisonous = poisonous


class WildFlowers(Flowers):
    place_of_growth = 'meadow'


may_lily = ForestFlowers('lily_of_the_valley', 'white', 10, 'strong', 2, 50, True)
corallorhiza = ForestFlowers('candystick', 'white', 50, 'weak', 10, 100, False)
coralroot = ForestFlowers('coralroot', 'white', 10, 'weak', 15, 30, False)

violet = WildFlowers('violet', 'violet', 15, 'medium', 7, 60)
taraxacum_officinale = WildFlowers('dandelion', 'yellow', 50, 'strong', 4, 40)
cichorium_intybus = WildFlowers('Chicory', 'white', 80, 'weak', 6, 20)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers
        self.price = sum(flower.cost for flower in flowers)

    def fading_time(self):
        avr_lifetime = round((sum(flower.average_lifetime for flower in self.flowers) / len(self.flowers)), 1)
        return avr_lifetime

    def sort_by_color(self, color):
        sorted_flowers = [flower.name for flower in self.flowers if flower.color == color]
        if not sorted_flowers:
            return f"No flowers with {color} color in the bouquet"
        return f"Sorted flowers by the {color} color: {', '.join(sorted_flowers)}"

    def sort_by_cost(self, cost):
        sorted_flowers = [flower.name for flower in self.flowers if flower.cost == cost]
        if not sorted_flowers:
            return f"No flowers with {cost} cost {cost} in the bouquet"
        return f"Sorted flowers with the cost {cost}: {', '.join(sorted_flowers)}"

    def sort_by_height(self, height):
        sorted_flowers = [flower.name for flower in self.flowers if flower.height > height]
        if not sorted_flowers:
            return f"No flowers with height more {height} in the bouquet"
        return f"Sorted flowers with the height more {height}: {', '.join(sorted_flowers)}"

    def search_by_lifetime(self, lifetime):
        sorted_flowers = [flower.name for flower in self.flowers if flower.average_lifetime > lifetime]
        if not sorted_flowers:
            return f"No flowers with lifetime more {lifetime} in the bouquet"
        return f"Flowers with the lifetime more {lifetime} days: {', '.join(sorted_flowers)}"


bouquet_1 = Bouquet([may_lily, taraxacum_officinale, cichorium_intybus])
bouquet_2 = Bouquet([corallorhiza, coralroot, violet])

print(f"The fading time for the bouquet is near {bouquet_1.fading_time()} days")
print(f"The price for the bouquet is {bouquet_1.price} byn")
print(bouquet_1.sort_by_color('white'))
print(bouquet_1.sort_by_cost(20))
print(bouquet_1.sort_by_height(10))
print(bouquet_1.search_by_lifetime(3))
