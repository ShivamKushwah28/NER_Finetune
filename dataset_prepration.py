import pandas as pd
import os
from openai import OpenAI

# Initialize lists to store data
data = []
os.environ['OPENAI_API_KEY'] = "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"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


# Read the text file line by line
with open("FLAT_RCL.txt", "r") as file:
    for line in file:
        data.append(line)

def get_completion(prompt, model="gpt-3.5-turbo"):
  chat_completion = client.chat.completions.create(
      messages=[{"role": "user","content": prompt}],
      model=model,
  )
  return chat_completion.choices[0].message.content


dataset = {
   "prompt": [],
   "response": []
}

for row in data[:50]:
   temp = """ 
    Give me the entities from above data like this  in json format

    [ {"Entity": "bottoming out the suspension", "Label": "Failure Issue"},
    {"Entity": "amplification of the stress", "Label": "Failure Issue"},
    {"Entity": "floor truss network", "Label": "Component"},
    {"Entity": "fracture of welds", "Label": "Failure Issue"},
    {"Entity": "chassis frame rail", "Label": "Component"},
    {"Entity": "floor truss network support system", "Label": "Component"},
    {"Entity": "damage to electrical wiring", "Label": "Failure Issue"},
    {"Entity": "fuel lines", "Label": "Component"},
    {"Entity": "fire", "Label": "Failure Issue"} ]"""
   
   prompt = row +" "+ temp
   answer = get_completion(prompt)

   dataset['prompt'].append(row)
   dataset['response'].append(answer)


finaldata = pd.DataFrame(dataset)
finaldata.to_csv("finetuning_data.csv")