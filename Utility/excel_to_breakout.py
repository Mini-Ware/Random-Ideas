import pandas as pd

breakout_list = "Pre-assign Room Name,Email Address"

def create_room(room, email):
    # based on format
    room_info = f"{room}, {email}"
    return room_info

# read excel file location
excel_file = ""
cols = ""

no_of_records = 0

for i in range(1,no_of_records):
    df = pd.read_excel(excel_file, usecols=cols, skiprows=1+i, nrows=1, header=None)

    # extract info and append to breakout_list
    data = df.values[0]

rooms = []
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

# assign person into rooms in desired way

# break up into rooms
print()
for room in range(len(rooms)):
    for person in rooms[room]:
        breakout_list += f"\nroom{room+1},{person}"

for room in range(len(rooms)):
    print(f"Room {room+1}: {', '.join(rooms[room])}")

print(breakout_list)

breakout_file = ""
if breakout_file != "":
    f = open(breakout_file, "w")
    f.write(breakout_list)
    f.close()
