#image.py
#****************************************************************************************************************************************
# Names: Trevor Hunt, Nosagie Sherman, JaJuan Hill, Cian Roopnarine                                                                     *
# emails: huntt3@mail.uc.edu, shermani@mail.uc.edu, hill4ju@mail.uc.edu, roopnacn@mail.uc.edu                                           *
# Assignment Number: Final Project                                                                                                      *
# Due Date: 04/23/2024                                                                                                                  *
# Course/Section: IS4010-001                                                                                                            *
# Semester/Year: Spring 2024                                                                                                            *
# Brief Description of the assignment: Collaborative assignment demonstrating working with encryption, JSON, Pillow, txt, lists and more*
#                                                                                                                                       *
# Brief Description of what this module does: Defines function to open and load images with pillow                                      *
# Citations: Bill Nicholson                                                                                                             *
# Anything else that's relevant:                                                                                                        *
#****************************************************************************************************************************************
from PIL import Image

def loadImage( filename ) :
    '''
    Load an image file from disk
    @param: filename The file to load
    @return: the image object
    '''
    myimage = Image.open(filename)
    myimage.load()
    return myimage