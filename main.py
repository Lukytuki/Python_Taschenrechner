def addieren(a, b):
    return a + b


def divison(a, b):
    if b == 0:
        print("Error, Divison durch 0 Nicht moeglich")
        return 0
    else:
        return a / b


def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")

    match wahl:
        case "1":
            print("Resultat: {}".format(addieren(2, 3)))
            # Hier Funktion für Addition einfügen
        case "2":
             #Hier Funktion für die Subtraktion einfügen

        case "3":
             #Hier die Funktion für die Multiplikation einfügen

        case "4":
            print("Resultat: {}".format(divison(2, 3)))
        # Hier die Funktion für die Division einfügen

        case _:
            print("Falsche Auswahl, das Programm wird beendet.")


if __name__ == "__main__":
    main()
