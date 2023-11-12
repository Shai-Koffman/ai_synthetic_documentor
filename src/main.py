#!/usr/bin/env python3

import autogen
from config import config_list

planner = autogen.AssistantAgent(
    name="planner",
    llm_config={"config_list": config_list},
    # the default system message of the AssistantAgent is overwritten here
    system_message="You are a helpful AI assistant." +
                   " You suggest coding and reasoning steps for another AI assistant to accomplish a task."+
                   " Do not suggest concrete code."+
                   " For any action beyond writing code or reasoning,"+ 
                   " convert it to a step that can be implemented by writing code."
                   +" For example, browsing the web can be implemented by writing code that" 
                   +" reads and prints the content of a web page." 
                   +" Finally, inspect the execution result. If the plan is not good," 
                   +" suggest a better plan. If the execution is wrong, analyze the error and suggest a fix."
)
planner_user = autogen.UserProxyAgent(
    name="planner_user",
    max_consecutive_auto_reply=0,  # terminate without auto-reply
    human_input_mode="NEVER",
)

def ask_planner(message):
    planner_user.initiate_chat(planner, message=message)
    # return the last message received from the planner
    return planner_user.last_message()["content"]



# create an AssistantAgent instance named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "temperature": 0,
        "timeout": 600,
 #       "cache_seed": 41,
        "config_list": config_list,
        "functions": [
            {
                "name": "ask_planner",
                "description": "ask planner to: 1. get a plan for finishing a task, 2. verify the execution result of the plan and potentially suggest new plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "question to ask planner. Make sure the question include enough context, such as the code and the execution result. The planner does not know the conversation between you and the user, unless you share the conversation with the planner.",
                        },
                    },
                    "required": ["message"],
                },
            },
        ],
    }
)

# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    # is_termination_msg=lambda x: "content" in x and x["content"] is not None and x["content"].rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "planning"},
    function_map={"ask_planner": ask_planner},
)






#a main method that prints hello world
def main():
    user_proxy.initiate_chat(
    assistant,
    message="""Suggest a fix to an open good first issue of flaml""",
) 

if __name__ == "__main__":
    main()