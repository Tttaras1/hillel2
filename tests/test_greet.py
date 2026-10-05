from main import greet


def test_greet_includes_the_name():
    assert greet("Taras") == "Hello, Taras!"
