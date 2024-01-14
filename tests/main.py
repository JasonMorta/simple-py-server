#Import a function from a file in the same directory
import normal_function

# Import a function from a file in a subdirectory
from innerFIles import inner_function

good = normal_function.getPrint()

inner = inner_function.my_inner_function()