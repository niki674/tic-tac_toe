board = list(range(9))
cells = 3
dashes = 13
spaces = 14
counter = 0
winCoords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
isWin = False

print('Tic-Tac toe the game for two players')
print()

while not isWin:
    for i in range(cells):
        print(' ' * spaces, end='')
        print('-' * dashes)
        print(' ' * spaces, end='')
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
    print(' ' * spaces, end='')
    print('-' * dashes)

    if counter % 2 == 0:
        pkayerToken = 'X'
    else:
        pkayerToken = 'O'

    print()

    playerAnswer = int(input(f'Where we put a {pkayerToken}? '))

    if playerAnswer in board:
        board[playerAnswer] = pkayerToken
    else:
        print('incorrect position')
        continue

    counter += 1

    if counter > 4:
        for i in winCoords:
            if board[i[0]] == board[i[1]] == board[i[2]]:
                isWin = True
                break
        if isWin:
            print(pkayerToken, 'is win!')
            break

    if counter >= 9:
        print("Draw! You're amazing!")


for i in range(cells):
    print(' ' * spaces, end='')
    print('-' * dashes)
    print(' ' * spaces, end='')
    print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
print(' ' * spaces, end='')
print('-' * dashes)

print('*Press Enter to exit*')