#!/usr/bin/env python3

import autogen
from config import config_list, llm_config
import agents as ag

    

#a main method that prints hello world
def main():
    manager = None
    try:
        groupchat = autogen.GroupChat(agents=ag.agents_list, 
                                  messages=[], max_round=100)    
        manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config,)
    #catch all exceptions and print the status
    except Exception as e:
        print ("Exception occured" + str(e))
    
    if not manager:
        print ("manager not created")
        return
    
    ag.admin_user_proxy.initiate_chat(manager, 
                                      message = 
                                      """
                                        Ask the planner:  plan and initiate the below mission:
                                        Create all necessary information to respond to an RFP from a 
                                        fictional car manufacturer (Bord company) to a Fictional Lidar Provider (Shinobi-z).
                                        The collection must include:
                                        
                                        1-Pager describing the Shinobi-z Lidar company.
                                        A fictional organizational structure, with names, roles, departments, email addresses for Shinobi-z
                                        A fictional set of counterparts in Bord company.
                                        A set of fictional emails correspondences related to the topic or any other relevant between Shinobi-z employees.
                                        A set of Slack sessions between Shinobi-z employees
                                        A set of fictional emails related to the RFP between Employees and the Bord company.
                                        A set of Product documentation about the Shinob-z product, limitations and roadmap
                                        Market information - Both on  Lidar and on the car industry as a whole, This can also be real information from the internet.
                                        Technical Specification, and technical docs of the Shinobi-z Lidar product.
                                        A set of historical RFQ’s by other car companies to Shinobi-z and responses as reference material., If you can find references in the internet of such RFQ’s by car companies to Lidar companies that can be good as well.
                                        The Bord company RFP.

                                        All the data should be split to relevant directories and saved each in a different text file (.txt, .pdf. , .docx are all good)
                                        """ )
  

if __name__ == "__main__":
    main()