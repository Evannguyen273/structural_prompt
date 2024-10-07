# Generate the background module of the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_background(client, messages):
    messages = [
        {"role": "system", "content": "You need to analyze the task given by the user, generate background information for the task, and output it in an unordered list format. For example, when the user needs the LLM to play the game 'Who is the Undercover', the background information might be:\n- You are participating in a game of 'Who is the Undercover'\n- Your identity word is 'yellow peach'."},
    ] + messages
    response = client.generate_response(messages)
    return response