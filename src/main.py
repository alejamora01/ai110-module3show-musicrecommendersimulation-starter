"""Runs the music recommender with different user profiles."""

from .recommender import load_songs, recommend_songs


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
    """Prints the five best recommendations for each profile."""
    songs = load_songs("data/songs.csv")

    for name, prefs in PROFILES.items():
        print("\n" + "=" * 50)
        print("Profile:", name)
        print("Preferences:", prefs)
        print("=" * 50)

        results = recommend_songs(prefs, songs, k=5)

        for number, (song, score, reasons) in enumerate(
            results, start=1
        ):
            print(f"{number}. {song['title']} - {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Because: {reasons}")
            print()


if __name__ == "__main__":
    main()
