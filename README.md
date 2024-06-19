# Trivia---The-Quiz-Game
Welcome to Quizzyy, the most exhilarating true/false quiz game you'll play this minute! 
This Python-based game pulls trivia questions from the Open Trivia Database and lets you test your knowledge while racking up a score. 
Ready to challenge yourself and prove how much useless trivia you know? 
Let's dive in!

## Features
Interactive UI: Built with Tkinter for a sleek and responsive interface.

Dynamic Question Loading: Fetches fresh questions from the Open Trivia Database every time.

Real-time Feedback: Immediate response to your answers with score updates.

## How It Works
### Main Script: main.py
This is the engine room. It:

 -> Imports questions from the data.py file.

 -> Converts the question data into Question objects.
 
 -> Initializes the quiz brain and user interface. 
 
 -> Keeps you updated with your final score when you finish the quiz.

### User Interface: ui.py
This module handles the interaction with the player:

 -> Creates a GUI with buttons and canvas for displaying questions.

 -> Fetches the next question and updates the display.
  
 -> Provides feedback on whether your answers are correct or not.
