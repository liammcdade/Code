import csv
import re

file_path = "inventory_parts.csv"
output_file_path = "unique_part_nums.txt"

# Creating a set to store unique part numbers
unique_part_nums = set()

# Creating a CSV reader from the provided data
with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)

    # Assuming the first row contains headers
    headers = next(csv_reader)

    # Finding the index of the "part_num" column
    part_num_index = headers.index("part_num")

    # Extracting only the "part_num" column
    part_nums = [line[part_num_index] for line in csv_reader]

    # Filtering out values that contain letters and adding to the set
    unique_part_nums.update(num for num in part_nums if re.match(r'^\d+$', num))

# Writing the unique part numbers to a text file
with open(output_file_path, "w") as output_file:
    output_file.write("\n".join(unique_part_nums))

print(f"Unique part numbers without letters have been written to {output_file_path}")
