# ELIZA Chatbot

This is a Python-based chatbot inspired by ELIZA, one of the first AI programs in history. It simulates a simple psychotherapy conversation by responding to user input with predefined patterns using basic natural language techniques.

## About the Project

Originally designed for a university coding inquiry project, this implementation of ELIZA uses:
- Python string manipulation
- Regular expressions (`re`)
- Randomized response logic
- A dictionary of pattern-response pairs

The chatbot mimics a therapist by reflecting the user’s statements back in the form of questions, based on matched patterns.

## Technologies Used

- Python 3
- `re` module (for pattern matching)
- `random` module
- `string` module

## Features

- Recognizes patterns in user input like “I need ___”, “Why can’t I ___”, etc.
- Replaces variables in responses using `%1` placeholder logic
- Includes over 10 custom conversational patterns
- Cleans user input by removing punctuation
- Responds with a default message if no pattern matches

## ▶ How to Run

1. Make sure you have Python 3 installed  
2. Download or clone this repo  
3. Run the chatbot with:

```bash
python eliza_chatbot.py
```

## Sample Interaction

```text
> I feel overwhelmed  
→ Does it make you happy to feel overwhelmed?

> I need more time  
→ Why do you need more time?

> People say I'm lazy  
→ Do you agree with their perception of you as lazy?
```

## What I Learned

- How to design rule-based logic using string patterns  
- Basics of NLP (natural language processing) with regex  
- Clean code organization and dictionary-driven interaction systems

## 🔗 Created by

**Justin Restrepo**  
Student – Computer Programming & Information Systems  
Farmingdale State College  
[LinkedIn](https://linkedin.com/in/justin-restrepo)  
[GitHub](https://github.com/ResJustin1F)

