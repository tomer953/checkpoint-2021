import math
import requests
import json
import numpy as np

# def board_to_long(board):
#     res = ''
#     for i in range(7):
#         for j in range(6,-1,-1):
#             ch = board[j][i]
#             res += '1' if (ch == 'O') else '0'
#     # print(res)
#     return int(res, 2)


def board_to_int_arr(board, is_source):
    arr = []
    initial_points = []
    for i in range(len(board[0])):
        for j in range(len(board)):
            ch = board[j][i]
            if (ch == 'O'):
                arr.append(1)
            elif ch == '.':
                # the java algorithm not contains 0 in the source, but save it as initial point instead
                if is_source:
                    arr.append(1)
                    initial_points.append(j)
                    initial_points.append(i)
                else:
                    arr.append(0)
            else:
                arr.append(2)
    print(str(arr).replace('[','{').replace(']','}') + ";")
    return initial_points


def get_initial_position(points):
    print(str(points).replace('[','{').replace(']','}') + ";")


def print_board(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

def main():
    
    req = requests.get("https://puzzword.csa-challenge.com/puzzle")
    req = req.json()
    print(req)
    while True:
        if req['message']:
            msg = req['message']
            msg = json.loads(msg)
            puzzle_id = msg["puzzle_id"]
            source_board = msg["source_board"]
            dest_board = msg["destination_board"]

            print(msg)
            print('source')
            print_board(source_board)
            print('dest')
            print_board(dest_board)

            print('\ninput for jave:')
            init_points = board_to_int_arr(source_board, True)
            board_to_int_arr(dest_board, False)
            
            # print board size
            board_size = 'board size: ' + str(len(source_board)) + " , " + str(len(source_board[0]))
            print(board_size)

            # print initial point
            get_initial_position(init_points)
            



            valid_ans = False
            while not valid_ans:
                solution = input("insert moves:\n")
                solution = json.loads(solution)
                body = { "puzzle_id": puzzle_id, "solution": solution} 
                req = requests.post('https://puzzword.csa-challenge.com/solve', json=body)
                print(req.status_code)
                if (str(req.status_code) == '200'):
                    req = req.json()
                    msg  = req['message']
                    if ('wrong' not in msg):
                        valid_ans = True
                    print(msg)
                        
                
    
    pass


main()


# [[1, 3, ">"],[2, 1, "v"],[4, 2, "<"],[2, 3, "^"],[2, 0, "v"],[1, 2, ">"],[6, 2, "<"],[6, 4, "^"],[3, 2, ">"],[6, 2, "<"],[3, 0, "v"],[3, 2, ">"],[4, 0, "v"],[2, 5, "^"],[0, 4, ">"],[0, 2, "v"],[3, 4, "<"],[0, 4, ">"],[2, 3, "v"],[5, 4, "<"],[4, 6, "^"],[3, 4, ">"],[3, 6, "^"],[2, 6, "^"],[2, 4, ">"],[5, 2, "<"],[3, 2, "v"],[5, 3, "<"],[3, 3, "v"],[5, 4, "<"],[3, 5, "^"]]

