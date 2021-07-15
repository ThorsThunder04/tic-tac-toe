"""
Game written by Thor.N from scratch.
Project started on 16/07/2021 at 00:07.
"""
import os



clear = lambda: os.system('cls')

pause = lambda: input('\nPress enter to continue...')

"""
design:
a:  X | O | X
   -----------
b:    |   |  
   -----------
c:  O |   |

    1   2  3
"""
pause()



def main():
    currentBoard = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]


