import cv2
import numpy as np

def add(file, width, height, color):
    # Loads the picture
    #file = cv2.imread("./Emojis/smirk.png", -1)

    # Create the mask for emoji
    orig_mask = file[:,:,3]

    # Create the inverted mask for the emoji
    orig_mask_inv = cv2.bitwise_not(orig_mask)

    # Convert emoji to BGR
    # and save the original emoji size
    file = file[:,:,0:3]
      
    # Resizes the emoji, mask, and mask_inv according to the face
    file = cv2.resize(file, (width,height), interpolation = cv2.INTER_AREA)
    mask = cv2.resize(orig_mask, (width,height), interpolation = cv2.INTER_AREA)
    mask_inv = cv2.resize(orig_mask_inv, (width,height), interpolation = cv2.INTER_AREA)

    # Sets the region of interest of the face
    roi = color[0:width, 0:height]

    # Creates the background (face) and foreground (emoji)
    roi_bg = cv2.bitwise_and(roi,roi, mask = mask_inv)
    roi_fg = cv2.bitwise_and(file,file, mask = mask)

    # Overlays emoji to face
    dst = cv2.add(roi_bg,roi_fg)

    # Sets the layer back to the region of interest
    color[0:height, 0:width] = dst
    
    return color[0:height, 0:width]