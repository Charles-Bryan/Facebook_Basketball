# This function will take an updated image of the screen and return the updated ball_com and hoop_com in the form of
# a dictionary.
import cv2 as cv
from PIL import ImageGrab
import numpy as np


def update_both_masks(topleft, bottomright):
    lower_red_hsv_threshold = np.array([116, 239, 254])
    upper_red_hsv_threshold = np.array([117, 240, 255])
    lower_ball_hsv_threshold = np.array([105, 208, 231])
    upper_ball_hsv_threshold = np.array([108, 255, 255])

    input_img = ImageGrab.grab(bbox=(topleft[0], topleft[1], bottomright[0], bottomright[1]))  # x, y, w, h
    input_img = np.array(input_img)
    hsv_img = cv.cvtColor(input_img, cv.COLOR_BGR2HSV)

    mask_hoop = cv.inRange(hsv_img, lower_red_hsv_threshold, upper_red_hsv_threshold)
    mask_ball = cv.inRange(hsv_img, lower_ball_hsv_threshold, upper_ball_hsv_threshold)

    masks = {
        "ball": mask_ball,
        "hoop": mask_hoop
    }

    return masks


def update_ball_mask(topleft, bottomright):
    lower_ball_hsv_threshold = np.array([105, 208, 231])
    upper_ball_hsv_threshold = np.array([108, 255, 255])

    input_img = ImageGrab.grab(bbox=(topleft[0], topleft[1], bottomright[0], bottomright[1]))  # x, y, w, h
    input_img = np.array(input_img)
    hsv_img = cv.cvtColor(input_img, cv.COLOR_BGR2HSV)

    return cv.inRange(hsv_img, lower_ball_hsv_threshold, upper_ball_hsv_threshold)


def update_hoop_mask(topleft, bottomright):
    lower_red_hsv_threshold = np.array([116, 239, 254])
    upper_red_hsv_threshold = np.array([117, 240, 255])

    input_img = ImageGrab.grab(bbox=(topleft[0], topleft[1], bottomright[0], bottomright[1]))  # x, y, w, h
    input_img = np.array(input_img)
    hsv_img = cv.cvtColor(input_img, cv.COLOR_BGR2HSV)

    return cv.inRange(hsv_img, lower_red_hsv_threshold, upper_red_hsv_threshold)
