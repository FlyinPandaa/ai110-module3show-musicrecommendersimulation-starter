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

The genre weight (+2.0) is so dominant that a song matching only on genre will almost always outrank a song that matches on mood, energy, and acousticness combined. This creates a filter bubble: a user who enjoys "happy pop" will consistently receive "intense pop" (Gym Hero) as a top result simply because it shares the genre label, even though the mood is the opposite of what they asked for. The catalog is also severely unbalanced. Lofi has 3 songs while genres like classical, metal, and reggae each have only one, meaning users of niche genres quickly exhaust their genre matches and receive unrelated results for slots 2 through 5. The scoring treats every user as having a single fixed taste point, so someone with genuinely mixed preferences (such as high energy but a sad mood) gets penalized, the system has no way to honor conflicting signals and will quietly ignore the weaker one. Finally, because the ranking rule simply picks the K closest matches with no diversity enforcement, similar songs cluster at the top: a chill lofi listener receives Library Rain and Midnight Coding as their top two picks even though those songs are nearly identical, but offering no real variety.

---

## 7. Evaluation

Five user profiles were tested against the full 18-song catalog: High-Energy Pop, Chill Lofi, Deep Intense Rock, a Conflicted Listener (high energy but sad mood), and a Niche Classical Fan. For each profile the top 5 results were reviewed to check whether they felt musically reasonable. The clearest successes were profiles with a strong genre presence in the catalog, Storm Runner was an almost perfect match for the rock fan, and Sunday Sermon was the obvious top pick for the classical fan. The most surprising result came from the High-Energy Pop profile: "Gym Hero" (pop, intense) consistently ranked second even though the user explicitly preferred a happy mood, but it kept appearing because the genre match alone was worth more points than any combination of mood and numeric features. A weight-shift experiment was also run where the genre bonus was halved (2.0 → 1.0) and the energy weight was doubled (1.0 → 2.0). The top-ranked song stayed the same for most profiles, but the gap between the #1 and #2 results narrowed significantly, and the Conflicted Listener's rankings reshuffled, showing that the genre weight is the single biggest factor controlling which song wins, not sonic similarity. This confirmed that the system is currently more of a genre sorter than a true taste matcher.

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
