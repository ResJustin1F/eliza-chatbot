## Justin Restrepo 

 

import re
import random
import string

def eliza_chatbot():
    print("Hello! I'm ELIZA, your virtual therapist. How can I help you today? (Type 'quit' to exit.)")

    while True:
        user_input = input("> ")

        # Exit condition
        if user_input.lower() == 'quit':
            print("Goodbye! Take care.")
            break

        # Patterns and responses
        responses = {
            r"I need (.*)": [
                "Why do you need %1?",
                "Would obtaining %1 really help you?",
                "Are you sure you need %1?"   
            ],

            r"Why don't you (.*)\??": [
                "Do you really think I don't %1?",
                "Perhaps eventually I will %1.",
                "Do you want me to %1?"    
            ],

            r"Why can't I (.*)\??": [
                "Do you think you should be able to %1?",
                "If you could %1, what would you do?",
                "What would help you %1?"    
            ],

            r"I am (.*)": [
                "Did you come to me because you are %1?",
                "How long have you been %1?",
                "How do you feel about being %1?"
            ],

            # Additional patterns and responses
            r"I feel (.*)": [
                "Does it make you happy to feel %1?",
                "Why do you feel %1?",
                "When you feel %1, how do you typically deal with it?",
            ],

            r"My dreams (.*)": [
                "What do you think your dreams about %1 mean?",
                "Do these dreams have any recurring themes?",
                "How do these dreams impact your waking life?",
            ],

            r"People say I'm (.*)": [
                "How do you feel about what people are saying about you being %1?",
                "Do you agree with their perception of you as %1?",
                "Have you talked to those people about their opinions of you being %1?",
            ],

            r"I can't (.*)": [
                "What makes you think you can't %1?",
                "Do you feel restricted in your ability to %1?",
                "What would happen if you could %1?",
            ],

            r"I love (.*)": [
                "What do you enjoy most about %1?",
                "How does your love for %1 make you feel?",
                "Tell me more about your feelings towards %1.",
            ],

            r"Sometimes I (.*)": [
                "In what situations do you %1?",
                "Can you identify any patterns related to %1?",
                "How do you feel about yourself when you %1?",
            ],

            r"I'm worried about (.*)": [
                "What specifically worries you about %1?",
                "Have you talked to anyone else about your concerns regarding %1?",
                "How long have you been worried about %1?",
            ],

            r"People around me (.*)": [
                "How do you perceive the people around you regarding %1?",
                "Do you think their opinions about %1 affect you?",
                "Have you discussed %1 with those people?",
            ],

            r"I dream of (.*)": [
                "What do you think your dreams about %1 symbolize?",
                "Do these dreams evoke any emotions?",
                "How do you feel about the possibility of %1?",
            ],

            r"I can't stop thinking about (.*)": [
                "What aspects of %1 occupy your thoughts?",
                "Do you find it challenging to redirect your thoughts from %1?",
                "How would you feel if you could control your thoughts about %1?",
            ],
        }

        # Default response if no pattern matches
        default_response = "Tell me more."

        # Check each pattern and select a response
        for pattern, pattern_responses in responses.items():
            match = re.fullmatch(pattern, user_input, re.IGNORECASE)
            if match:
                # Remove punctuation from the captured group
                captured_group = match.group(1).translate(str.maketrans('', '', string.punctuation))
                response = random.choice(pattern_responses)
                # Replace the placeholder with the cleaned captured group
                response = response.replace('%1', captured_group)
                break
        else:
            response = default_response

        print(response)

# Run the chatbot
eliza_chatbot()
