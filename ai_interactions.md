# AI Interactions Log

## Design Pattern (SF10)

**Which design pattern did you use?**

I used a simple strategy-based design for my music recommender.

**How did AI help you brainstorm or implement it?**

I used ChatGPT to help me add three scoring modes:
Genre-First, Mood-First, and Energy-Focused.

The idea was to keep the same scoring process but use
different weights for each recommendation mode.

**How does the pattern appear in your final code?**

In recommender.py, SCORING_MODES stores the weights
for each mode.

The score_with_mode function uses those weights,
and recommend_with_mode ranks the songs.

This makes it easier to try different recommendation
strategies without rewriting the entire algorithm.

**What did you verify?**

I ran the original tests and checked the Energy-Focused
results with four different user profiles.

The conflicting profile was interesting because
Gym Hero ranked above Quiet Piano when energy
became more important.
