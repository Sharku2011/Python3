import time
import random
def populate_doors():
        door=['goat', 'goat', 'goat']
        door[random.randint(0,2)]='car'
        return door
wins = 0
losses = 0

a = time.time()

for x in range(100000):
        doors=populate_doors()
        first_choice=random.randint(0,2)
        for y in range(2):
                if doors[y] != 'car' and y != first_choice:
                        doors[y] = 'out'
                        break
        if doors[first_choice] == 'car':
                losses = losses + 1
        else:
                wins = wins + 1
print("All choices were switched.")
print("Wins:", wins)
print("Losses:", losses)

print("Python elapsed",(time.time()-a))
