# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~ PRINT FUNCTIONS ~~~
def optionsMenu():
    pass


def printList():
    pass


    # ~~~ FILE FUNCTIONS ~~~
def loadList(filename):
    try:
        with open(filename, "r") as listIn:
            loadedList = listIn.readlines()
            for idx in range(len(loadedList)):
                loadedList[idx] = loadedList[idx].replace("\n", "")
    except FileNotFoundError:
        loadedList = []
    finally:
        return loadedList


def saveList(listIn, filename):
    with open(filename, "w") as listOut:
        for idx in range(len(listIn)):
            if idx < len(listIn) - 1:
                listOut.write(f"{listIn[idx]}\n")
            else:
                listOut.write(listIn[idx])


    # ~~~ LIST FUNCTIONS ~~~
def addItems():
    pass


def removeItems():
    pass


def editItems():
    pass


def moveItems():
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    appOn = True
    listName = "groceries.txt"

    while appOn:
        groceries = loadList(listName)

        optionsMenu()
        userChoice = input(" --> ")

        if userChoice == "1":
            printList()
        elif userChoice == "2":
            addItems()
        elif userChoice == "3":
            removeItems()
        elif userChoice == "4":
            editItems()
        elif userChoice == "5":
            moveItems()
        elif userChoice == "6":
            appOn = False
        else:
            print("")
            print("Invalid choice - try again!")


        saveList(groceries, listName)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
