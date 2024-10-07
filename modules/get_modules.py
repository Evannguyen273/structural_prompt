# Description: Get the modules needed for the task
import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.
import json

def get_modules(generator, messages):
    '''
    Get the modules needed for the task
    :param generator: OpenAI client
    :param messages: The task description and context
    :return: The modules needed for the task
    The Correct format of the modules is:
    {
        background: bool,
        command: bool,
        suggestion: bool,
        goal: bool,
        examples: bool,
        constraints: bool,
        workflow: bool,
        output_format: bool,
        skills: bool,
        style: bool,
        initialization: bool
    }
    '''
    default_modules = {
        "background": True,
        "command": False,
        "suggesstion": False,
        "goal": True,
        "examples": False,
        "constraints": True,
        "workflow": True,
        "output_format": True,
        "skills": False,
        "style": False,
        "initialization": True
    }
    ## Generate the modules needed for the task
    messages = [
        {"role": "system", "content": "You need to analyze the task type given by the user, analyze the modules needed for the complete prompt to describe this task, such as: background, goal, constraints, commands, suggestions, task examples, workflow, output format, skills, style, initialization, etc. Output in JSON format, indicating whether a certain class is needed, with True for needed classes and False for unneeded classes. For example, when background, skills, workflow, output format, and initialization are needed, the specific format is as follows: {\"background\": True, \"command\": False, \"suggesstion\": False, \"goal\": False, \"examples\": False, \"constraints\": False, \"workflow\": True, \"output_format\": True, \"skills\": True, \"style\": False, \"initialization\": True}"},
    ] + messages
    response = generator.generate_response(messages).replace("```", "").replace("\n", "").replace("json", "").replace(" ", "").replace("True", "true").replace("False", "false")

    for i in range(5):
        ## Verify if the format of the modules is correct
        try:
            ## Load the modules
            print(response)
            modules = json.loads(response)
            ## Check if there are missing modules or extra modules
            for key in ["background", "command", "suggesstion", "goal", "examples", "constraints", "workflow", "output_format", "skills", "style", "initialization"]:
                if key not in modules:
                    modules[key] = False
            extra_keys = [key for key in modules.keys() if key not in ["background", "command", "suggesstion", "goal", "examples", "constraints", "workflow", "output_format", "skills", "style", "initialization"]]
            for key in extra_keys:
                del modules[key]
            return modules
        except Exception as e:
            print(e)
            continue
    ## Return the default modules if the format is incorrect
    return default_modules