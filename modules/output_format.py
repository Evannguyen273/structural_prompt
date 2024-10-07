# Generate the output_format module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_output_format(generator, messages):
    messages = [
        {"role": "system", "content": "You need to analyze the task given by the user, determine the output format for the task, and do not output any interactive information. Note that the output format should be as simple as possible, prioritizing standard formats such as JSON or XML. If standard formats are not applicable to this task, briefly describe the specified format in one sentence, without including too many details. For example, when the user needs the LLM to calculate the solution to an equation, the output format information might be:\n- The output is only a single number, representing the solution to the equation"},
    ] + messages
    response = generator.generate_response(messages)
    return response