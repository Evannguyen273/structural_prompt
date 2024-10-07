# Generate the initialization module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_initialization(generator, messages):
    messages = [
        {"role": "system", "content": "You need to analyze the task given by the user, determine the initialization part of the task, which is a one-sentence greeting and communication with the user before the task begins. For example, when the user needs the LLM to provide nutritional planning, the initialization information might be:\nAs a nutritional planner, I will provide nutritional advice based on your situation."},
    ] + messages
    response = generator.generate_response(messages)
    return response