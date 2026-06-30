# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~ PRINT FUNCTIONS ~~~~~
def optionsMenu():
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("            OPTIONS MENU")
    print("")
    print("          1. View List")
    print("          2. Add Item(s)")
    print("          3. Remove Item(s)")
    print("          4. Edit Item(s)")
    print("          5. Move Item(s)")
    print("          6. Exit")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")


def printList(listIn):
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("              GROCERIES")
    print("")
    if len(listIn) > 0:
        for idx in range(len(listIn)):
            print(f"           {idx+1}. {listIn[idx]}")
    else:
        print("")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")


    # ~~~~~ FILE FUNCTIONS ~~~~~
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


    # ~~~~~ LIST FUNCTIONS ~~~~~
def addItems(listIn, listName):
    listCopy = listIn
    addMore = True
    while addMore:
        printList(listCopy)
        print("Enter an item to add (or 'done' to exit)")
        toAdd = input(" --> ")
        if toAdd in ["done", "exit", "quit"]:
            addMore = False
        else:
            listCopy.append(toAdd)
    saveList(listCopy, listName)


def removeItems(listIn, listName):
    listCopy = listIn
    removeMore = True
    while removeMore:
        validRemove = False
        while not validRemove:
            printList(listCopy)
            print("Enter an item position to remove (or 'done' to exit)")
            toRemove = input(" --> ")
            try:
                toRemove = int(toRemove) - 1
                if toRemove < len(listCopy):
                    validRemove = True
                else:
                    print("")
                    print("Invalid choice - please try again!")
                    print("")
            except ValueError:
                if toRemove in ["done", "quit", "exit"]:
                    validRemove = True
                else:
                    print("")
                    print("Invalid choice - please try again!")
                    print("")
        if toRemove in ["done", "quit", "exit"]:
            removeMore = False
        else:
            listCopy.pop(toRemove)
    saveList(listCopy, listName)


def editItems(listIn, listName):
    listCopy = listIn
    editMore = True
    while editMore:
        validEdit = False
        while not validEdit:
            printList(listCopy)
            print("Enter an item position to edit (or 'done' to exit)")
            toEdit = input(" --> ")
            try:
                toEdit = int(toEdit) - 1
                if toEdit < len(listCopy):
                    validEdit = True
                else:
                    print("")
                    print("Invalid choice - please try again!")
                    print("")
            except ValueError:
                if toEdit in ["done", "quit", "exit"]:
                    validEdit = True
                else:
                    print("")
                    print("Invalid choice - please try again!")
                    print("")
        if toEdit in ["done", "quit", "exit"]:
            editMore = False
        else:
            print("")
            print("Enter an updated entry:")
            newEntry = input(" --> ")
            listCopy[toEdit] = newEntry
    saveList(listCopy, listName)


def moveItems(listIn, listName):
    listCopy = listIn
    moveMore = True
    while moveMore:
        validMoveFrom = False
        while not validMoveFrom:
            printList(listCopy)
            print("Enter position of an item to move (or 'done' to exit)")
            toMoveFrom = input(" --> ")
            try:
                toMoveFrom = int(toMoveFrom) - 1
                if toMoveFrom < len(listCopy):
                    validMoveFrom = True
                else:
                    print("")
                    print("Invalid choice - please try again!")
                    print("")
            except ValueError:
                if toMoveFrom in ["done", "quit", "exit"]:
                    validMoveFrom = True
                else:
                    print("")
                    print("Invalid choice - please try again!")
                    print("")
        if toMoveFrom in ["done", "quit", "exit"]:
            moveMore = False
        else:
            validMoveTo = False
            while not validMoveTo:
                print("")
                print("Enter a new position for the item:")
                toMoveTo = input(" --> ")
                try:
                    toMoveTo = int(toMoveTo) - 1
                    if toMoveTo < len(listCopy):
                        validMoveTo = True
                    else:
                        print("")
                        print("Invalid choice - please try again!")
                        print("")
                except ValueError:
                    print("")
                    print("Invalid choice - please try again!")
                    print("")
            listCopy.insert(toMoveTo, listCopy.pop(toMoveFrom))
    saveList(listCopy, listName)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    appOn = True
    listName = "groceries.txt"

    while appOn:
        # Reload list at the top of every loop; file saved at end of each helper
        groceries = loadList(listName)

        # Print options and verify correct user input (with while loop)
        validMenuChoice = False
        while not validMenuChoice:
            optionsMenu()
            userChoice = input(" --> ")
            
            if userChoice in ["1", "2", "3", "4", "5", "6",
                              "1.", "2.", "3.", "4.", "5.", "6.",
                              "1. View List", "2. Add Item(s)", "3. Remove Item(s)",
                              "4. Edit Item(s)", "5. Move Item(s)", "6. Exit"
                              "exit", "quit", "done"]:
                validMenuChoice = True
            else:
                print("")
                print("Invalid choice - please try again!")
                print("")

        # Check user input and run chosen function
        if userChoice in ["1", "1.", "1. View List"]:
            printList(groceries)
        elif userChoice in ["2", "2.", "2. Add Item(s)"]:
            addItems(groceries, listName)
        elif userChoice in ["3", "3.", "3. Remove Item(s)"]:
            removeItems(groceries, listName)
        elif userChoice in ["4", "4.", "4. Edit Item(s)"]:
            editItems(groceries, listName)
        elif userChoice in ["5", "5.", "5. Move Item(s)"]:
            moveItems(groceries, listName)
        else:
            appOn = False

        # To move (to helpers)
        

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
