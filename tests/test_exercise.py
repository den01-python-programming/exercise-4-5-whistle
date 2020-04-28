import pytest
from src import whistle

def test_exercise(capsys):
    fox_whistle = whistle.Whistle("RingDing")
    print(fox_whistle.sound)

    out, err = capsys.readouterr()
    assert out == "RingDing\n"
