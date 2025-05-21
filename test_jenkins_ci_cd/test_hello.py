# test_jenkins_ci_cd/test_hello.py
import hello
import sys

def test_hello_world(capsys):
    # Call the function
    hello.hello_world()

    # Capture stdout
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
