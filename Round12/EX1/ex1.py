import math
import numpy as np

names = {'pow': math.pow, 'pi': math.pi, 'e': math.e}

print(eval(input("Write: "), names))
