import os  // for operating system related functionality

os.getcwd() // Get the current working directory
'/Users/mrnobody/Documents/VS code/python/01_basic'

import sys // for system-specific parameters and functions

sys.platform // Get the platform identifier
'darwin'

3 ** 4 // Exponentiation: 3 raised to the power of 4
81

3 // 4 // Floor division: quotient without the remainder
0

>>> 3 % 6 // Modulus: remainder of the division of 3 by 6
3

>>> 3 / 7 // True division: precise division result
0.42857142857142855

>>> 2 ** 1000 // 2 raised to the power of 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

>>> repr('"sid"') // Get the string representation including quotes
'\'"sid"\''

>>> repr("sid") // Get the string representation including quotes
"'sid'"

>>> print('"sid"') // Print the string with double quotes
"sid"

>>> print('sid') // Print the string without quotes
sid

>>> len("sid") // Get the length of the string "sid"
3

>>> len('"sid"') // Get the length of the string including quotes
5

import math // for mathematical functions
math.sqrt(16) // Calculate the square root of 16
4.0

import random // for generating random numbers
random.randint(1, 10) // Generate a random integer between 1 and 10 (inclusive)
7

random.random() // Generate a random float between 0.0 and 1.0
0.6394267984578837

random.choice(['apple', 'banana', 'cherry']) // Randomly select an item from the list
'cherry'

import datetime // for manipulating dates and times
datetime.datetime.now() // Get the current date and time

datetime.datetime(2024, 6, 15, 12, 34, 56, 789012) // Example output

datetime.datetime.now().year // Get the current year
2024   

datetime.datetime.now().month // Get the current month
6

datetime.datetime.now().day // Get the current day
15

2024-06-15 12:34:56.789012 // Example output of current date and time

