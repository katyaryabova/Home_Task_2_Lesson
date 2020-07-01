options = {
    'A': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
    'I': ['***', '  * ', '  * ', '  * ', '\t***'],
    'T': ['******', ' \t * ', ' \t * ', ' \t * ', '\t *'],
    'K': ['*   *', '*  * ', '***  ', '*  * ', '*   *'],
}


def print_big(newList):
    for i in range(5):
        for j, _ in enumerate(newList):
            print(options[newList[j]][i] + "   ", end=" ")
        print()


name = "KATIA"
print_big(list(name))

