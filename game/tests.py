# Unit tests for Game: Rock, Paper, Scissors
#Write unit tests with pytest

# Author: Fan Zhang

import rps
import warnings
import pytest

##test cases for rps_compare
def test_rps_compare_rock_and_rock():
    assert rps.rps_compare(rps.rpsList.index("r"),0) == 0

def test_rps_compare_rock_and_paper():
    assert rps.rps_compare(rps.rpsList.index("r"),1) == 1

def test_rps_compare_rock_and_Scissors():
    assert rps.rps_compare(rps.rpsList.index("r"),2) == -1

def test_rps_compare_paper_and_rock():
    assert rps.rps_compare(rps.rpsList.index("p"),0) == -1

def test_rps_compare_paper_and_paper():
    assert rps.rps_compare(rps.rpsList.index("p"),1) == 0

def test_rps_compare_paper_and_scissors():
    assert rps.rps_compare(rps.rpsList.index("p"),2) == 1

def test_rps_compare_scissors_and_rock():
    assert rps.rps_compare(rps.rpsList.index("s"),0) == 1

def test_rps_compare_scissors_and_paper():
    assert rps.rps_compare(rps.rpsList.index("s"),1) == -1

def test_rps_compare_scissors_and_scissors():
    assert rps.rps_compare(rps.rpsList.index("s"),2) == 0

def test_rps_compare_player_exit():
    assert rps.rps_compare(-1,2) == -2



#monkeypatch the "input" function, so it gives the expected input.
def test_rps_play_customized_user_input_r(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda x: "r")

    assert rps.rps_play() == 0

def test_rps_play_customized_user_input_p(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda x: "p")

    assert rps.rps_play() == 1

def test_rps_play_customized_user_input_s(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda x: "s")

    assert rps.rps_play() == 2

def test_rps_play_customized_user_input_exit(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda x: "exit")

    assert rps.rps_play() == -1

#This test stucks at the while loop waiting for user input
# I am trying to test by asserting the warnings

#@pytest.mark.xfail(raises=Warning)
# def test_rps_play_customized_user_input_rock(monkeypatch):
#     # monkeypatch the "input" function, so that it returns "rock".
#     monkeypatch.setattr('builtins.input', lambda x: "rock")
#     monkeypatch.setattr('rps.rps_play', 'playFlag', "0")

#     with pytest.warns(UserWarning, match='Warning - User input was not r, p or s...'):
#         rps.rps_play()