import pytest
import unittest.mock as mock
from mlutils.misc import seed


random_mock = mock.MagicMock()


def test_seed() -> None:
    with mock.patch.dict("sys.modules", random=random_mock):
        breakpoint()
        seed(42)
        pass
