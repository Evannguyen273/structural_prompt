# Generate the constraints module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_constraints(client, messages):
    messages = [
        {"role": "system", "content": "The user is writing prompts, and you need to help the user refine the constraints part of the prompt. First, analyze the task given by the user and determine the constraints needed to execute the task. Then, directly specify the details about the constraints. For example, for length constraints, you should specify concrete constraints like 'length should not exceed 20 words' rather than vague directions like 'expected word range'. If the user hasn't given specific constraints, complete the content based on your experience and knowledge. Output in an unordered list format, without any interactive information. For example, when the user needs the LLM to conceive a title for a paper, the constraint information might be:\n- Title length should not exceed 20 characters\n- No offensive words should be used\n- Professional terminology should be used"},
    ] + messages
    response = client.generate_response(messages)
    return response