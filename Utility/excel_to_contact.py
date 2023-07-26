import pandas as pd

contact_list = ""

def create_contact():
    # based on format
    contact_card = f""
    return contact_card

# read excel file location
excel_file = ""
cols = ""

for i in range(1,no_of_records):
    df = pd.read_excel(excel_file, usecols=cols, skiprows=1+i, nrows=1, header=None)
    #print(df)

    # extract info and append to contact_list
    data = df.values

print(contact_list)

# write to contact file
f = open("", "w")
f.write(contact_list)
f.close()
