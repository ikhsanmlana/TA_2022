dict = {'Dog': '13', 'Cat': '20', 'Rabbit': '11'}
dict2 = {'Dog': 1000000, 'Cat': 750000, 'Rabbit': 1500000}
dict3 = {'Dog': 250000, 'Cat': 150000, 'Rabbit': 500000}

class Pet:
    def __init__(self,animal):
        self.animal = animal
        self.amount = dict.get(self.animal)


    def getPet(self):
        return self.amount

    def showPet(self):
        return self.animal

class Buy:
    def __init__(self, animal,amount):
        self.animal = animal
        self.amount = amount

    def getPrice(self):
        return self.price

    def buy_pet(self):
        Buy.price = dict2.get(self.animal)
        self.price = int(self.price * self.amount)
        return self.price

class Sell:

    def __init__(self,animal,amount):
        self.animal = animal
        self.amount = amount

    def sell_pet(self):
        Sell.price = dict3.get(self.animal)
        return int(self.price * self.amount)

# pets = Pet("Turtle")
#
# print(pets.getPet())

def main():
    print ("Welcome to the Pet Shop!")
    while True:
        x = input("What would you like to do? (V to view, B to buy, S to sell, and E to EXIT) ")
        if x == "v" or x == "V":
            y = input("What animal do you want? ")
            pets = Pet(y)
            if y in dict.keys():
                print("We have " + str(pets.getPet()) + " " + str(pets.animal))
                continue
            else:
                print("Sorry we don't have those in our shop.")
                continue

        elif x == "b" or x == "B":
            z = input("What animal do you want? ")
            if not (z in dict.keys()):
                print ("Sorry! We do not have those.")
                continue
            z2 = input("How many do you want? ")
            z3 = int(dict.get(z))
            pets = Buy(z, z2)
            if z2 > z3:
                print("Sorry! We do not have that many " + z + "s")
                continue
            print (str(pets.amount) + " " + str(pets.animal) + " " + "is " + str(pets.buy_pet()))
            y = input("Confirm purchase? Y/N ")
            if y == "y" or y == "Y":
                print("Thank you for your purchase, you have bought " + str(pets.amount) + " " + str(pets.animal) + "(s)")
                dict[z] = z3 - z2

                continue
            elif y == "N" or y == "n":
                print ("Okay then.")
                continue
            elif not (pets in dict):
                print ("Sorry we don't have those!")
                continue

        elif x == "S" or x == "s":
            z = input("What animal do you have? ")
            z2 = input("How many do you want to sell? ")
            pets = Sell(z, z2)
            print (str(pets.amount) + " " + str(pets.animal) + " " + "is " + str(pets.sell_pet()))
            y = input("Do you still want to sell your animals? Y/N ")
            if y == "Y" or y == "y":
                print("Thank you for trading with us" + "\n")
                dict.update({z: int(dict[z]) + z2})
                continue
            else:
                print("Okay." + "\n")
                continue
        else:
            print ("Thank you for visiting our store, see you next time!")
            break

main()