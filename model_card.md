# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps

## Algorithmic Approach

My music recommender uses content-based filtering. It
compares the features of each song with the user's music
preferences instead of using data from other users.

The system gives 2.0 points for a matching genre, 1.2
points for a matching mood, and up to 1.0 point based on
energy similarity. It also gives 0.5 points when the
song matches the user's acoustic preference.

After scoring every song, the system sorts them from
highest to lowest and returns the top five results.
It also explains why each song received its score.

This is a simple rule-based model, not a machine learning
model trained on real listening data. One limitation is
that it might recommend too many songs from the same
genre because genre has the highest weight.


## Phase 4 Evaluation

I tested four different user profiles to see how the recommender responds to different preferences. I also included a profile with conflicting preferences to test an edge case.

### High-Energy Pop

```text
1. Sunrise City - 4.68
   Because: genre match (+2.0), mood match (+1.2), energy similarity (+0.98), acoustic preference match (+0.5)
2. Gym Hero - 3.37
   Because: genre match (+2.0), energy similarity (+0.87), acoustic preference match (+0.5)
3. Summer Salsa - 2.68
   Because: mood match (+1.2), energy similarity (+0.98), acoustic preference match (+0.5)
4. Rooftop Lights - 2.66
   Because: mood match (+1.2), energy similarity (+0.96), acoustic preference match (+0.5)
5. Bogota Nights - 2.62
   Because: mood match (+1.2), energy similarity (+0.92), acoustic preference match (+0.5)
```

### Chill Lofi

```text
1. Library Rain - 4.65
   Because: genre match (+2.0), mood match (+1.2), energy similarity (+0.95), acoustic preference match (+0.5)
2. Midnight Coding - 4.58
   Because: genre match (+2.0), mood match (+1.2), energy similarity (+0.88), acoustic preference match (+0.5)
3. Focus Flow - 3.40
   Because: genre match (+2.0), energy similarity (+0.90), acoustic preference match (+0.5)
4. Spacewalk Thoughts - 2.68
   Because: mood match (+1.2), energy similarity (+0.98), acoustic preference match (+0.5)
5. Coffee Shop Stories - 1.43
   Because: energy similarity (+0.93), acoustic preference match (+0.5)
```

### Intense Rock

```text
1. Storm Runner - 4.66
   Because: genre match (+2.0), mood match (+1.2), energy similarity (+0.96), acoustic preference match (+0.5)
2. Gym Hero - 2.68
   Because: mood match (+1.2), energy similarity (+0.98), acoustic preference match (+0.5)
3. Electric Weekend - 2.68
   Because: mood match (+1.2), energy similarity (+0.98), acoustic preference match (+0.5)
4. Bogota Nights - 1.43
   Because: energy similarity (+0.93), acoustic preference match (+0.5)
5. Sunrise City - 1.37
   Because: energy similarity (+0.87), acoustic preference match (+0.5)
```

### Conflicting Preferences

```text
1. Quiet Piano - 2.73
   Because: genre match (+2.0), energy similarity (+0.23), acoustic preference match (+0.5)
2. Gym Hero - 2.18
   Because: mood match (+1.2), energy similarity (+0.98)
3. Electric Weekend - 2.18
   Because: mood match (+1.2), energy similarity (+0.98)
4. Storm Runner - 2.16
   Because: mood match (+1.2), energy similarity (+0.96)
5. Country Roads Home - 1.10
   Because: energy similarity (+0.60), acoustic preference match (+0.5)
```

### Comparing Profiles

