# import flag, shortest_path
import random
import json
import base64


def verify_game(board, level):
    #card_number = random.randint(1, 20)
    for card_number in range(1, 21):
        print(card_number)
        board_obj = json.loads(base64.b64decode(board))
        #print(board_obj)
        indexes = []
        for i in range(5):
            for j in range(8):
                if board_obj[i][j] == card_number:
                    indexes.append([i, j])

        print(indexes)

    # shortest = shortest_path(indexes[0], indexes[1], board, "UP|DOWN|LEFT|RIGHT")
    # shortest = shortest.length - 1
    # result = 0
    # if shortest == (flag[level] % 9) + 1:
    #     result = 1
    # return result


verify_game("W1s1LDIsNCw1LDE0LDExLDksM10sWzE4LDgsNywxNiwxOSwxNyw5LDEzXSxbMTIsMTMsMSwxNSwxMiwxMSwyMCwxNl0sWzE0LDgsMTksNiw0LDE4LDE3LDE1XSxbMSwyMCwxMCwxMCw2LDcsMiwzXV0=", 0)
