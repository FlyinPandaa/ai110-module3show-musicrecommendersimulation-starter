import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
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
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "acousticness": 0.9 if user.likes_acoustic else 0.1,
        }
        song_dicts = [s.__dict__ for s in self.songs]
        ranked = recommend_songs(user_prefs, song_dicts, k=k)
        top_ids = {rec[0]["id"] for rec in ranked}
        return sorted(
            [s for s in self.songs if s.id in top_ids],
            key=lambda s: next(score for d, score, _ in ranked if d["id"] == s.id),
            reverse=True,
        )

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "acousticness": 0.9 if user.likes_acoustic else 0.1,
        }
        _, _, explanation = score_song(user_prefs, song.__dict__)
        return explanation


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Numeric fields are converted to float or int for math operations.
    """
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    int(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[Dict, float, str]:
    """
    Scores a single song against a user's preferences.

    Scoring recipe:
      +2.0  genre match
      +1.0  mood match
      +1.0  energy proximity    (1 - |user - song|)
      +0.5  valence proximity   (if provided)
      +0.5  acousticness proximity (if provided)

    Returns (song, score, explanation).
    """
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    if "energy" in user_prefs:
        energy_score = 1.0 - abs(user_prefs["energy"] - song["energy"])
        score += energy_score
        reasons.append(f"energy proximity (+{energy_score:.2f})")

    if "valence" in user_prefs:
        valence_score = 0.5 * (1.0 - abs(user_prefs["valence"] - song["valence"]))
        score += valence_score
        reasons.append(f"valence proximity (+{valence_score:.2f})")

    if "acousticness" in user_prefs:
        acoustic_score = 0.5 * (1.0 - abs(user_prefs["acousticness"] - song["acousticness"]))
        score += acoustic_score
        reasons.append(f"acousticness proximity (+{acoustic_score:.2f})")

    explanation = ", ".join(reasons) if reasons else "no strong match"
    return song, score, explanation


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song and returns the top-k results sorted highest to lowest.

    Uses sorted() (not .sort()) to leave the original songs list unchanged.
    """
    scored = [score_song(user_prefs, song) for song in songs]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
