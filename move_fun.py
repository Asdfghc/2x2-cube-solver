import pickle


def move(amove, state):
    next_state = pickle.loads(pickle.dumps(state))
    if amove == "R":
        next_state[3][2] = state[0][1]
        next_state[3][0] = state[0][3]
        next_state[0][1] = state[1][1]
        next_state[0][3] = state[1][3]
        next_state[1][1] = state[5][1]
        next_state[1][3] = state[5][3]
        next_state[5][1] = state[3][2]
        next_state[5][3] = state[3][0]

        next_state[2][0] = state[2][2]
        next_state[2][1] = state[2][0]
        next_state[2][2] = state[2][3]
        next_state[2][3] = state[2][1]

    elif amove == "R'":
        next_state[0][1] = state[3][2]
        next_state[0][3] = state[3][0]
        next_state[1][1] = state[0][1]
        next_state[1][3] = state[0][3]
        next_state[5][1] = state[1][1]
        next_state[5][3] = state[1][3]
        next_state[3][2] = state[5][1]
        next_state[3][0] = state[5][3]

        next_state[2][0] = state[2][1]
        next_state[2][1] = state[2][3]
        next_state[2][2] = state[2][0]
        next_state[2][3] = state[2][2]

    elif amove == "L":
        next_state[0][0] = state[3][3]
        next_state[0][2] = state[3][1]
        next_state[1][0] = state[0][0]
        next_state[1][2] = state[0][2]
        next_state[5][0] = state[1][0]
        next_state[5][2] = state[1][2]
        next_state[3][3] = state[5][0]
        next_state[3][1] = state[5][2]

        next_state[4][0] = state[4][2]
        next_state[4][1] = state[4][0]
        next_state[4][2] = state[4][3]
        next_state[4][3] = state[4][1]

    elif amove == "L'":
        next_state[3][3] = state[0][0]
        next_state[3][1] = state[0][2]
        next_state[0][0] = state[1][0]
        next_state[0][2] = state[1][2]
        next_state[1][0] = state[5][0]
        next_state[1][2] = state[5][2]
        next_state[5][0] = state[3][3]
        next_state[5][2] = state[3][1]

        next_state[4][0] = state[4][1]
        next_state[4][1] = state[4][3]
        next_state[4][2] = state[4][0]
        next_state[4][3] = state[4][2]

    elif amove == "F":
        next_state[0][2] = state[4][3]
        next_state[0][3] = state[4][1]
        next_state[2][0] = state[0][2]
        next_state[2][2] = state[0][3]
        next_state[5][1] = state[2][0]
        next_state[5][0] = state[2][2]
        next_state[4][3] = state[5][1]
        next_state[4][1] = state[5][0]

        next_state[1][0] = state[1][2]
        next_state[1][1] = state[1][0]
        next_state[1][2] = state[1][3]
        next_state[1][3] = state[1][1]

    elif amove == "F'":
        next_state[4][3] = state[0][2]
        next_state[4][1] = state[0][3]
        next_state[0][2] = state[2][0]
        next_state[0][3] = state[2][2]
        next_state[2][0] = state[5][1]
        next_state[2][2] = state[5][0]
        next_state[5][1] = state[4][3]
        next_state[5][0] = state[4][1]

        next_state[1][0] = state[1][1]
        next_state[1][1] = state[1][3]
        next_state[1][2] = state[1][0]
        next_state[1][3] = state[1][2]

    elif amove == "B":
        next_state[4][2] = state[0][0]
        next_state[4][0] = state[0][1]
        next_state[0][0] = state[2][1]
        next_state[0][1] = state[2][3]
        next_state[2][1] = state[5][3]
        next_state[2][3] = state[5][2]
        next_state[5][3] = state[4][2]
        next_state[5][2] = state[4][0]

        next_state[3][0] = state[3][2]
        next_state[3][1] = state[3][0]
        next_state[3][2] = state[3][3]
        next_state[3][3] = state[3][1]

    elif amove == "B'":
        next_state[0][0] = state[4][2]
        next_state[0][1] = state[4][0]
        next_state[2][1] = state[0][0]
        next_state[2][3] = state[0][1]
        next_state[5][3] = state[2][1]
        next_state[5][2] = state[2][3]
        next_state[4][2] = state[5][3]
        next_state[4][0] = state[5][2]

        next_state[3][0] = state[3][1]
        next_state[3][1] = state[3][3]
        next_state[3][2] = state[3][0]
        next_state[3][3] = state[3][2]

    elif amove == "D":
        next_state[1][2] = state[4][2]
        next_state[1][3] = state[4][3]
        next_state[2][2] = state[1][2]
        next_state[2][3] = state[1][3]
        next_state[3][2] = state[2][2]
        next_state[3][3] = state[2][3]
        next_state[4][2] = state[3][2]
        next_state[4][3] = state[3][3]

        next_state[5][0] = state[5][2]
        next_state[5][1] = state[5][0]
        next_state[5][2] = state[5][3]
        next_state[5][3] = state[5][1]

    elif amove == "D'":
        next_state[4][2] = state[1][2]
        next_state[4][3] = state[1][3]
        next_state[1][2] = state[2][2]
        next_state[1][3] = state[2][3]
        next_state[2][2] = state[3][2]
        next_state[2][3] = state[3][3]
        next_state[3][2] = state[4][2]
        next_state[3][3] = state[4][3]

        next_state[5][0] = state[5][1]
        next_state[5][1] = state[5][3]
        next_state[5][2] = state[5][0]
        next_state[5][3] = state[5][2]

    elif amove == "U":
        next_state[4][0] = state[1][0]
        next_state[4][1] = state[1][1]
        next_state[1][0] = state[2][0]
        next_state[1][1] = state[2][1]
        next_state[2][0] = state[3][0]
        next_state[2][1] = state[3][1]
        next_state[3][0] = state[4][0]
        next_state[3][1] = state[4][1]

        next_state[0][0] = state[0][2]
        next_state[0][1] = state[0][0]
        next_state[0][2] = state[0][3]
        next_state[0][3] = state[0][1]

    elif amove == "U'":
        next_state[1][0] = state[4][0]
        next_state[1][1] = state[4][1]
        next_state[2][0] = state[1][0]
        next_state[2][1] = state[1][1]
        next_state[3][0] = state[2][0]
        next_state[3][1] = state[2][1]
        next_state[4][0] = state[3][0]
        next_state[4][1] = state[3][1]

        next_state[0][0] = state[0][1]
        next_state[0][1] = state[0][3]
        next_state[0][2] = state[0][0]
        next_state[0][3] = state[0][2]

    if amove == "Rot_R":
        next_state = [next_state[i] for i in [0, 2, 3, 4, 1, 5]]

    if amove == "Rot_D":
        next_state = [next_state[i] for i in [3, 0, 2, 5, 4, 1]]

    if amove == "Rot_U":
        next_state = [next_state[i] for i in [1, 5, 2, 0, 4, 3]]

    return next_state


# print(move("U'", move("R'", move("F", move("U", move("B", move("L'", move("B", [["y", "y", "y", "y"], ["r", "r", "r", "r"], ["g", "g", "g", "g"], ["o", "o", "o", "o"], ["b", "b", "b", "b"], ["w", "w", "w", "w"]]))))))))
# print(move("Rot_R", [["y", "y", "y", "y"], ["r", "r", "r", "r"], ["g", "g", "g", "g"], ["o", "o", "o", "o"], ["b", "b", "b", "b"], ["w", "w", "w", "w"]]))