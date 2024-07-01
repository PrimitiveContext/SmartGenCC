import csv
import os
import sys
from tqdm import tqdm

# Function to calculate the Luhn checksum
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

# Function to generate a valid Luhn number sequentially
def generate_luhn_number(bin_value, length, start):
    while True:
        number = bin_value + str(start).zfill(length - len(bin_value) - 1)
        checksum = luhn_checksum(int(number) * 10)
        luhn_digit = (10 - checksum) % 10
        valid_number = number + str(luhn_digit)
        if luhn_checksum(int(valid_number)) == 0:
            return valid_number
        start += 1

# Function to display help information
def display_help():
    print("Usage: python script.py <bin_value_or_file> [--batch <batch_size>]")
    print()
    print("    <bin_value_or_file>")
    print("        Example: '372395*********'   (American Express: 15 digits total)")
    print("        Example: '423456**********'  (other cards: 16 digits total)")
    print("        Example: 'bin_values.txt'    (text file with multiple wildcard BINs)")
    print()
    print("    --batch, -b")
    print("    Max number of CC numbers per CSV (default is 100,000)")
    print()
    
# Function to process a single BIN value
def process_bin_value(bin_value, batch_size):
    num_asterisks = bin_value.count('*')
    bin_digits = bin_value.replace('*', '')
    total_length = len(bin_value)

    # Validate total length
    if total_length not in [15, 16]:
        print(f"Invalid total length for BIN {bin_value}. Skipping...")
        return

    directory = "cc_numbers"

    # Create the directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    total_possible_numbers = 10 ** num_asterisks
    total_batches = (total_possible_numbers + batch_size - 1) // batch_size  # Calculate the total number of batches

    file_counter = 0
    current_number = 0

    with tqdm(total=total_batches, desc=f"Generating CSVs for BIN {bin_value}", unit="csv") as pbar:
        while current_number < total_possible_numbers:
            remaining_numbers = total_possible_numbers - current_number
            current_batch_size = min(batch_size, remaining_numbers)
            generated_numbers = []

            for _ in range(current_batch_size):
                valid_number = generate_luhn_number(bin_digits, total_length, current_number)
                generated_numbers.append(valid_number)
                current_number += 1

            file_index = file_counter + 1
            csv_path = os.path.join(directory, f"{bin_digits}_{file_index}.csv")
            with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for number in generated_numbers:
                    writer.writerow([number])

            file_counter += 1
            pbar.update(1)

    print(f'Generated card numbers for BIN {bin_value} are written to directory: {directory}')

# Function to read BIN values from a file
def read_bin_values_from_file(file_path):
    bin_values = []
    if file_path.endswith('.csv'):
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and '*' in row[0]:
                    bin_values.append(row[0])
    elif file_path.endswith('.txt'):
        with open(file_path, mode='r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if '*' in line:
                    bin_values.append(line)
    else:
        print("Unsupported file format. Please provide a txt or csv file.")
    return bin_values

# Entry point of the script
if __name__ == "__main__":
    bin_value = None
    batch_size = 100000  # Default batch size

    if '--help' in sys.argv or '-h' in sys.argv:
        display_help()
    else:
        if '-b' in sys.argv or '--batch' in sys.argv:
            batch_index = sys.argv.index('-b') + 1 if '-b' in sys.argv else sys.argv.index('--batch') + 1
            if batch_index < len(sys.argv):
                batch_size = int(sys.argv[batch_index])
        if len(sys.argv) >= 2:
            bin_value_or_file = sys.argv[1]
            if os.path.isfile(bin_value_or_file):
                bin_values = read_bin_values_from_file(bin_value_or_file)
                for bin_value in bin_values:
                    process_bin_value(bin_value, batch_size)
            else:
                bin_value = bin_value_or_file
                process_bin_value(bin_value, batch_size)
        else:
            display_help()
