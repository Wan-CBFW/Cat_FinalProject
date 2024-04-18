#*********************************************************************************************************
# Names: Trevor Hunt, [], [], []                                                    *
# emails: huntt3@mail.uc.edu, [], [], []                                 *
# Assignment Number: Final Project                                                                       *
# Due Date: 04/23/2024                                                                                   *
# Course/Section: IS4010-001                                                                             *
# Semester/Year: Spring 2024                                                                             *
# Brief Description of the assignment: []                      *
#                                                                                                        *
# Brief Description of what this module does: [] *
# Citations: https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/                    *
# Anything else that's relevant:                                                                         *
#*********************************************************************************************************    
def txtToList(path):
    '''
    Turns txt file into a list of words
    @param: txt file path
    @return: list of words
    '''
    with open(path, 'r') as file:
        lines = file.read().split()
    return(lines)