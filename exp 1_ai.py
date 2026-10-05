
room = {
    "A": "Dirty",
    "B": "Dirty"
}


position = "A"


path = []


path_count = 0

print("Initial State:")
print("Room A:", room["A"])
print("Room B:", room["B"])
print("Agent Position:", position)

while room["A"] == "Dirty" or room["B"] == "Dirty":

    if room[position] == "Dirty":
        action = "SUCK"
        room[position] = "Clean"

    elif position == "A":
        action = "RIGHT"
        position = "B"

    elif position == "B":
        action = "LEFT"
        position = "A"

    else:
        action = "NO OPERATION"


    path_count += 1


    path.append((position, action))

    print("\nStep:", path_count)
    print("Position:", position)
    print("Action:", action)

print("\n-------------------------")
print("FINAL STATE")
print("-------------------------")
print("Room A:", room["A"])
print("Room B:", room["B"])

print("\nPATH:")
for i, (pos, action) in enumerate(path, 1):
    print("Step", i, ":", action, "->", pos)

print("\nTotal Path Count:", path_count)
print("Both rooms are CLEAN.")
