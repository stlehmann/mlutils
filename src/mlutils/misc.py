import random

# try to import numpy
try:
    import numpy as np
except ModuleNotFoundError:
    np = None

# try to import tensorflow
try:
    import tensorflow as tf
except ModuleNotFoundError:
    tf = None


def seed(x: int) -> None:
    """Set the random seed for installed machine learning packages."""
    random.seed(x)

    if np is not None:
        np.random.seed(x)

    if tf is not None:
        tf.random.set_seed(x)
