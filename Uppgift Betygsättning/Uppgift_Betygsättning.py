def grade(laborationDone, correctAnswers):
    if laborationDone == "J":
        if correctAnswers > 75:
            return "VG"
        elif correctAnswers > 50:
            return "G"
    return "IG"


while True:
    print(grade(input("Är laborationen gjord? J/N ").upper(),
                int(input("Hur många korrekta svar? "))))
    if "J" == input("Är du klar? J/N ").upper():
        break
