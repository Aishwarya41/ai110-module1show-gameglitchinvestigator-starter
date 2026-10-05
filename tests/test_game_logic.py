from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_hint_says_go_lower_when_guess_too_high():
    # Regression: hints were backwards. A guess above the secret must tell the player to go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_hint_says_go_higher_when_guess_too_low():
    # Regression: a guess below the secret must tell the player to go HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_hint_direction_with_string_secret():
    # app.py passes the secret as a str on some attempts; hints must still be numeric and correct.
    # 9 vs "10" would be "Too High" under string comparison.
    outcome, message = check_guess(9, "10")
    assert outcome == "Too Low"
    assert "HIGHER" in message
