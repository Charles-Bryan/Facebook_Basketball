# This function controls throwing the ball with the inputs: ball location and aiming location.

# The most essential part of this function is the realization that the variables MINIMUM_DURATION and MINIMUM_SLEEP
# must be set very low otherwise the ball will not release.
import pyautogui

# These two are required otherwise the mouse moves but there is no toss
pyautogui.MINIMUM_DURATION = 0.0001
pyautogui.MINIMUM_SLEEP = 0.0001


def throw_ball(ball_center, target_loc, top_left):
    # ball_center is intended to be the 2D coordinates for the ball's center of mass: (x, y)
    # target_loc is intended to be the 2D coordinates for our target calculated by the genetic algorithm: (x, y)
    # segments is how many segments we break apart the mouse's journey from ball_center to target_loc.

    pyautogui.moveTo(ball_center[0] + top_left[0], ball_center[1] + top_left[1])
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(target_loc[0] + top_left[0], target_loc[1] + top_left[1], duration=.01, tween=pyautogui.easeInQuad)
    pyautogui.mouseUp(button='left')



