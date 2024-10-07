# Generate the goal module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_goal(generator, messages):
    messages = [
        {"role": "system", "content": "You need to analyze the task given by the user, determine the goal of the task, and output it in an unordered list format. Do not output any interactive information. Note that the goal should be as simple as possible. When the task doesn't have obviously multiple behaviors, it's usually just 1 item, generally not exceeding 2 items. For example, when the user needs the LLM to calculate the solution to an equation, the goal information might be:\n- Calculate the correct solution to the equation"},
    ] + messages
    response = generator.generate_response(messages)
    return response