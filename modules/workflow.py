# Generate the workflow module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_workflow(generator, messages):
    messages = [
        {"role": "system", "content": "You need to analyze the task given by the user, break down the workflow needed to execute this task, and output it in an ordered list format. The numbers indicate the sequence, and do not output any interactive information. For conditional branch processes, you can use sub-processes like '1.1' and '1.2'; for iterative loop processes, you can use phrases like 'Jump to step 2' or 'Repeat the previous step'. For example, when the user needs the LLM to solve a quadratic equation, the workflow information might be:\n1. Convert the equation to standard form, identifying the coefficients a, b, and c.\n2. Calculate the discriminant of the equation, analyze the root situation\n2.1 If discriminant > 0, the equation has two real roots;\n2.2 If discriminant = 0, the equation has one real root;\n2.3 If discriminant < 0, the equation has no real roots\n3. Give the form of the solution based on the root situation\n4. Solve for the roots of the equation\n5. Verify the correctness of the solution"},
    ] + messages
    response = generator.generate_response(messages)
    return response