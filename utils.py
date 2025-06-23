import rawpy
import numpy as np

def convert_raw_to_rgb(raw_file):
    with rawpy.imread(raw_file) as raw:
        rgb = raw.postprocess()
    return rgb