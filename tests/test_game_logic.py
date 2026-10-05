from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)[0]
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)[0]
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)[0]
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


# --- Input range validation ---
from logic_utils import parse_guess, get_range_for_difficulty


def test_guess_within_range_is_accepted():
    assert parse_guess("10", 1, 20) == (True, 10, None)


def test_guess_at_range_boundaries_is_accepted():
    assert parse_guess("1", 1, 20)[0] is True
    assert parse_guess("20", 1, 20)[0] is True


def test_guess_above_range_is_rejected():
    ok, value, err = parse_guess("21", 1, 20)
    assert ok is False
    assert value is None
    assert "between 1 and 20" in err


def test_guess_below_range_is_rejected():
    ok, value, err = parse_guess("0", 1, 20)
    assert ok is False
    assert value is None
    assert "between 1 and 20" in err


def test_negative_guess_is_rejected():
    assert parse_guess("-5", 1, 100)[0] is False


def test_decimal_guess_out_of_range_is_rejected():
    # "50.7" truncates to 50, which is out of range for Easy
    assert parse_guess("50.7", 1, 20)[0] is False


def test_range_is_per_difficulty():
    # 60 is valid on Normal (1-100) but not on Hard (1-50) or Easy (1-20)
    for difficulty, expected in [("Easy", False), ("Hard", False), ("Normal", True)]:
        low, high = get_range_for_difficulty(difficulty)
        assert parse_guess("60", low, high)[0] is expected


def test_non_numeric_and_empty_still_rejected():
    assert parse_guess("abc", 1, 100)[1:] == (None, "That is not a number.")
    assert parse_guess("", 1, 100)[0] is False
    assert parse_guess(None, 1, 100)[0] is False