- **High-Energy Pop vs Chill Lofi:** The first profile ranked Sunrise City (pop, happy) first, while the second ranked Library Rain (lofi, chill) first. The different genre, mood, energy, and acoustic preferences affect the scores.
- **High-Energy Pop vs Intense Rock:** The first profile ranked Sunrise City (pop, happy) first, while the second ranked Storm Runner (rock, intense) first. The different genre, mood, energy, and acoustic preferences affect the scores.
- **High-Energy Pop vs Conflicting Preferences:** The first profile ranked Sunrise City (pop, happy) first, while the second ranked Quiet Piano (classical, relaxed) first. The different genre, mood, energy, and acoustic preferences affect the scores.
- **Chill Lofi vs Intense Rock:** The first profile ranked Library Rain (lofi, chill) first, while the second ranked Storm Runner (rock, intense) first. The different genre, mood, energy, and acoustic preferences affect the scores.
- **Chill Lofi vs Conflicting Preferences:** The first profile ranked Library Rain (lofi, chill) first, while the second ranked Quiet Piano (classical, relaxed) first. The different genre, mood, energy, and acoustic preferences affect the scores.
- **Intense Rock vs Conflicting Preferences:** The first profile ranked Storm Runner (rock, intense) first, while the second ranked Quiet Piano (classical, relaxed) first. The different genre, mood, energy, and acoustic preferences affect the scores.

### Weight Experiment

I reduced the genre weight from 2.0 to 1.0 and increased the energy weight from 1.0 to 2.0. I compared the new rankings with the original recommendations.

```text
PROFILE: High-Energy Pop
Original top 5:
  Sunrise City: 4.68
  Gym Hero: 3.37
  Summer Salsa: 2.68
  Rooftop Lights: 2.66
  Bogota Nights: 2.62
Experimental top 5:
  Sunrise City: 4.66
  Summer Salsa: 3.66
  Rooftop Lights: 3.62
  Bogota Nights: 3.54
  Gym Hero: 3.24
Ranking changed: True

PROFILE: Chill Lofi
Original top 5:
  Library Rain: 4.65
  Midnight Coding: 4.58
  Focus Flow: 3.40
  Spacewalk Thoughts: 2.68
  Coffee Shop Stories: 1.43
Experimental top 5:
  Library Rain: 4.60
  Midnight Coding: 4.46
  Spacewalk Thoughts: 3.66
  Focus Flow: 3.30
  Coffee Shop Stories: 2.36
Ranking changed: True

PROFILE: Intense Rock
Original top 5:
  Storm Runner: 4.66
  Gym Hero: 2.68
  Electric Weekend: 2.68
  Bogota Nights: 1.43
  Sunrise City: 1.37
Experimental top 5:
  Storm Runner: 4.62
  Gym Hero: 3.66
  Electric Weekend: 3.66
  Bogota Nights: 2.36
  Sunrise City: 2.24
Ranking changed: False

PROFILE: Conflicting Preferences
Original top 5:
  Quiet Piano: 2.73
  Gym Hero: 2.18
  Electric Weekend: 2.18
  Storm Runner: 2.16
  Country Roads Home: 1.10
Experimental top 5:
  Gym Hero: 3.16
  Electric Weekend: 3.16
  Storm Runner: 3.12
  Quiet Piano: 1.96
  Bogota Nights: 1.86
Ranking changed: True

PAIRWISE COMPARISONS
High-Energy Pop vs Chill Lofi: Sunrise City (pop, happy) vs Library Rain (lofi, chill)
High-Energy Pop vs Intense Rock: Sunrise City (pop, happy) vs Storm Runner (rock, intense)
High-Energy Pop vs Conflicting Preferences: Sunrise City (pop, happy) vs Quiet Piano (classical, relaxed)
Chill Lofi vs Intense Rock: Library Rain (lofi, chill) vs Storm Runner (rock, intense)
Chill Lofi vs Conflicting Preferences: Library Rain (lofi, chill) vs Quiet Piano (classical, relaxed)
Intense Rock vs Conflicting Preferences: Storm Runner (rock, intense) vs Quiet Piano (classical, relaxed)
```

### Accuracy and Surprises

The recommendations generally make sense when the user
has clear preferences. Songs that match the favorite genre
receive a large bonus, which explains why genre matches
can rank higher than songs with a better mood match.
For conflicting preferences, the system still gives a
ranking, even when none of the songs is a perfect match.
I cannot measure real prediction accuracy without actual
user feedback or ground truth.

## Limitations and Bias

The biggest limitation I noticed is that genre has a
strong influence on the final score. This might create
a filter bubble because users could keep receiving music
from the same genres. The dataset is also small and uses
made-up songs, so it does not represent all music styles.
The acousticness rule uses a simple threshold, which
might not describe everyone's actual preferences.
