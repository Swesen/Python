import random


dice = ["+-------+\n" +
        "|       |\n" +
        "|   #   |\n" +
        "|       |\n"
        "+-------+\n",
        "+-------+\n" +
        "|      #|\n" +
        "|       |\n" +
        "|#      |\n" +
        "+-------+\n",

        "+-------+\n" +
        "|      #|\n" +
        "|   #   |\n" +
        "|#      |\n" +
        "+-------+\n",

        "+-------+\n"+
        "|#     #|\n" +
        "|       |\n" +
        "|#     #|\n" +
        "+-------+\n",

        "+-------+\n" +
        "|#     #|\n" +
        "|   #   |\n" +
        "|#     #|\n" +
        "+-------+\n",

        "+-------+\n" +
        "|#     #|\n" +
        "|#     #|\n" +
        "|#     #|\n" +
        "+-------+\n"]


def PrintListOfDice(diceList):
    for i in diceList:
        print(dice[i - 1])


diceList = []

for i in range(5):
    diceList.append(random.randrange(1, 7))
    PrintListOfDice(diceList)
