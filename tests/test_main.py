import pytest


from rotate.rotate import rotate


class TestRotate:
    def test_rotate_plus_1(self):
        assert rotate("Hello", 1) == "Ifmmp"

    def test_rotate_plus_27(self):
        assert rotate("Hello", 27) == "Ifmmp"

    def test_rotate_minus_1(self):
        assert rotate("Hello", -1) == "Gdkkn"

    def test_rotate_minus_27(self):
        assert rotate("Hello", -27) == "Gdkkn"

    def test_non_alphabetical_text(self):
        with pytest.raises(ValueError):
            rotate("?", 1)
