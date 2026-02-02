from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_get_range_for_difficulty_known():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_get_range_for_difficulty_default():
    # Unknown difficulty falls back to Normal range
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_parse_guess_empty_and_none():
    ok, val, err = parse_guess(None)
    assert ok is False and val is None and err == "Enter a guess."

    ok, val, err = parse_guess("")
    assert ok is False and val is None and err == "Enter a guess."


def test_parse_guess_numbers_and_invalid():
    ok, val, err = parse_guess("42")
    assert ok is True and val == 42 and err is None

    ok, val, err = parse_guess("10.0")
    assert ok is True and val == 10 and err is None

    ok, val, err = parse_guess("not a number")
    assert ok is False and val is None and err == "That is not a number."


def test_check_guess_with_ints_and_string_secret():
    # integer comparisons
    assert check_guess(50, 50) == "Win"
    assert check_guess(60, 50) == "Too High"
    assert check_guess(40, 50) == "Too Low"

    # secret stored as a string (app sometimes does this); exact match should still win
    assert check_guess(50, "50") == "Win"


def test_update_score_win_and_floor():
    # Winning on early attempt gives larger points
    assert update_score(0, "Win", 1) > 0

    # Ensure floor of 10 points when formula would go below 10
    # attempt_number=9 -> points = 100 - 10*(9+1) = 0 -> floored to 10
    assert update_score(0, "Win", 9) == 10


def test_update_score_too_high_alternates_and_too_low():
    # Too High: even attempt -> +5, odd attempt -> -5
    assert update_score(0, "Too High", 2) == 5
    assert update_score(0, "Too High", 1) == -5

    # Too Low always -5
    assert update_score(10, "Too Low", 1) == 5


def test_update_score_unknown_outcome_no_change():
    assert update_score(7, "SomethingElse", 1) == 7
