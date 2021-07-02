# Generates an abstract for an academic paper in a given field

import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")



def prompt_for_field(academic_field):
    return("The following paper won a prize at this year's most prestigious conference for "+academic_field+":\n\nTitle:")
    
def get_completion(response):
    return response["choices"][0]["text"]

#Get name of academic field as input
academic_field=input("Enter academic field (e.g. \"sociolinguistics of queer communities\"):")


title_response = openai.Completion.create(engine="davinci", prompt=prompt_for_field(academic_field), max_tokens=40, stop='\n')
title=get_completion(title_response).lstrip()
abstract_response=openai.Completion.create(engine="davinci", prompt=prompt_for_field(academic_field)+title+"\nAbstract:\n", max_tokens=400, stop="\n")




print("Here's your abstract!\n")
print(title,"\nAbstract:\n"+get_completion(abstract_response))

#TODO:
# find way to manipulate it into finishing