import tkinter as tk
from tkinter import ttk

file_path = "inventory_data.txt"


def read_inventory_data(file_path):
    inventory_data = {}
    with open(file_path, "r") as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue

            # Split the line into tokens
            tokens = line.strip().split()

            # Check if the line has at least three tokens (piece number, color, quantity)
            if len(tokens) < 3:
                print(f"Skipping line: {line.strip()}")
                continue

            # Extract piece number, color, and quantity
            piece_number = tokens[0]
            color = ' '.join(tokens[1:-1])  # Join color tokens
            quantity = int(tokens[-1])

            # Create or update the nested dictionary
            if piece_number not in inventory_data:
                inventory_data[piece_number] = {}
            inventory_data[piece_number][color.lower()] = quantity  # Convert color to lowercase

    return inventory_data


def calculate_total(piece_entry, color_entry, result_label, inventory_data):
    selected_piece = piece_entry.get()
    selected_color = color_entry.get()

    # Check if the selected_piece is a valid piece number
    if not selected_piece.isdigit():
        result_label.config(text=f"Invalid piece number: {selected_piece}", foreground="red")
        return

    # Convert the selected_piece to an integer
    selected_piece = int(selected_piece)

    # Construct the key without the "piece_" prefix
    key = f"{selected_piece}"

    if key in inventory_data:
        total = inventory_data[key].get(selected_color, 0)
    else:
        result_label.config(text=f"Piece {selected_piece} not found in inventory", foreground="red")
        return

    result_label.config(text=f"Total quantity of {selected_color} {selected_piece}: {total}", foreground="green")


def lookup_color_total(color_entry, result_label, inventory_data):
    selected_color = color_entry.get().lower()
    total = sum(piece_data.get(selected_color, 0) for piece_data in inventory_data.values())

    text_color = get_text_color(selected_color)
    result_label.config(text=f"Total quantity of {selected_color} for all pieces: {total}", foreground=text_color)


def lookup_all_totals(result_label, inventory_data):
    total_quantity = sum(sum(piece_data.values()) for piece_data in inventory_data.values())
    result_label.config(text=f"Total quantity of all pieces and colors: {total_quantity}", foreground="black")


def update_color_total(piece_entry, color_entry, new_value_entry, result_label, inventory_data, file_path):
    selected_piece = piece_entry.get()
    selected_color = color_entry.get().lower()
    new_value = int(new_value_entry.get())

    # Check if the selected_piece is a valid piece number
    if not selected_piece.isdigit():
        result_label.config(text=f"Invalid piece number: {selected_piece}", foreground="red")
        return

    # Convert the selected_piece to an integer
    selected_piece = int(selected_piece)

    # Construct the key without the "piece_" prefix
    key = f"{selected_piece}"

    # Update the total for the specified color for the given piece
    if key in inventory_data:
        inventory_data[key][selected_color] = new_value

        # Save the updated data to the file
        save_inventory_data(inventory_data, file_path)

        text_color = get_text_color(selected_color)
        result_label.config(text=f"Updated total quantity of {selected_color} for piece {selected_piece}: {new_value}", foreground=text_color)
    else:
        result_label.config(text=f"Piece {selected_piece} not found in inventory", foreground="red")


def save_inventory_data(inventory_data, file_path):
    with open(file_path, "w") as file:
        for piece_number, color_quantity in inventory_data.items():
            for color, quantity in color_quantity.items():
                file.write(f"{piece_number} {color} {quantity}\n")


def get_text_color(color):
    # Define color mappings based on user's input
    color_mappings = {
        "red": "red",
        "blue": "blue",
        # Add more color mappings as needed
    }

    # Default to black if the color is not found in mappings
    return color_mappings.get(color, "black")


def create_gui():
    window = tk.Tk()
    window.title("Inventory Calculator")
    window.geometry("400x400")  # Set window size

    # Create and place widgets with some styling
    style = ttk.Style()
    style.configure("TButton", padding=10, font=('Helvetica', 12))
    style.configure("TLabel", padding=5, font=('Helvetica', 12))

    piece_label = ttk.Label(window, text="Enter the piece number:")
    piece_label.pack(pady=10)

    piece_var = tk.StringVar()
    piece_entry = ttk.Entry(window, font=('Helvetica', 12), textvariable=piece_var)
    piece_entry.pack(pady=10)

    color_label = ttk.Label(window, text="Enter the color:")
    color_label.pack(pady=10)

    color_var = tk.StringVar()
    color_entry = ttk.Entry(window, font=('Helvetica', 12), textvariable=color_var)
    color_entry.pack(pady=10)

    new_value_label = ttk.Label(window, text="Enter the new value:")
    new_value_label.pack(pady=10)

    new_value_var = tk.StringVar()
    new_value_entry = ttk.Entry(window, font=('Helvetica', 12), textvariable=new_value_var)
    new_value_entry.pack(pady=10)

    result_label = ttk.Label(window, text="", font=('Helvetica', 12))
    result_label.pack(pady=10)

    calculate_button = ttk.Button(window, text="Calculate Total", command=lambda: calculate_total(piece_entry, color_entry, result_label, inventory_data))
    calculate_button.pack(pady=10)

    lookup_button = ttk.Button(window, text="Lookup Color Total", command=lambda: lookup_color_total(color_entry, result_label, inventory_data))
    lookup_button.pack(pady=10)

    update_button = ttk.Button(window, text="Update Color Total", command=lambda: update_color_total(piece_entry, color_entry, new_value_entry, result_label, inventory_data, file_path))
    update_button.pack(pady=10)

    lookup_all_button = ttk.Button(window, text="Lookup All Totals", command=lambda: lookup_all_totals(result_label, inventory_data))
    lookup_all_button.pack(pady=10)

    # Start the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    inventory_data = read_inventory_data(file_path)
    create_gui()
