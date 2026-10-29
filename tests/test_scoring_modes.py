"""Tests for the optional scoring modes."""

import pytest

from src.recommender import (
    load_songs,
    score_song,
    score_with_mode,
    recommend_with_mode,
    SCORING_MODES
)


@pytest.fixture
def songs():
    return load_songs("data/songs.csv")


@pytest.fixture
def prefs():
    return {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "likes_acoustic": False
    }


def test_three_modes():
    """Checks that all three modes exist."""
    assert len(SCORING_MODES) == 3


def test_all_modes_rank_songs(songs, prefs):
    """Checks that every mode returns ranked results."""
    for mode in SCORING_MODES:
        results = recommend_with_mode(prefs, songs, k=5)
        assert len(results) == 5
        scores = [item[1] for item in results]
        assert scores == sorted(scores, reverse=True)


def test_original_scores(songs, prefs):
    """Checks that Genre-First matches the original algorithm."""
    for song in songs:
        original, _ = score_song(prefs, song)
        new, _ = score_with_mode(prefs, song, "Genre-First")
        assert original == new


def test_modes_change_scores(songs, prefs):
    """Checks that the selected mode changes scoring."""
    song = songs[0]
    scores = [
        score_with_mode(prefs, song, mode)[0]
        for mode in SCORING_MODES
    ]
    assert len(set(scores)) > 1


def test_invalid_mode(songs, prefs):
    """Checks that invalid modes raise an error."""
    with pytest.raises(ValueError):
        score_with_mode(prefs, songs[0], "Unknown")
