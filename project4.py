from os import path
from random import randrange
from GameAPI import GameAPI
import numpy as np
import pprint
import time


GameAPI = GameAPI()
teamId = 1269
worldId = 0
startWorld = 4
endWorld = 10
dimension = 40
alpha = 0.9


def load_gridWorld(worldId):
    gridWorld = np.load('world' + str(worldId) + '.npy')
    return gridWorld

def load_qVals(worldId):
    qVals = np.load('world' + str(worldId) + 'qVals.npy', allow_pickle=True)
    return qVals

def before_exit(worldId, gridWorld, qValues):
    np.save('world' + str(worldId), gridWorld)
    np.save('world' + str(worldId) + 'qVals', qValues)

def init_q_values(dimension):
    qValues = []
    for i in range(dimension):
        for j in range(dimension):
            tempDict = {'U':0, 'D':0, 'R':0, 'L':0, 'i':i, 'j':j}
            qValues.append(tempDict)
    return qValues

def get_action(x, y, qValue):
    actions = ['U', 'D', 'R', 'L']
    if(x == 0):
        actions.remove('L')
    if (x == dimension - 1):
        actions.remove('R')
    if (y == 0):
        actions.remove('D')
    if (y == dimension - 1):
        actions.remove('U')



    return actions[randrange(0, len(actions), 1)]

def Q_learning(gridWorld, qValues):
    X = 0
    Y = 0

    # Update location and worldId
    location = GameAPI.locate_me(teamId)
    worldId = int(location['world'])
    state = location['state'].split(':')
    X = int(state[0])
    Y = int(state[1])

    while True:
        # for act in actions:
        act = get_action(X, Y, qValues[(X+1)*(Y+1)-1])

        move_res = GameAPI.make_move(teamId, worldId, act)
        reward = move_res['reward']
        scoreIncrement = move_res['scoreIncrement']
        newState = move_res['newState']

        # If reached the end, save the values and return
        if(newState == 'null' or newState == None):
            before_exit(worldId, gridWorld, qValues)
            print('terminal state:', X, Y, act)
            return
        else:
            newX = int(newState['x'])
            newY = int(newState['y'])
            qValues[(X+1)*(Y+1)-1][act] = (1 - alpha) * qValues[(X+1)*(Y+1)-1][act] + alpha * (reward + scoreIncrement)

        # Update location
        X = newX
        Y = newY

qValues = []
gridWorld = []

for i in range(startWorld, endWorld+1):
    worldId = i

    for j in range(0, 5):
        print('world: ', worldId, 'time: ', j)
        GameAPI.enter_world(teamId, worldId)
        # If files exist, load them, if not initialize the world
        if(path.exists('world' + str(worldId) + '.npy')):
            qValues = load_qVals(worldId)
            gridWorld = load_gridWorld(worldId)
        else:
            qValues = init_q_values(dimension)
            np.zeros((dimension,dimension), dtype=float)

        Q_learning(gridWorld, qValues)

    before_exit(worldId, gridWorld, qValues)