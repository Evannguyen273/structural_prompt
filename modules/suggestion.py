# Generate the suggestion module of the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_suggestion(client, messages):
    messages = [
        {"role": "system", "content": "You need to analyze the task given by the user, generate suggestion information for the task, and output it in an unordered list format. Do not output any interactive information. For example, when the user needs the LLM to play the 'Who is the Undercover' game, the suggestion information might be:\n- When you're unsure about your team, your description should be as vague as possible"},
    ] + messages
    response = client.generate_response(messages)
    return response