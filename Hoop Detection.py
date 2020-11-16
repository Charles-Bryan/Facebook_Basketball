import cv2 as cv
import numpy as np
import pyautogui
import time
import random
import math
import pickle

from BallThrowing import throw_ball
from Distance_Off import Fitness_Distance
from Update_Image import update_both_masks, update_ball_mask, update_hoop_mask
import original_measurements as om
import statistics

import LoadSave as ls
import DarwinTasks as DT
import GNN as gn

pyautogui.FAILSAFE = True  # This is True by default but I want to stress it's importance

# region 1: Selecting the game screen
print("Put the mouse cursor in the top left corner of the game's screen. You have 3 seconds")
time.sleep(3)
point1 = pyautogui.position()

print("Put the mouse cursor in the bottom right corner of the game's screen. You have 3 seconds")
time.sleep(3)
point2 = pyautogui.position()

deltax = point2[0] - point1[0]
deltay = point2[1] - point1[1]
# endregion

# Setting Genetic Algorithm Parameters
family = ls.createFamily(2, 3, 10, 6)  # (number of survivors during trimming, layerQty, layerSize, weightQty)
num_generations = 500  # Might change to a fitness score based approach or infinite

with open(r"20190514-084205", "rb") as input_file:
    family = pickle.load(input_file)
# "update_both_masks" updates the screen shots used to detect the ball and hoop
joint_masks = update_both_masks(point1, point2)
hoop_width = om.width(joint_masks["hoop"])              # determine the red portion of the hoop's width
ball_height = om.middle_vertical(joint_masks["ball"])   # determine the ball's vertical position

fit_scale = 1.4     # Used for scaling the distance metric. 1.4 was chosen based on gameplay
hoop_mask = update_hoop_mask(point1, point2)
hoop_com = om.orig_com(hoop_mask)
gamecenter = hoop_com[0]
# print("Game center is: ", gamecenter)

for gen in range(num_generations):  # Repeat overall loop for as many generations as hard-coded previously
    for index, kid in enumerate(family):    # Repeat for each kid in the family of the genetic algorithm.

        # print("Generation Number: ", gen+1)
        # print("Child Number: ", index+1)

        t_end = 0
        total_score = 0
        keep_shooting = 1

        while keep_shooting:    # keep shooting is only set to 0 when a shot misses

            joint_masks = update_both_masks(point1, point2)
            hoop_com = om.orig_com(joint_masks["hoop"])  # (x, y)
            ball_com = om.orig_com(joint_masks["ball"])  # (x, y)

            if time.time() > t_end:
                if ball_com[1] == ball_height:  # Ball on screen

                    # Loop to throw the ball.
                    # Occasionally the ball will not throw due to Facebook not registering the input,
                    # so the while loop is for making sure the ball actually moves.
                    while True:
                        inputs = []
                        hoop_com1 = []
                        hoop_com2 = []

                        time.sleep(0.25)  # Give time for the ball to become tangible
                        ball_mask = update_ball_mask(point1, point2)
                        ball_com = om.orig_com(ball_mask)  # (x, y)

                        # ball_left True if ball is left of game center. Otherwise False
                        ball_left = True if ball_com[0] < gamecenter else False

                        # At this point the ball has reset from the previous shot and is tangible.
                        # We wait until the hoop crosses over the ball's position before preparing the shot.
                        while True:
                            hoop_mask = update_hoop_mask(point1, point2)

                            hoop_com1 = om.orig_com(hoop_mask)  # (x, y)

                            if math.floor(0.995*ball_com[0]) <= hoop_com1[0] <= math.ceil(1.005*ball_com[0]):
                                time.sleep(0.15)

                                hoop_mask = update_hoop_mask(point1, point2)
                                hoop_com2 = om.orig_com(hoop_mask)  # (x, y)

                                # hoop_left True if hoop is moving left. Otherwise False
                                hoop_left = True if hoop_com1[0] > hoop_com2[0] else False

                                if ball_left and not hoop_left:
                                    break
                                elif not ball_left and hoop_left:
                                    break

                            if total_score < 10:  # The hoop doesn't move if the score is less than 10
                                hoop_com2 = hoop_com1
                                break

                        # Store the following as inputs for the genetic algorithm
                        inputs.append(hoop_com1[0]/deltax)
                        inputs.append(hoop_com1[1]/deltay)
                        inputs.append(hoop_com2[0]/deltax)
                        inputs.append(hoop_com2[1]/deltay)
                        inputs.append(ball_com[0]/deltax)
                        inputs.append(0)

                        # Target value will be the output of our genetic algorithm.
                        target = []
                        target.append(gn.solve(kid, inputs) * deltax)   # Target's x value by gen.alg. and scaled
                        target.append(hoop_com2[1])                     # Target's y value. Locked as hoop's recent y

                        # Function to actually throw the ball based on target's pixel values
                        throw_ball(ball_center=ball_com, target_loc=target, top_left=point1)

                        ball_mask = update_ball_mask(point1, point2)
                        new_ball_com = om.orig_com(ball_mask)  # (x, y)

                        if new_ball_com[1] != ball_com[1]:  # True when ball is properly thrown
                            break
                        else:
                            time.sleep(0.1)  # Problem throwing ball and process must be repeated to avoid loc. error

                    fitness = Fitness_Distance(top_left=point1, bottom_right=point2, hoop_width=hoop_width)

                    fitness_scaled = 10**(fit_scale*(fitness-1))  # equivalent to (10^1.4*x)/(10^1.4)
                    total_score = total_score + fitness_scaled
                    t_end = time.time() + 0.8

                    if fitness_scaled != 1.0:
                        # print(str(gen) + "_" + str(index) + " score: " + str(total_score))
                        kid.score = total_score
                        keep_shooting = 0
                else:
                    time.sleep(0.5)     # Let the ball rest and become tangible

            k = cv.waitKey(5) & 0xFF
            if k == 27:
                break

    # region Statistics per Generation

    # Retrieve scores of each child
    scores = []
    for element in family:
        scores.append(element.score)

    scores_top = max(scores)                    # Calculate Top Score
    scores_mean = statistics.mean(scores)       # Calculate Mean
    scores_std_dev = statistics.pstdev(scores)  # Calculate Population Std. Dev.

    # Printout statistics for each Generation: Top Score, Scores Std Deviation, Scores Mean
    print("Gen", gen, ": Top_Score:", scores_top, "Mean:", scores_mean, "Std_Dev:", scores_std_dev)
    # endregion

    timestr = time.strftime("%Y%m%d-%H%M%S")
    ls.saveFamily(family, timestr)        # Commented out temporarily due to Memory Crashes
    family = DT.nextEpoch(family)
    # print(family[0].network)
