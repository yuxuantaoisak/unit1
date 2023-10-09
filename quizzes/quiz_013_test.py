from quizzes.quiz_013 import mysteryThree
import pytest
#testing if individual functions work

def test_hello_world():
    assert mysteryThree(original_text='hello',copied_text='world')=="hellohellohellohellohello"


def test_second_case():
    assert mysteryThree(original_text='qwerty',copied_text='lol lol')=="qwertyqwertyqwertyqwertyqwertyqwertyqwerty"

def test_repeat_string_unicode():
    assert mysteryThree(original_text='😃',copied_text=5)=="Error, copied_text must be a string"

pytest.main()