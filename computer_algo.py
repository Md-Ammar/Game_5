import random

w, h = 700, 700

win_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]

corners = [0, 2, 6, 8]
adjacents = [1, 3, 5, 7]

def computer(grid_value):
    for win in win_list:
        trio = [grid_value[i] for i in win]
        if trio.count("circle") == 2 and trio.count("") == 1:
            emp_pos = trio.index("")
            return win[emp_pos]

    for win in win_list:
        trio = [grid_value[i] for i in win]
        if trio.count("cross") == 2 and trio.count("") == 1:
            emp_pos = trio.index("")
            return win[emp_pos]

    # adj = list(i for i in range(9) if grid_value[i] == "circle" and i in adjacents)
    # if len(adj) > 1:
    #     adjacent_trick(grid_value, adj)

    # corner = list(i for i in range(9) if grid_value[i] == "cross" and i in corners)
    # if len(corner) > 1:
    #     corner_defense(grid_value, corner)


    vacants = list(i for i in range(9) if grid_value[i] == "")
    rand = vacants[random.randrange(len(vacants))]
    return rand

# def adjacent_trick(grid_value, adj):
#     if grid_value[4] == "":
#         opp_adj = list(i for i in range(9) if grid_value[i] == "cross" and i in adjacents)
#         if len(opp_adj) <= 1:
#             pass

def corner_defense(grid_value, cross):
    pass