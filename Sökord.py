from pathlib import Path


searchText = ["UFDACYGLKP",
              "KABINAQXYV",
              "YLLNGTTAKE",
              "ZMPLWARZNO",
              "GVFAIXAAFY",
              "YMPLPGLSOH",
              "WGVHFPACKW",
              "AFTERTLTHU",
              "TNKIDCBEOS",
              "ZBAMANSWER"]
foundText = []


def LoadFile(filePath):
    global searchText
    openFile = open(filePath)
    searchText = []
    for line in openFile.readlines():
        searchText.append(line[:10])


def LookForWord(word):
    origin = []

    for y in range(len(searchText)):
        for x in range(len(searchText[y])):
            if (searchText[y][x].lower() == word[0].lower()):
                origin.append({"X": x, "Y": y})

    for pos in origin:
        for dirY in range(-1, 2):
            for dirX in range(-1, 2):
                if (dirY == 0 and dirX == 0):
                    continue
                if (SearchInDirection(word, pos["X"], pos["Y"], dirX, dirY)):
                    foundText.append({"word": word,
                                      "origin": {"X": pos["X"], "Y": pos["Y"]},
                                      "direction": {"X": dirX, "Y": dirY},
                                      "length": len(word)})


# Search from point X/Y in a direction dirX/Y
def SearchInDirection(word, x, y, dirX, dirY):
    for i in range(1, len(word)):
        posX = x + dirX * i
        posY = y + dirY * i
        if (posX < 0 or posY < 0 or posX >= len(searchText[0]) or posY >= len(searchText)):
            return False

        wordChar = word[i].lower()
        searchTextChar = searchText[posY][posX].lower()

        if (wordChar != searchTextChar):
            return False

    return True


def PrintFoundText():
    textToPrint = searchText

    for found in foundText:
        for i in range(found["length"]):
            posX = found["origin"]["X"] + found["direction"]["X"] * i
            posY = found["origin"]["Y"] + found["direction"]["Y"] * i
            textToPrint[posY] = textToPrint[posY][:posX] + \
                textToPrint[posY][posX].lower() + textToPrint[posY][posX + 1:]

    return textToPrint


while True:
    print("Words found:")
    for found in foundText:
        print(found["word"])

    for i in PrintFoundText():
        print("  ".join(i))

    userInput = input(
        "Input word to find in text or 'load' to load a new file: ")

    if (userInput.lower() == "load"):
        filePath = Path(input("Please input the full file path: "))
        LoadFile(filePath)
        foundText = []
    else:
        LookForWord(userInput)
