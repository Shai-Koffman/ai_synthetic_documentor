import time
import autogen
from config import  llm_config

# creating and engineer agent
engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=llm_config,
    system_message='''Engineer. You follow an approved plan. You write python/shell code to solve tasks.
                      Wrap the code in a code block that specifies the script type. The user can't modify your code. So do not suggest incomplete code which requires others to modify. Don't use a code block if it's not intended to be executed by the executor.
                      Don't include multiple code blocks in one response. Do not ask others to copy and paste the result. 
                      Check the execution result returned by the executor.
                      If the result indicates there is an error, fix the error and output the code again. 
                      Suggest the full code instead of partial code or code changes. 
                      If the error can't be fixed or if the task is not solved even after the code is executed
                      successfully, analyze the problem, revisit your assumption, 
                      collect additional info you need, and think of a different approach to try.
                      save all files to the working directory.''',
)

# creating and code executor agent
code_executor = autogen.UserProxyAgent(
    name="Executor",
    system_message='''Executor. Execute the code written by the engineer and report the result. 
                      Reply TERMINATE if the task has been solved at full satisfaction. 
                      Otherwise, reply CONTINUE, or the reason why the task is not solved yet.''',
    human_input_mode="NEVER",
    code_execution_config={"last_n_messages": 100, "work_dir": "code"},
)

# creating and researcher agent
scientist = autogen.UserProxyAgent(
    name="Researcher",
    llm_config=llm_config,
    system_message="""Researcher. You follow an approved plan (by the planner)
                      You are responsible for creating the information and gathering necessary information from the internet. 
                      This includes market information on Lidar and the car industry (remember that shinobi-z and bord are fictional and do not have any online presence)
                      You then invent the data and write the files to the working directiry, according to the plan.
                      You can respond to the planned that you need the engineer to write code for gathering web data or such and then use these tools.
                      save all files to the working directory as you go along""",
    human_input_mode="NEVER",
    code_execution_config={"last_n_messages": 10, "work_dir": "documents"},
)

# creating and critic agent
critic = autogen.AssistantAgent(
    name="Critic",
    system_message="""Double check plan, claims, code from other agents and provide feedback. 
                      If you find issues respond with method to either fix the issue or to improve the plan.""",
    llm_config=llm_config,
)



#creating the Planner agent
planner = autogen.AssistantAgent(
    name="Planner",
    system_message='''"PLanner, You are a helpful AI assistant, a planner" 
                     
                     You suggest coding and reasoning steps for other AI assistants to accomplish a task:
                     
                     The Engineer can create scripts to solve tasks - such as gathering data from the web, or creating files.
                     The Researcher can research topics on the web (using tools for scraping an searching the engineer will create) and suggest data to be created in files.
                     The Executor can run the scrips that the Engineer creates and report the results.
                     The critic can check the plan and the code and suggest improvements.

                     Think step by step and create a detailed plan to accomplish the tasks you are requested, involving the needed team members.
                     Do not suggest concrete code.
                     convert it to a step that can be implemented by writing code.
                     For example, browsing the web can be implemented by writing code thatreads and prints the content of a web page
                     Finally, inspect the execution result.
                     Explain the plan first. 
                     Be clear which step is performed by whom.
                     instruct the team to save the intermediate results and outputs to the working directory. as they go along
                     operate 1 step at a time.
                     When a step finishes, remind the team of the next steps and assign them
                     Drive the task to completion. 
                     In case of recieving an empty message from one of the users, write the ramining plan and continue'''
                     ,
    llm_config=llm_config,
    human_input_mode="NEVER",
)


# creating and admin agent
admin_user_proxy = autogen.UserProxyAgent(
   name="Admin",
   system_message='''Admin. passes user request to planner, and communicates results to user.
                      The admin shares the user input with the planner.
                      Answers the planner when asked
                      When the planned does not know how to continue , tell him to continue to the next steps in the plan 
                      Do not send empty messages ever!''',

   code_execution_config=False,
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=100,
    )


agents_list = [engineer, code_executor, scientist, planner, critic, admin_user_proxy]

# planner = autogen.AssistantAgent(
#     name="planner",
#     llm_config={"config_list": config_list},
#     # the default system message of the AssistantAgent is overwritten here
#     system_message="You are a helpful AI assistant." +
#                    " You suggest coding and reasoning steps for another AI assistant to accomplish a task."+
#                    " Do not suggest concrete code."+
#                    " For any action beyond writing code or reasoning,"+ 
#                    " convert it to a step that can be implemented by writing code."
#                    +" For example, browsing the web can be implemented by writing code that" 
#                    +" reads and prints the content of a web page." 
#                    +" Finally, inspect the execution result. If the plan is not good," 
#                    +" suggest a better plan. If the execution is wrong, analyze the error and suggest a fix."
# )
# planner_user = autogen.UserProxyAgent(
#     name="planner_user",
#     max_consecutive_auto_reply=0,  # terminate without auto-reply
#     human_input_mode="NEVER",
# )

# def ask_planner(message):
#     planner_user.initiate_chat(planner, message=message)
#     # return the last message received from the planner
#     return planner_user.last_message()["content"]



# # create an AssistantAgent instance named "assistant"
# assistant = autogen.AssistantAgent(
#     name="assistant",
#     llm_config={
#         "temperature": 0,
#         "timeout": 600,
#  #       "cache_seed": 41,
#         "config_list": config_list,
#         "functions": [
#             {
#                 "name": "ask_planner",
#                 "description": "ask planner to: 1. get a plan for finishing a task, 2. verify the execution result of the plan and potentially suggest new plan.",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "message": {
#                             "type": "string",
#                             "description": "question to ask planner. Make sure the question include enough context, such as the code and the execution result. The planner does not know the conversation between you and the user, unless you share the conversation with the planner.",
#                         },
#                     },
#                     "required": ["message"],
#                 },
#             },
#         ],
#     }
# )

# # create a UserProxyAgent instance named "user_proxy"
# user_proxy = autogen.UserProxyAgent(
#     name="user_proxy",
#     human_input_mode="TERMINATE",
#     max_consecutive_auto_reply=10,
#     # is_termination_msg=lambda x: "content" in x and x["content"] is not None and x["content"].rstrip().endswith("TERMINATE"),
#     code_execution_config={"work_dir": "planning"},
#     function_map={"ask_planner": ask_planner},
# )

