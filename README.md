# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project is a simple music recommendation system built in Python. It recommends songs based on a user's music preferences, such as genre, mood, and energy. The system calculates a score for each song and ranks them to find the best matches.

---

## How The System Works

My recommender uses content-based filtering to suggest songs based on user preferences.

### Song Features
Each song has a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

### User Profile
The user prefers pop music, a happy mood, energy of 0.8, and less acoustic music.

### Algorithm Recipe
- Genre match: 2.0 points
- Mood match: 1.2 points
- Energy similarity: 1 - abs(song energy - target energy)
- Acoustic preference match: 0.5 points

For acousticness, I will use 0.5 as the threshold. The user gets a match when their acoustic preference agrees with whether a song's acousticness is at least 0.5.

The system calculates a score for every song, sorts the results from highest to lowest, and recommends the top K songs.

### Possible Bias
The algorithm might recommend too many songs from the same genre because genre has the highest weight. This could limit music discovery and create a filter bubble.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

The following output was generated using my default pop/happy user profile.

~~~text
Loaded songs: 18

User Profile
Genre: pop | Mood: happy | Energy: 0.8
Acoustic preference: No

Top 5 Recommendations

1. Sunrise City - Neon Echo
   Score: 4.68
   Because: genre match (+2.0), mood match (+1.2), energy similarity (+0.98), acoustic preference match (+0.5)

2. Gym Hero - Max Pulse
   Score: 3.37
   Because: genre match (+2.0), energy similarity (+0.87), acoustic preference match (+0.5)

3. Summer Salsa - Caribe Flow
   Score: 2.68
   Because: mood match (+1.2), energy similarity (+0.98), acoustic preference match (+0.5)

4. Rooftop Lights - Indigo Parade
   Score: 2.66
   Because: mood match (+1.2), energy similarity (+0.96), acoustic preference match (+0.5)

5. Bogota Nights - Luna Beats
   Score: 2.62
   Because: mood match (+1.2), energy similarity (+0.92), acoustic preference match (+0.5)
~~~

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

This project helped me understand how recommendation
systems turn user preferences into ranked suggestions.
I learned that even simple scoring rules can produce
results that feel personalized.

Using AI tools helped me with coding and debugging,
but I still needed to check the logic and compare
the results. One thing that surprised me was how
changing the weights affected the recommendations,
especially for users with conflicting preferences.

If I continued working on this project, I would
add more music genres and user feedback to improve
the recommendations.

For more details, see my [Model Card](model_card.md).
