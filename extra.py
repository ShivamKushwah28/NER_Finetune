import pandas as pd


df = pd.read_csv("finetuning_data.csv")
data = pd.DataFrame()
df.head()
data['text'] = "<s>[INST] "+df['prompt']+ " [/INST] " + df['response']+" </s>"

data.to_csv("data.csv")
