from typing import Union, Callable, Optional, List

import tensorflow as tf
from tensorflow.keras import activations, models, layers, optimizers

ActivationFct = Union[str, Callable[[], tf.Tensor]]
Optimizer = Union[str, optimizers.Optimizer]


def create_model(n_inputs: int, n_outputs: int, n_hidden_layers: int, n_hidden_units: int,
                 activation: ActivationFct = activations.tanh, optimizer: Optimizer = "adam", loss: str = "mse",
                 metrics: Optional[List[str]] = None) -> models.Sequential:

    if metrics is None:
        metrics=["mse"]

    model = models.Sequential()

    # inputs
    model.add(layers.InputLayer(input_shape=(n_inputs)))

    # hidden layers
    for i in range(n_hidden_layers):
        model.add(layers.Dense(n_hidden_units, activation=activation))

    # outputs
    model.add(layers.Dense(n_outputs))

    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    return model
