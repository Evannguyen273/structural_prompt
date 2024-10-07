# Generate the command module of the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_command(client, messages):
    messages = [
        {"role": "system", "content": "You need to analyze the task given by the user, create command prompts for the LLM based on the actions that might be needed for the task, and output them in an unordered list format. Each command should start with '/', followed by the command word, and then an explanation of the command. For example, when the user needs the LLM to play the game 'Who is the Undercover', the command information might be:\n- /describe Please describe your identity word\n- /vote Please vote for the player you think is from the opposing team"},
    ] + messages
    response = client.generate_response(messages)
    return response