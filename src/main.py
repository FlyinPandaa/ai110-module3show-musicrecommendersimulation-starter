"""
Command line runner for the Music Recommender Simulation.
Runs multiple user profiles to stress-test the recommender.
"""

from src.recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "valence": 0.8,
        "acousticness": 0.1,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.4,
        "valence": 0.6,
        "acousticness": 0.8,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "valence": 0.3,
        "acousticness": 0.1,
    },
    # Adversarial: conflicting preferences (high energy but sad mood)
    "Conflicted Listener": {
        "genre": "r&b",
        "mood": "sad",
        "energy": 0.9,
        "valence": 0.2,
        "acousticness": 0.5,
    },
    # Edge case: genre that has only one song in catalog
    "Niche Classical Fan": {
        "genre": "classical",
        "mood": "peaceful",
        "energy": 0.2,
        "valence": 0.8,
        "acousticness": 0.95,
    },
}


def run_profile(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    print(f"\n{'=' * 50}")
    print(f"Profile: {name}")
    print(f"Prefs:   {user_prefs}")
    print(f"{'=' * 50}")
    results = recommend_songs(user_prefs, songs, k=k)
    for rank, (song, score, explanation) in enumerate(results, start=1):
        print(f"  {rank}. {song['title']} ({song['genre']}, {song['mood']}) — Score: {score:.2f}")
        print(f"     Because: {explanation}")


def main() -> None:
    songs = load_songs("data/songs.csv")

    for name, prefs in PROFILES.items():
        run_profile(name, prefs, songs, k=5)

    print("\n")


if __name__ == "__main__":
    main()
