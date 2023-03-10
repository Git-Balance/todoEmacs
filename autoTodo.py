import re
from datetime import datetime, timedelta
import argparse

if __name__ == "__main__":
    # Parser variables
    parser = argparse.ArgumentParser(description="A program that creates todo items for emacs.")
    parser.add_argument("-d", "--dates", help="Add items in the future", type=int)
    args = parser.parse_args()
    
    # Date variables
    dObject = "" # See if this needs to be a datetime object at start
    dString = "" # Actually string
    present = ""
    dateAmount = -1

    # Files
    datesFile = "/home/user/Todo/dates.txt" # "/home/user/Scripts/Todo/dates.txt"
    todoFile = "/home/user/Todo/dec.org"

    ## Finding dates

    # If there is no argument
    # Set dateAmount to 0
    if args.dates is None:
        dateAmount = 0

    # If there is an argument
    # Set dateAmount to argument
    elif args.dates is not None and args.dates > 0:
        dateAmount = args.dates

    # If the value of dateAmount is still -1
    # Raise an error
    if dateAmount < 0:
        raise Exception("Error: dateAmount is negative (" + str(dateAmount) + ")")
    
    ## Attach value to date variables
    # Find current date
    present = datetime.now()

    ## Start loop of finding and attaching dates
    n = 0
    dateTrue = 0
    while (n <= dateAmount):
        dateTrue = 0
        
        ## Attach value to date variable
        # Make dObject equal the provided date
        dObject = present + timedelta(n)
        # Make dString equal string of dObject in uppercase
        dString = dObject.strftime("%d %b %Y").upper()

        ## Open date file
        fRead = open(datesFile, "r")

        ## Check datesFile for n
        for line in fRead:
            nLine = re.sub("\n", "", line)
            if dString in nLine:
                dateTrue += 1;

        ## Check dateTrue
        if dateTrue > 1:
            raise Exception("Error: Multiple of the same date inside fRead")
        elif dateTrue == 1:
            n = n + 1
            continue # Stop loop temperarily
        fRead.close()

        ## Write to file
        # File variables
        faDates = open(datesFile, "a")
        faTodo = open(todoFile, "a")
        # Appending to files
        faDates.write(dString + "\n")
        faTodo.write("* " + dString + "\n")

        ## Add one to n
        n = n + 1
