import pytest
from MyModel import MyModel


@pytest.fixture
def init_model():
    return MyModel()


def test_predict(init_model):
    assert init_model.predict([[1, 2, 3]], ['col1']) == [[1, 2, 3]]


def test_send_feedback(init_model):
    assert init_model.send_feedback(
        [[1, 2, 3]], ['col1'], 0.0, [[1, 2, 3]]) == []
