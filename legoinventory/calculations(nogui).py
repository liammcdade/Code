

file_path = "inventory_data.txt"

def read_inventory_data(file_path):
    inventory_data = {}
    with open(file_path, "r") as file:
        for line in file:
            if not line.strip():
                continue

            tokens = line.strip().split()

            if len(tokens) < 3:
                print(f"Skipping line: {line.strip()}")
                continue

            piece_number = tokens[0]
            color = ' '.join(tokens[1:-1])
            quantity = int(tokens[-1])

            if piece_number not in inventory_data:
                inventory_data[piece_number] = {}
            inventory_data[piece_number][color.lower()] = quantity

    return inventory_data

def calculate_total(piece, color, inventory_data):
    if not piece.isdigit():
        print(f"Invalid piece number: {piece}")
        return

    selected_piece = int(piece)
    key = f"{selected_piece}"

    if key in inventory_data:
        total = inventory_data[key].get(color, 0)
        print(f"Total quantity of {color} {selected_piece}: {total}")
    else:
        print(f"Piece {selected_piece} not found in inventory")

def lookup_color_total(inventory_data):
    total_quantity = sum(quantity for piece_data in inventory_data.values() for quantity in piece_data.values())
    print(f"Total quantity of all pieces and colors: {total_quantity}")

def update_color_total(piece, color, new_value, inventory_data, file_path):
    if not piece.isdigit():
        print(f"Invalid piece number: {piece}")
        return

    selected_piece = int(piece)
    key = f"{selected_piece}"

    if key in inventory_data:
        inventory_data[key][color.lower()] = new_value
        save_inventory_data(inventory_data, file_path)
        print(f"Updated total quantity of {color} for piece {selected_piece}: {new_value}")
    else:
        print(f"Piece {selected_piece} not found in inventory")

def save_inventory_data(inventory_data, file_path):
    with open(file_path, "w") as file:
        for piece_number, color_quantity in inventory_data.items():
            for color, quantity in color_quantity.items():
                file.write(f"{piece_number} {color} {quantity}\n")

def get_text_color(color):
    color_mappings = {
        "red": "red",
        "blue": "blue",
    }

    return color_mappings.get(color, "black")

def main():
    inventory_data = read_inventory_data(file_path)

    while True:
        print("\n1. Calculate Total")
        print("2. Lookup Color Total")
        print("3. Update Color Total")
        print("4. Lookup Total of All Pieces and Colors")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            piece = input("Enter piece number: ")
            color = input("Enter color: ")
            calculate_total(piece, color, inventory_data)
        elif choice == "2":
            color = input("Enter color: ")
            lookup_color_total(inventory_data)
        elif choice == "3":
            piece = input("Enter piece number: ")
            color = input("Enter color: ")
            new_value = int(input("Enter new value: "))
            update_color_total(piece, color, new_value, inventory_data, file_path)
        elif choice == "4":
            lookup_color_total(inventory_data)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
