import pytest
from tokenizer import tokenize_text


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            "Don't hesitate to ask questions.",
            ["Do", "n't", "hesitate", "to", "ask", "questions", "."],
        ),
        ("Hello, world!", ["Hello", ",", "world", "!"]),
        ("", []),
        ("I can't do this.", ["I", "ca", "n't", "do", "this", "."]),
        (
            "We're going to John's house.",
            ["We", "'re", "going", "to", "John", "'s", "house", "."],
        ),
        ("She said, 'Hello!'", ["She", "said", ",", "'Hello", "!", "'"]),
    ],
)
def test_tokenizer(text, expected):
    assert tokenize_text(text) == expected
