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
This module handles the interaction with the player, it requires two images for buttons, which are attached alongwith files:

 -> Creates a GUI with buttons and canvas for displaying questions.

 -> Fetches the next question and updates the display.
  
 -> Provides feedback on whether your answers are correct or not.

### Quiz Logic: quiz_brain.py
The brain behind the operation:

 -> Manages the flow of questions.
 
 -> Checks if answers are correct.
 
 -> Keeps track of the score and current question number.

 ### Question Data: data.py
This script pulls trivia questions from the Open Trivia Database API. Feel free to tweak the parameters to adjust the quiz settings.

### Question Model: question_model.py
Defines the Question class to create question objects.

## Running the Game
To get started, clone this repository and run main.py. Make sure you have Tkinter installed and an active internet connection to fetch the latest questions. Enjoy the quiz and may your brain cells multiply!

## Contributions
Feel free to fork this repository, make improvements, and submit a pull request. We welcome contributions that make Quizzyy even better!
