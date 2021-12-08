def findIncreases(text_file):

    increaseCount = 0

    myPuzzleInput = open(text_file,"r")

    myNumbers = myPuzzleInput.readlines()

    for i in range(len(myNumbers)):

        myNumbers[i] = int(myNumbers[i])

    for i in range (1, len(myNumbers)):

        if myNumbers[i]>myNumbers[i-1]:

            increaseCount += 1

    print(f"{increaseCount} measurements were larger than previous measurements.")

findIncreases("advent1input.txt")
