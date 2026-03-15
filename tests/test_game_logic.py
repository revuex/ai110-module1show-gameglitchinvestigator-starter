from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

#FIX: Refactored logic into logic_utils.py using Copilot Agent mode
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_get_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_get_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_get_range_default():
    low, high = get_range_for_difficulty("Invalid")
    assert low == 1
    assert high == 100

def test_parse_guess_none():
    ok, guess, err = parse_guess(None)
    assert not ok
    assert guess is None
    assert "Enter a guess" in err

def test_parse_guess_empty():
    ok, guess, err = parse_guess("")
    assert not ok
    assert guess is None
    assert "Enter a guess" in err

def test_parse_guess_invalid():
    ok, guess, err = parse_guess("abc")
    assert not ok
    assert guess is None
    assert "not a number" in err

def test_parse_guess_float():
    ok, guess, err = parse_guess("5.0")
    assert ok
    assert guess == 5
    assert err is None

def test_parse_guess_int():
    ok, guess, err = parse_guess("5")
    assert ok
    assert guess == 5
    assert err is None

def test_update_score_win_first_attempt():
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_update_score_win_second_attempt():
    new_score = update_score(0, "Win", 2)
    assert new_score == 70

def test_update_score_win_minimum():
    new_score = update_score(0, "Win", 10)  # 100 - 10*11 = 100-110=-10, min 10
    assert new_score == 10

def test_update_score_too_high_attempt():
    new_score = update_score(0, "Too High", 2)  # even
    assert new_score == -5

def test_update_score_too_low():
    new_score = update_score(0, "Too Low", 1)
    assert new_score == -5

def test_update_score_other():
    new_score = update_score(0, "Other", 1)
    assert new_score == 0
