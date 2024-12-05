from scipy import signal
import numpy as np

from images.constants import IMAGE_SIZE


def resize_image(data: list[int]) -> list[int]:
    return signal.resample(data, IMAGE_SIZE).astype(np.uint8).tolist()


def apply_color_map(data: list[int]) -> list[int]:
    return data
