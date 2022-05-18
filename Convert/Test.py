import pytest
from Convert import Convert

@pytest.mark.parametrize(
    "input_a,expect",
    [
    (3,"III"),
    (5,"V")
    ]
)
def test_Todos(input_a, expected):
    assert Convert(input_a) == expected
