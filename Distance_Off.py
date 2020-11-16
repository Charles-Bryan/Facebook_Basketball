# The purpose of this function is to determine the horizontal distance the ball is off from the hoop itself if it misses
# The inputs needed will be the ball mask and the hoop mask.
from scipy.ndimage import measurements
import time
import numpy as np
from Update_Image import  update_both_masks, update_ball_mask, update_hoop_mask#,update_coms
import original_measurements as om

def Fitness_Distance(top_left, bottom_right, hoop_width):
    ball_mask = update_ball_mask(top_left, bottom_right)
    ball_height = om.middle_vertical(ball_mask)  # Just the vertical pixel

    # No fail safe currently built in in case something is missed
    while True:
        previous_ball_height = ball_height
        ball_mask = update_ball_mask(top_left, bottom_right)
        ball_height = om.middle_vertical(ball_mask)  # Just the vertical pixel

        if ball_height > previous_ball_height:    # inverted cause screen pixels start (0,0) top left
            break
        # Now the ball is falling

    # No fail safe currently built in in case something is missed
    while True:
        joint_masks = update_both_masks(top_left, bottom_right)
        ball_height = om.middle_vertical(joint_masks["ball"])  # Just the vertical pixel
        hoop_height = om.middle_vertical(joint_masks["hoop"])  # Just the vertical pixel

        if ball_height > hoop_height:
            break

    # Total width of game is roughly 5.2 hoop widths.
    max_distance = 6*hoop_width

    # Small issue is if the ball hits the rim then it would be complicated to count that as close if it bounces far away
    # Would require some two step method where we check the bottom of the ball or we check to see if it
    # goes up, down, up or something like that.... actually that wouldn't be too bad. Too lazy though

    ball_hor = om.middle_hor(joint_masks["ball"])  # Just the horizontal pixel
    hoop_hor = om.middle_hor(joint_masks["hoop"])  # Just the horizontal pixel
    distance_away = abs(ball_hor - hoop_hor)

    if distance_away < hoop_width/2:
        return 1.0  # A success
    else:
        return 1.0-distance_away/max_distance

