from PIL import Image
import PIL
import os
import glob


def resize(image_name):
    """Resizes the image in base dir.
    Parameters: image_name
    Returns: new_name, Null(Overrides the resized image)
    """
    im = Image.open(image_name)

    #Display actual image
    # im.show()

    #Make the new image half the width and half the height of the original image
    resized_im = im.resize((384, 384))

    #Display the resized imaged
    # resized_im.show()

    #Save the cropped image
    resized_im.save(image_name)