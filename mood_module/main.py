"""
Remember to take your time and work through each question diligently! Test your code, make sure it works,
 and try to find ways to improve. Once you are happy and satisfied with your code, 
 upload it to Github, then turn in your Github link at the bottom of the page!


Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

1. Python Modules and Data Handling Assignment
Objective: The aim of this assignment is to assess your understanding and ability to implement Python 
modules, both built-in and custom, and to apply data handling techniques using Python's data structures and error handling.

Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module that asks the 
user how they are feeling today and responds with a custom message based on the mood entered. - Code Example:

    # mood_responses.py
    def mood_response(mood):
        # Implement your response logic here

    # main.py
    import mood_responses
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))
- Expected Outcome: The program should be able to take a user's mood as input 
(e.g., happy, sad, excited) and return a corresponding custom message.
"""
import mood_responses

def main():
    mood = input('What is your mood today?').lower()
    mood_responses.mood_response(mood)

if __name__ == "__main__":
    main()