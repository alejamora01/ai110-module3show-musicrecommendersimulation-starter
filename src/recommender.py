import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """Stores a song and its features."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Stores a user's music preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file."""
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])

            for feature in [
                "energy", "tempo_bpm", "valence",
                "danceability", "acousticness"
            ]:
                row[feature] = float(row[feature])

            songs.append(row)

    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculates a song's score and explains the matches."""
    score = 0.0
    reasons = []

    genre = user_prefs.get("genre",
                           user_prefs.get("favorite_genre", ""))
    mood = user_prefs.get("mood",
                          user_prefs.get("favorite_mood", ""))
    energy = user_prefs.get("energy",
                            user_prefs.get("target_energy", 0.5))

    if song["genre"].lower() == genre.lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == mood.lower():
        score += 1.2
        reasons.append("mood match (+1.2)")

    energy_points = max(
        0.0, 1.0 - abs(song["energy"] - energy)
    )
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    if "likes_acoustic" in user_prefs:
        acoustic_song = song["acousticness"] >= 0.5

        if acoustic_song == user_prefs["likes_acoustic"]:
            score += 0.5
            reasons.append("acoustic preference match (+0.5)")

    return round(score, 2), reasons


def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Ranks songs and returns the top recommendations."""
    results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        results.append((song, score, explanation))

    ranked = sorted(
        results, key=lambda item: item[1], reverse=True
    )

    return ranked[:k]


class Recommender:
    """Object-oriented version of the music recommender."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the highest-scoring Song objects."""
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic
        }

        results = []

        for song in self.songs:
            score, _ = score_song(prefs, vars(song))
            results.append((song, score))

        ranked = sorted(
            results, key=lambda item: item[1], reverse=True
        )

        return [song for song, score in ranked[:k]]

    def explain_recommendation(
        self, user: UserProfile, song: Song
    ) -> str:
        """Explains why a song matches the user's preferences."""
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic
        }

        score, reasons = score_song(prefs, vars(song))
        return f"Score: {score:.2f} - " + ", ".join(reasons)


# Optional Challenge 2: Multiple Scoring Modes

SCORING_MODES = {
    "Genre-First": {
        "genre": 2.0,
        "mood": 1.2,
        "energy": 1.0,
        "acoustic": 0.5
    },
    "Mood-First": {
        "genre": 1.0,
        "mood": 2.0,
        "energy": 1.0,
        "acoustic": 0.5
    },
    "Energy-Focused": {
        "genre": 1.0,
        "mood": 1.2,
        "energy": 2.0,
        "acoustic": 0.5
    }
}


def score_with_mode(user_prefs, song, mode="Genre-First"):
    """Calculates a song score using the selected weights."""
    if mode not in SCORING_MODES:
        raise ValueError("Unknown scoring mode: " + mode)

    weights = SCORING_MODES[mode]
    score = 0.0
    reasons = []

    genre = user_prefs.get("genre", user_prefs.get("favorite_genre", ""))
    mood = user_prefs.get("mood", user_prefs.get("favorite_mood", ""))
    energy = user_prefs.get("energy", user_prefs.get("target_energy", 0.5))

    if song["genre"].lower() == genre.lower():
        score += weights["genre"]
        reasons.append(f"genre match (+{weights['genre']:.1f})")

    if song["mood"].lower() == mood.lower():
        score += weights["mood"]
        reasons.append(f"mood match (+{weights['mood']:.1f})")

    similarity = max(0.0, 1.0 - abs(song["energy"] - energy))
    points = similarity * weights["energy"]
    score += points
    reasons.append(f"energy similarity (+{points:.2f})")

    if "likes_acoustic" in user_prefs:
        acoustic = song["acousticness"] >= 0.5

        if acoustic == user_prefs["likes_acoustic"]:
            score += weights["acoustic"]
            reasons.append(f"acoustic match (+{weights['acoustic']:.1f})")

    return round(score, 2), reasons


def recommend_with_mode(user_prefs, songs, k=5, mode="Genre-First"):
    """Ranks songs using the selected scoring strategy."""
    results = []

    for song in songs:
        score, reasons = score_with_mode(user_prefs, song, mode)
        results.append((song, score, ", ".join(reasons)))

    return sorted(results, key=lambda item: item[1], reverse=True)[:k]
