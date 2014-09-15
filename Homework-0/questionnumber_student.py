#This is an example of a solution to a homework problem in python
#at the top of the script will be the author and any contributors


# 1. restate the problem (cut/paste) in comments

'''Create a grid of x values for plotting x = [-10: .1 : 20]'''

# 2. post solution

import numpy as np
x = np.arange(-10, 20.1, .1)

# 3. write pseudocode/plain english explanation

'''
import the numpy library in order to use the arange array object
variable = np.arange(beginning, ending-not inclusive, increment amount)
'''

'''
Additional notes: the script should be able to run as is.  If the script is downloaded, it should run correctly with no modification from the user. 
'''
