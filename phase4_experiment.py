"""Compares the original scoring weights with an experiment."""

from itertools import combinations
from pathlib import Path

from src.main import PROFILES
from src.recommender import load_songs, recommend_songs


def experimental_score(prefs, song):
    """Uses less genre weight and more energy weight."""
    score = 0.0

    if song["genre"] == prefs["genre"]:
        score += 1.0

    if song["mood"] == prefs["mood"]:
        score += 1.2

    score += 2.0 * max(
        0.0, 1.0 - abs(song["energy"] - prefs["energy"])
    )

    acoustic = song["acousticness"] >= 0.5
    if acoustic == prefs["likes_acoustic"]:
        score += 0.5

    return round(score, 2)


def main():
    """Prints comparisons and writes an evaluation report."""
    songs = load_songs("data/songs.csv")
    lines = []
    results = {}

    for name, prefs in PROFILES.items():
        original = recommend_songs(prefs, songs, k=5)

        experimental = sorted(
            songs,
            key=lambda song: experimental_score(prefs, song),
            reverse=True
        )[:5]

        results[name] = original

        lines.append(f"PROFILE: {name}")
        lines.append("Original top 5:")

        for song, score, _ in original:
            lines.append(f"  {song['title']}: {score:.2f}")

        lines.append("Experimental top 5:")

        for song in experimental:
            score = experimental_score(prefs, song)
            lines.append(f"  {song['title']}: {score:.2f}")

        before = [item[0]["title"] for item in original]
        after = [song["title"] for song in experimental]

        lines.append(
            "Ranking changed: " + str(before != after)
        )
        lines.append("")

    lines.append("PAIRWISE COMPARISONS")

    for (name_a, result_a), (name_b, result_b) in combinations(
        results.items(), 2
    ):
        top_a = result_a[0][0]
        top_b = result_b[0][0]

        lines.append(
            f"{name_a} vs {name_b}: "
            f"{top_a['title']} ({top_a['genre']}, "
            f"{top_a['mood']}) vs "
            f"{top_b['title']} ({top_b['genre']}, "
            f"{top_b['mood']})"
        )

    report = "\n".join(lines) + "\n"
    Path("phase4_experiment_results.txt").write_text(report)

    print(report)


if __name__ == "__main__":
    main()
