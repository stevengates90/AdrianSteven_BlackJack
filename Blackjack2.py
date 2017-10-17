from random import shuffle
import random

class Box():
    def __init__(self, deck):
        self.newdeck = deck

    def Shufflin(self):
        Values = []
        for key in self.newdeck:
            for values in self.newdeck[key]:
                Values.append(values)

        shuffle(Values)

        for i in range(len(Values)):
            if Values[i] == "J" or Values[i] == "Q" or Values[i] == "K":
                Values[i] = 10
        return Values

    def Game(self,Cards):
        hand1 = []
        hand1.append(Cards.pop())
        hand1.append(Cards.pop())
        print(hand1)

        while True:
            request = input("\nDo you want to add your hand?(Y/N)").lower()
            if request == "yes" or request == "y":
                hand1.append(Cards.pop())
                print(hand1)
                if len(hand1)>5:
                    break
            elif request == "no" or request == "n":
                break

        if "A" in hand1:
            countA = hand1.count("A")
            hand1 = list(filter(lambda a: a != "A", hand1))
            result = sum(hand1)
            result += countA
            if result <12:
                result += 10
                return result
            else:
                return result
        else:
            result = sum(hand1)
            return result
    def RNG(self):
        rng = random.randint(13,21)
        return rng

class Brand(Box):
    def __init__(self):
        super(Brand, self).__init__(1)
        self.type = "Marlboro"


print("================================================================================")
print("\t\t\t\t\t\t\tWelcome to the Devil's Emporium!")
print("\t\t\t\t\t\t\tWould you like to bet your soul?")
print("================================================================================")
request = input("Will it be a yes, or will it be a no? (Y/N)").lower()

if request == "y" or request == "yes":
    print("\nVery Well! Let's play some Blackjack!")
    start = 1
elif request == "n" or request == "no":
    print("\nThen get off my lawn!")
    start = 0
else:
    print("\nAre you unsure? Then let's just play the game!")
    start = 1

if start == 1:
    Deck = {"Spades":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],"Hearts":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],
            "Clovers":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],"Diamonds":["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]}
    x = Box(Deck)
    value = x.Game(x.Shufflin())
    if value>21:
        print("Bust! You lost the game.")
        print("It's time for you to pay!")
    else:
        if value>x.RNG():
            print("\nYou have won the game!")
            print("You've earned the casino and the 'Devil's Dice'!")
        else:
            print("\nYou have lost the game! And now you must pay the price!!")
            print("Your points is",value,", while the devil's is",x.RNG())
            print("Or perhaps you could pay your debt back with some soul contracts....")
