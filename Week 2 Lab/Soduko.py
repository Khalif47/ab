# Create a list of values


def row():
    Row = [0]
    Row = Row * 9
    return Row

# Basic backtracking algorithm


def backtrack(Current):
    Possible = PossibleSolution(Current)
    if Possible =[]:
        return Current
    else:
        for item in Possible:
            Current.append(Possible)
            backtrack(Current)
            Possible.pop()


#