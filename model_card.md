# Model Card - VibeFinder 1.0

## 1. Model Name

VibeFinder 1.0 - Music Recommender Simulation

## 2. Goal / Task

My recommender suggests songs based on a user's music
preferences. It compares genre, mood, energy, and
acousticness to find songs that match their taste.

## 3. Data Used

I used a dataset of 18 songs. The original dataset
had 10 songs, and I added 8 more to include different
genres and moods.

Each song has a title, artist, genre, mood, energy,
tempo, valence, danceability, and acousticness.

The dataset is small and the songs are fictional.
It does not include real listening history or
feedback from users.

## 4. Algorithm Summary

My system uses content-based filtering.

It gives 2.0 points for a genre match and 1.2 points
for a mood match. Energy similarity adds up to 1.0
point, and matching acoustic preferences adds 0.5.

The recommender calculates a score for every song
and sorts the results from highest to lowest.
It then returns the top five recommendations
with explanations.

The maximum possible score is 4.7.

## 5. Observed Behavior / Biases

I noticed that genre has a strong influence on
the recommendations.

For the pop profile, Gym Hero ranked second even
though its mood was intense instead of happy.

The most surprising result was the conflicting
profile. Quiet Piano ranked first because it matched
the genre, even though its energy was much lower
than the user's preference.

This could create a filter bubble because users
might keep getting songs from the same genre.

## 6. Evaluation Process

I tested four different profiles:

- High-Energy Pop
- Chill Lofi
- Intense Rock
- Conflicting Preferences

I compared the top five recommendations for each
profile and checked whether the songs matched
what I would expect.

I also tested a different scoring system by
reducing genre weight from 2.0 to 1.0 and
increasing energy weight from 1.0 to 2.0.

The rankings changed for three out of four
profiles. The Intense Rock profile kept the
same ranking.

For the conflicting profile, Gym Hero became
the top recommendation instead of Quiet Piano.

This showed me how much the weights can affect
the results.

I also ran the project's automated tests,
and both tests passed.

## 7. Intended Use and Non-Intended Use

This project is intended for learning how
recommendation algorithms work.

It can demonstrate how user preferences are
compared with song features.

It is not intended to replace a real music
streaming recommendation system.

It should not be used to make important
decisions about users or to predict their
real musical preferences accurately.

## 8. Ideas for Improvement

1. Add more songs from different genres and moods.
2. Let users like or dislike songs so their
   preferences can improve over time.
3. Add more features such as danceability
   and valence to make recommendations more detailed.

## Personal Reflection

The biggest thing I learned was how a simple scoring
system can create recommendations that actually make
sense. Before this project, I thought recommendation
systems needed much more complicated algorithms.

Using AI tools helped me understand how to organize
the functions, calculate scores, and test different
ideas. I still had to check the results myself and
make sure the code followed my scoring rules.

What surprised me the most was how changing just
two weights could change the order of the songs.
The conflicting profile was a good example because
the original system recommended a calm piano song
to someone who wanted intense music.

If I continued this project, I would add more
songs and allow users to give feedback. I think
that would make the recommendations more useful
and less repetitive.

---

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
