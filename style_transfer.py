from skimage.exposure import match_histograms
import numpy as np

def apply_histogram_match(source_img, reference_img):
    matched = match_histograms(source_img, reference_img, channel_axis=-1)
    return np.uint8(matched)