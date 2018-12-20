from collections import OrderedDict
#import numpy as np
import random
from os import listdir
import pandas as pd
#import time



def get_filenames(path, suffix=".csv"):
    filenames = listdir(path)
    return [filename for filename in filenames if filename.endswith(suffix)]