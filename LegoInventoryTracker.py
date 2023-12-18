#Lego pieces inventory
piece_3001 = {
    "red": 10,
    "blue": 10,
    "green": 20,
    "yellow": 10,
    "black": 5,
    "white": 30,
    "orange": 8,
    "gray": 12,
    "brown": 7,
    "purple": 3
}

lookup = input("What piece are you looking for?: ")

if lookup in piece_3001:
    total_pieces = piece_3001[lookup]
    total_message = f"There are {total_pieces} 2x4 pieces in {lookup} color in the inventory"
    print(total_message)
else:
    print("Piece not found in inventory")
