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

    def test_rotate_0(self):
        assert rotate("Hello", 0) == "Hello"

    def test_rotate_26(self):
        assert rotate("Hello", 26) == "Hello"

    def test_lowercase_text(self):
        assert rotate("hello", 1) == "ifmmp"

    def test_uppercase_text(self):
        assert rotate("HELLO", 1) == "IFMMP"

    def test_text_with_non_alphabetical_character(self):
        assert rotate("Hello, World!", 1) == "Ifmmp, Xpsme!"

    def test_text_with_non_ascii_character(self):
        assert rotate("Helloはこんにちは", 1) == "Ifmmpはこんにちは"

    def test_empty_text(self):
        assert rotate("", 1) == ""
