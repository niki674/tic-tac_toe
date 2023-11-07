board = list(range(1, 10))
cells = 3
dashes = 13
spaces = 14

print('Tic-Tac toe the game for two players')
print()


def printBoard():
    for i in range(cells):
        print(' ' * spaces, end='')
        print('-' * dashes)
        print(' ' * spaces, end='')
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
    print(' ' * spaces, end='')
    print('-' * dashes)


def checkWin():
    wr = False
    winCoords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in winCoords:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            wr = board[1]
    return wr


def takeInput(pt):
    while True:
        print()
        pa = int(input(f'Where we put a {pt}? '))
        if pa in board:
            board[pa - 1] = pt
            break
        else:
            print('incorrect position')


def makeStep(c):
    if c % 2 == 0:
        pt = 'X'
    else:
        pt = 'O'

    takeInput(pt)

    print()

    return pt


def isWin(c, pt):
    iw = False
    if c > 4:
        winner = checkWin()
        if winner:
            print(f'{pt} is win!')
            iw = True
        elif c >= 9:
            print("Draw! You're amazing!")
            iw = True
    return iw


def main():
    counter = 0
    iw = False

    while not iw:
        printBoard()

        playerToken = makeStep(counter)

        counter += 1

        iw = isWin(counter, playerToken)

    printBoard()


main()

print('*Press Enter to exit*')
