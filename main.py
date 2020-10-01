from people.people import *


allen = Person()


print(f"Income: {allen.income}")
for day in range(50):
    print(f"Money: {allen.money}")
    print(f"Health: {allen.health}")
    print(f"Hunger: {allen.hunger}")
    print(f"Energy: {allen.energy}")
    print(f"Food: {allen.food}")
    print("----------")
    input("Type anything to continue.")
    dead = allen.update(day + 1)

    if dead:
        print("Allen has died. Fs in the chat.")
        break
