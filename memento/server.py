import flag, shortest_path
import random, json, base64

def verify_game(board, level):
    card_number = random.randint(1, 20)
    board_obj = base64.b64decode(json.loads(board))
    indexes = []
    for i in range(5):
        for j in range(8):
            if board_obj[i][j] == card_number:
                indexes.append([i, j])
    
    shortest = shortest_path(indexes[0], indexes[1], board, "UP|DOWN|LEFT|RIGHT")
    shortest = shortest.length - 1
    result = 0
    if shortest == (flag[level] % 9) + 1:
        result = 1
    return result

    # path can be from 1 step to 11
    # flag[0] == 9 % 9 = 1 [9,18,27,]
    # flag[0] == 10 % 9 = 2 [10,19,28]
    # flag[0] == 11 % 9 = 3
    # flag[0] == 12 % 9 = 4
    # flag[0] == 13 % 9 = 5
    # flag[0] == 14 % 9 = 6
    # flag[0] == 15 % 9 = 7
    # flag[0] == 16 % 9 = 8
    # flag[0] == 17 % 9 = 9
    # flag[0] == 18 % 9 = 1

    # ascii lowercase a-z 97(a)-122(z)