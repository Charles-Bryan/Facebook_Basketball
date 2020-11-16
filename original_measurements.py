import numpy as np
import math

def height(image_array):
    if np.max(image_array) == 0:
        return np.nan
    else:
        low = np.max(np.where(image_array == 255)[0][:])   # Low in terms of visually. Pixel value is higher
        high = np.min(np.where(image_array == 255)[0][:])   # High in terms of visually. Pixel value is lower
        return low-high

def middle_vertical(image_array):
    if np.max(image_array) == 0:
        return np.nan
    else:
        low = np.max(np.where(image_array == 255)[0][:])  # Low in terms of visually. Pixel value is higher
        high = np.min(np.where(image_array == 255)[0][:])  # High in terms of visually. Pixel value is lower
        return high + math.floor((low - high)/2)

def low_vertical(image_array):
    if np.max(image_array) == 0:
        return np.nan
    else:
        return np.max(np.where(image_array == 255)[0][:])   # Low in terms of visually. Pixel value is higher

def high_vertical(image_array):
    if np.max(image_array) == 0:
        return np.nan
    else:
        return np.min(np.where(image_array == 255)[0][:])   # High in terms of visually. Pixel value is lower

# //////////////Horizontal things/////////////////////////

def middle_hor(image_array):
    if np.max(image_array) == 0:
        return np.nan
    else:
        left = np.min(np.where(image_array == 255)[1][:])
        right = np.max(np.where(image_array == 255)[1][:])
        return left + math.floor((right - left)/2)

def left_hor(image_array):
    if np.max(image_array) == 0:
        return np.nan
    else:
        return np.min(np.where(image_array == 255)[1][:])

def right_hor(image_array):
    if np.max(image_array) == 0:
        return np.nan
    else:
        return np.max(np.where(image_array == 255)[1][:])

def width(image_array):
    if np.max(image_array) == 0:
        return np.nan
    else:
        left = np.min(np.where(image_array == 255)[1][:])
        right = np.max(np.where(image_array == 255)[1][:])
        return right - left

# /////////////COM///////////

def orig_com(image_array):
    if np.max(image_array) == 0:
        return [np.nan, np.nan]
    else:
        com = [0, 0]  # (x, y)

        left = np.min(np.where(image_array == 255)[1][:])
        right = np.max(np.where(image_array == 255)[1][:])
        com[0] = left + math.floor((right - left)/2)

        low = np.max(np.where(image_array == 255)[0][:])  # Low in terms of visually. Pixel value is higher
        high = np.min(np.where(image_array == 255)[0][:])  # High in terms of visually. Pixel value is lower
        com[1] = high + math.floor((low - high)/2)

        return com
