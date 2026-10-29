"""Runs the music recommender in the terminal."""

from .recommender import load_songs, recommend_songs


def main():
    """Displays the top five song recommendations."""
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "likes_acoustic": False
    }

    print("\nUser Profile")
    print("Genre: pop | Mood: happy | Energy: 0.8")
    print("Acoustic preference: No")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop 5 Recommendations\n")

    for number, (song, score, explanation) in enumerate(
        recommendations, start=1
    ):
        print(f"{number}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
