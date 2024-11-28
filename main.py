import pandas as pd

# Initialize lists to store data
data = []
column_names = [
    "RECORD_ID",
    "CAMPNO",
    "MAKETXT",
    "MODELTXT",
    "YEARTXT",
    "MFGCAMPNO",
    "COMPNAME",
    "MFGNAME",
    "BGMAN",
    "ENDMAN",
    "RCLTYPECD",
    "POTAFF",
    "ODATE",
    "INFLUENCED_BY",
    "MFGTXT",
    "RCDATE",
    "DATEA",
    "RPNO",
    "FMVSS",
    "DESC_DEFECT",
    "CONEQUENCE_DEFECT",
    "CORRECTIVE_ACTION",
    "NOTES",
    "RCL_CMPT_ID",
    "MFR_COMP_NAME",
    "MFR_COMP_DESC",
    "MFR_COMP_PTNO"
]
# Read the text file line by line
with open("FLAT_RCL.txt", "r") as file:
    for line in file:
        # Split each line by tabs and append to data list
        row = line.strip().split("\t")
        data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=column_names)

# Displaying the DataFrame
# print(df)
# df.to_csv("formated_data.csv")

print(df[[ "DESC_DEFECT","CONEQUENCE_DEFECT","CORRECTIVE_ACTION","NOTES"]].to_csv("Extracted_data.csv"))