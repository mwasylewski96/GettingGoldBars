import random
import time

Attempts = [i+1 for i in range(5)]
#Containers
BoxOrNothing = ("Box! :)", "Nothing :(")
BoxesColours = ("Green Box", "Orange Box", "Purple Box", "Gold Legendary Box")
BoxesWithGoldBar = {"Green Box": 1000, "Orange Box": 4000, "Purple Box": 9000, "Gold Legendary Box": 16000}
def RandomVariation(randomvariation=0):
    randomvariation = random.randint(-10,10)
    return randomvariation
def RandomBoxorNothing(BoxOrNothing):
    BoxOrNothingRandom = random.choices(BoxOrNothing, [60, 40], k=1)
    BoxOrNothingRandom = BoxOrNothingRandom[0]
    return BoxOrNothingRandom
def RandomBoxesWithGoldBar(BoxesColours):
    BoxesWithGoldBarRandom = random.choices(BoxesColours, [75, 20, 4, 1], k=1)
    BoxesWithGoldBarRandom = BoxesWithGoldBarRandom[0]
    return BoxesWithGoldBarRandom
def GettingGoldBars(BoxesWithGoldBarRandom,BoxesWithGoldBar):
    randomvariation = (RandomVariation()+100)/100
    if BoxesWithGoldBarRandom == "Green Box":
        gold = BoxesWithGoldBar["Green Box"]*randomvariation
    if BoxesWithGoldBarRandom == "Orange Box":
        gold = BoxesWithGoldBar["Orange Box"]*randomvariation
    if BoxesWithGoldBarRandom == "Purple Box":
        gold = BoxesWithGoldBar["Purple Box"]*randomvariation
    if BoxesWithGoldBarRandom == "Gold Legendary Box":
        gold = BoxesWithGoldBar["Gold Legendary Box"]*randomvariation
    return gold
SUM = 0
for attempt in Attempts:
    BoxOrNothingRandom = " "
    BoxOrNothingRandom = RandomBoxorNothing(BoxOrNothing)
    print(BoxOrNothingRandom)
    time.sleep(1)
    if BoxOrNothingRandom != "Nothing :(":
        gold = 0
        BoxesWithGoldBarRandom = " "
        BoxesWithGoldBarRandom = RandomBoxesWithGoldBar(BoxesColours)
        print(BoxesWithGoldBarRandom)
        time.sleep(1)
        #GettingGoldBars(BoxesWithGoldBarRandom,BoxesWithGoldBar)
        gold = GettingGoldBars(BoxesWithGoldBarRandom,BoxesWithGoldBar)
        print("You get", gold, "Goldbar")
        time.sleep(1)
        SUM = SUM + gold
time.sleep(1)
print("****TOTAL GOLD **** = ", SUM, "Goldbar")
