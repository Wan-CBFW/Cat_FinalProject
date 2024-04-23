#txt.py
#***********************************************************************************************************************************************
# Names: Trevor Hunt, Nosagie Sherman, JaJuan Hill, Cian Roopnarine                                                                            *
# emails: huntt3@mail.uc.edu, shermani@mail.uc.edu, hill4ju@mail.uc.edu, roopnacn@mail.uc.edu                                                  *
# Assignment Number: Final Project                                                                                                             *
# Due Date: 04/23/2024                                                                                                                         *
# Course/Section: IS4010-001                                                                                                                   *
# Semester/Year: Spring 2024                                                                                                                   *
# Brief Description of the assignment: Collaborative assignment demonstrating working with encryption, JSON, Pillow, txt, lists and more       *
#                                                                                                                                              *
# Brief Description of what this module does: Creates function to open and read a txt file, splitting into a list of separate words            *
# Citations: Bill Nicholson                                                                                                                    *
# Anything else that's relevant:                                                                                                               *
#***********************************************************************************************************************************************
def txtToList(path):
    '''
    Reads txt file into a list of words
    @param: txt file path
    @return: list of words
    '''
    with open(path, 'r') as file:
        words = file.read().split()     #read json file, splitting each word into a list item
    return(words)