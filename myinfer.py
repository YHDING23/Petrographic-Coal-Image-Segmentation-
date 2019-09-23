import sys
sys.path.append('../../../../utils/')
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import tensorflow as tf
import get_dataset_colormap

LABEL_NAMES = np.asarray([
    '_inm_','q','qtz','ignore'])

FULL_LABEL_MAP = np.arange(len(LABEL_NAMES)).reshape(len(LABEL_NAMES), 1)
FULL_COLOR_MAP = get_dataset_colormap.label_to_color_image(FULL_LABEL_MAP)

class DeepLabModel(object):
    """Class to load deeplab model and run inference."""
    INPUT_TENSOR_NAME = 'ImageTensor:0'
    OUTPUT_TENSOR_NAME = 'SemanticPredictions:0'
    INPUT_SIZE = 513
