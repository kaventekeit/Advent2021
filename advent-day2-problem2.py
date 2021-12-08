def getFinalPos(puzzle_input):

    myPuzzleInput = open(puzzle_input,"r")

    plannedMoves = myPuzzleInput.readlines()

    forwardPosition = 0
    depth = 0
    aim = 0

    for i in range(len(plannedMoves)):

        if plannedMoves[i][0] == 'f':

            forwardPosition += int(plannedMoves[i][8:])
            depth += aim*int(plannedMoves[i][8:])

        elif plannedMoves[i][0] == 'd':

            aim += int(plannedMoves[i][5:])

        elif plannedMoves[i][0] == 'u':

            aim -= int(plannedMoves[i][3:])

    print(
            f"My horizontal position is now {forwardPosition}. "
            + f"My depth is now {depth}. "
            + f"My aim is now {aim}."
            )

    ans = forwardPosition*depth

    print(
            f"My final horizontal position "
            + f"multiplied by my final depth is now "
            + f"{ans}."
    )

getFinalPos("advent2input.txt")
