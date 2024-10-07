# Generate the skills module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_skills(generator, messages):
    messages = [
        {"role": "system", "content": "You need to analyze the task given by the user, determine the skills needed for the task, and output them in an unordered list format. Note that the skill descriptions should be as simple as possible, without including too many details. For example, when the user needs the LLM to comment on current events, the required skills might be:\n- Thoroughly familiar with various social hot topics, able to quickly grasp the ins and outs of events\n- Good at analyzing events from multiple perspectives, providing unique and incisive commentary"},
    ] + messages
    response = generator.generate_response(messages)
    return response