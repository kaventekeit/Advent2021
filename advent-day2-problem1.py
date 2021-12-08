def getFinalPos(puzzle_input):

    myPuzzleInput = open(puzzle_input,"r")

    plannedMoves = myPuzzleInput.readlines()

    forwardPosition = 0
    depth = 0

    for i in range(len(plannedMoves)):

        if plannedMoves[i][0] == 'f':

            forwardPosition += int(plannedMoves[i][8:])

        elif plannedMoves[i][0] == 'd':

            depth += int(plannedMoves[i][5:])

        elif plannedMoves[i][0] == 'u':

            depth -= int(plannedMoves[i][3:])

    print(f"My horizontal position is {forwardPosition} "\
            + f"and my depth is {depth}.")

    ans = forwardPosition*depth

    print(f"Multiplied together this gives {ans}.")

getFinalPos("advent2input.txt")
