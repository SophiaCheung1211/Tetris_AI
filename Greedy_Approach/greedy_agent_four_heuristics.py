import argparse
import os
import shutil
from random import random, randint, sample

import numpy as np
import torch
import torch.nn as nn
from tensorboardX import SummaryWriter

from tetris import Tetris
from collections import deque


env = Tetris(width=10, height=20, block_size=30)

state = env.reset()

done = False

while not done:
    

    next_steps = env.get_next_states()
    next_actions, next_states = zip(*next_steps.items())
    rewards = env.calculate_reward_4h(next_states)

    index = np.argmax(rewards).item()
#    next_state = next_states[index_min]
    action = next_actions[index]

    reward, done = env.step(action, render=True)
 
    if done:
        final_score = env.score
        final_tetrominoes = env.tetrominoes
        final_cleared_lines = env.cleared_lines
        print(env.cleared_lines)
        state = env.reset()
         
    


