# pylint: disable=invalid-name
"""
convertNumbers.py

This script converts numbers from a file to binary and hexadecimal bases.
The results are printed on the screen and saved in a file named ConvertionResults.txt.
"""

import time
import sys

# Constants
FORMAT_STRING = 'Decimal: {dec} | Binary: {bin} | Hexadecimal: {hex}'


def read_file(file_path):
    """
    Read and parse the file containing numbers.

    Parameters:
    - file_path (str): Path to the input file.

    Returns:
    - list or None: List of numbers or None in case of an error.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            numbers = []
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Error: Invalid data in the file. {line}")
                    continue
        return numbers
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError as ve:
        print(f"Error: Invalid data in the file. {ve}")
        return None
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error reading file: {e}")
        return None


def convert_numbers(numbers):
    """
    Convert numbers to binary and hexadecimal bases.

    Parameters:
    - numbers (list): List of numbers.

    Returns:
    - dict or None: Dictionary containing original numbers, binary, and hexadecimal representations,
                   or None if conversion is not possible.
    """

    try:
        conversion_results = []

        for number in numbers:
            # Convert to binary and hexadecimal without using libraries
            binary_representation = bin(int(number))[2:]
            hexadecimal_representation = hex(int(number))[2:].upper()

            conversion_results.append(FORMAT_STRING.format(dec=number,
                                                           bin=binary_representation,
                                                           hex=hexadecimal_representation))
        return conversion_results
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error converting numbers: {e}")
        return None


def write_results(conversion_results, elapsed_time, file_name):
    """
    Write conversion results and elapsed time to ConvertionResults.txt.

    Parameters:
    - conversion_results (dict): Dictionary containing original numbers, binary, and
                                 hexadecimal representations.
    - elapsed_time (float): Elapsed time for execution and data calculation.
    """
    with open(f"./ConvertNumbersFiles/Convertion{file_name}Results.txt", 'w',
              encoding='utf-8') as result_file:
        result_file.write("Conversion Results\n")
        for conversion_string in conversion_results:
            result_file.write(conversion_string)
        result_file.write(f"\nElapsed Time: {elapsed_time} seconds")


def main():
    """
    Main function to execute the number conversion program.

    Requirements:
    - Req 4: The name of the program shall be convertNumbers.py
    - Req 5: The minimum format to invoke the program shall be as follows:
            python convertNumbers.py fileWithData.txt
    - Req 6: The program shall manage files having from hundreds of items to thousands of items.
    - Req 7: The program should include at the end of the execution the time elapsed for
            the execution and calculus of the data. This number shall be included in the
            results file and on the screen.
    - Req 8: Be compliant with PEP8.
    """
    # Requirement 4: Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    # Requirement 7: Record the start time for calculating elapsed time
    start_time = time.time()

    # Requirement 5: Get the file path from command line arguments
    file_name = sys.argv[1]
    file_path = './ConvertNumbersFiles/' + file_name + '.txt'

    # Requirement 3: Read and parse the file, handle errors
    numbers = read_file(file_path)

    # Requirement 8: Check if file reading was successful
    if numbers is not None:
        # Requirement 6: Convert numbers to binary and hexadecimal
        conversion_results = convert_numbers(numbers)

        # Requirement 8: Check if conversion was successful
        if conversion_results is not None:
            # Requirement 7: Calculate elapsed time
            elapsed_time = round(time.time() - start_time, 4)

            # Requirement 2: Print conversion results on the screen
            print("Conversion Results")
            for conversion_string in conversion_results:
                print(conversion_string)

            # Requirement 7: Print elapsed time on the screen
            print(f"\nElapsed Time: {elapsed_time} seconds")

            # Requirement 2: Write results to ConvertionResults.txt
            write_results(conversion_results, elapsed_time, file_name)


# Requirement 6: Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
