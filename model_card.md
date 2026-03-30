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

Genre is worth too many points (+2.0), so it overrides everything else. A "happy pop" user gets "intense pop" in their top results just because the genre matches, even though the mood is wrong. The catalog is also unbalanced: lofi has 3 songs, but most other genres have only 1, so niche listeners run out of genre matches quickly. The system also can't handle mixed preferences, for example, a user who wants high energy but a sad mood will have one of those signals ignored. Finally, the top results often look too similar to each other, since there is nothing stopping two nearly identical songs from both appearing in the top 5.

---

## 7. Evaluation

Five profiles were tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, a Conflicted Listener (high energy + sad mood), and a Niche Classical Fan. Most top picks felt right, Storm Runner was a clear match for the rock fan, and Sunday Sermon was the obvious choice for the classical fan. The most surprising result: "Gym Hero" kept showing up for the happy pop user even though its mood is intense, not happy. It ranked second simply because it shares the pop genre label, which is worth more points than a correct mood match. A weight experiment was also run and halving the genre bonus and doubling the energy weight. The top song rarely changed, but the scores got much closer together, which showed that genre is currently the biggest factor deciding who wins.
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
