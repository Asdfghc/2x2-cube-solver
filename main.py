import move_fun
from itertools import groupby
from util import Node, QueueFrontier
import threading
import time

start_time = time.time()


moves = ["R", "R'", "F", "F'", "U", "U'"]

invalid_moves = {"R": "R'", "R'": "R", "F": "F'", "F'": "F", "U": "U'", "U'": "U"}

explored1 = []
explored2 = []


ida = []
volta = []


def main(scramble):
    start = Node(state=scramble, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)
    explored1.append(start)

    while True:
        global stop_threads
        if stop_threads:
            break

        node = frontier.remove()
        for x in explored2:
            if x.state == node.state:
                path = []
                while node.parent is not None:
                    path.append(node.action)
                    node = node.parent
                path.reverse()
                print("ida: " + str(path))
                ida.append(path)

                path2 = []
                while x.parent is not None:
                    path2.append(x.action)
                    x = x.parent
                print("volta: " + str(path2))
                volta.append(path2)

                stop_threads = True
                return


        for action, state in possible_next_positions(node.state, node.action):
            if not any(x for x in explored1 if x.state == state):
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)
                explored1.append(child)


def reverse(solved_state):
    start = Node(state=solved_state, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)
    explored2.append(start)

    while True:
        global stop_threads
        if stop_threads:
            break

        node = frontier.remove()
        for x in explored1:
            if x.state == node.state:
                path = []
                while node.parent is not None:
                    path.append(node.action)
                    node = node.parent
                print("volta: " + str(path))
                volta.append(path)

                path2 = []
                while x.parent is not None:
                    path2.append(x.action)
                    x = x.parent
                path2.reverse()
                print("ida: " + str(path2))
                ida.append(path2)

                stop_threads = True
                return


        for action, state in possible_next_positions(node.state, node.action):
            if not any(x for x in explored2 if x.state == state):
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)
                explored2.append(child)


def possible_next_positions(state, last_move):
    next_moves = [(move, move_fun.move(move, state)) for move in moves if move not in invalid_moves.get(last_move, [])]
    return next_moves


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def trator(scramble):
    solved = [["y", "y", "y", "y"], ["r", "r", "r", "r"], ["g", "g", "g", "g"], ["o", "o", "o", "o"], ["b", "b", "b", "b"], ["w", "w", "w", "w"]]
    if solved[4][2] == scramble[4][2] and solved[5][2] == scramble[5][2]:
        return solved
    for _ in range(3):
        for i in range(3):
            solved = move_fun.move("Rot_R", solved)
            if solved[4][2] == scramble[4][2] and solved[5][2] == scramble[5][2]:
                return solved
        solved = move_fun.move("Rot_D", solved)
        if solved[4][2] == scramble[4][2] and solved[5][2] == scramble[5][2]:
            return solved
    solved = move_fun.move("Rot_U", solved)
    solved = move_fun.move("Rot_U", solved)
    if solved[4][2] == scramble[4][2] and solved[5][2] == scramble[5][2]:
        return solved
    for i in range(3):
        solved = move_fun.move("Rot_R", solved)
        if solved[4][2] == scramble[4][2] and solved[5][2] == scramble[5][2]:
            return solved
    for _ in range(2):
        solved = move_fun.move("Rot_U", solved)
        if solved[4][2] == scramble[4][2] and solved[5][2] == scramble[5][2]:
            return solved
        for i in range(3):
            solved = move_fun.move("Rot_L", solved)
            if solved[4][2] == scramble[4][2] and solved[5][2] == scramble[5][2]:
                return solved


if __name__ == '__main__':
    scramble = [['b', 'g', 'g', 'r'], ['y', 'g', 'b', 'y'], ['y', 'r', 'r', 'w'], ['w', 'y', 'b', 'o'], ['o', 'o', 'w', 'o'], ['w', 'b', 'g', 'r']]
    # print(trator(scramble))

    t1 = threading.Thread(target=main, args=(scramble, ))
    t2 = threading.Thread(target=reverse, args=(trator(scramble), ))

    stop_threads = False
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    volta = volta[0]
    count = 0
    for move in volta:
        if len(move) == 2:
            volta[count] = move[0]
        else:
            volta[count] = move[0] + "'"
        count += 1
    for mov in [ida[0] + volta][0]:
        print(mov, end="  ")
    print("\n" + ("--- %s seconds ---" % round(time.time() - start_time, 3)))
