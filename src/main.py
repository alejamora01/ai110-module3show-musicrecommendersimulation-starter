"""Runs the music recommender with different user profiles."""

from .recommender import load_songs, recommend_with_mode, SCORING_MODES


PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "likes_acoustic": False
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.3,
        "likes_acoustic": True
    },
    "Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "likes_acoustic": False
    },
    "Conflicting Preferences": {
        "genre": "classical",
        "mood": "intense",
        "energy": 0.95,
        "likes_acoustic": True
    }
}


def main():
    """Runs recommendations using the selected scoring mode."""
    import sys

    mode = sys.argv[1] if len(sys.argv) > 1 else "Genre-First"

    if mode not in SCORING_MODES:
        raise ValueError("Choose: " + ", ".join(SCORING_MODES))

    songs = load_songs("data/songs.csv")
    print("\nScoring Mode:", mode)

    for name, prefs in PROFILES.items():
        print("\n" + "=" * 50)
        print("Profile:", name)
        print("=" * 50)

        results = recommend_with_mode(prefs, songs, k=5, mode=mode)

        for number, (song, score, reason) in enumerate(results, 1):
            print(f"{number}. {song['title']} - {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Because: {reason}")
            print()


if __name__ == "__main__":
    main()
