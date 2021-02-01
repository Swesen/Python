import random

# 1
def ten():
    return list(range(1, 11))

# print(ten())


# 2
def even():
    return list(range(2, 101, 2))

# print(even())
# for i in even():
#     if (i % 2 != 0):
#         print("error")


# 3
def randomListOfN(ammount):
    answer = []
    for _ in range(ammount):
        answer.append(int(random.randrange(1000000)))
    return answer

# print(randomListOfN(23))


# 4
def bubbleSort(listToSort):
    lengthOfList = len(listToSort)
    lastSorted = lengthOfList
    done = False
    while (not done):
        done = True
        for i in range(lastSorted - 1):
            if (listToSort[i] > listToSort[i + 1]):
                temp = listToSort[i]
                listToSort[i] = listToSort[i+1]
                listToSort[i + 1] = temp

                done = False
                lastSorted = i + 1

        if (not done):
            print("Sorted {} out of {}".format(
                lengthOfList - lastSorted, lengthOfList))
    print("Done sorted {} out of {}".format(
        lengthOfList, lengthOfList))
    return listToSort

# listThatNeedsSorting = randomListOfN(15)
# print("List before sorting: " + str(listThatNeedsSorting))
# bubbleSort(listThatNeedsSorting)
# print("List sorted: " + str(listThatNeedsSorting))