# pylint: disable=invalid-name
"""
word_count.py

This script processes a text file, identifies distinct words, and calculates their frequencies.
The results are printed on the screen and saved in a file named WordCountResults.txt.
"""

import time
import sys


def process_file(file_path):
    """
    Process the input file and count the frequency of each word.

    Parameters:
    - file_path (str): Path to the input file.

    Returns:
    - dict or None: A dictionary containing word frequencies, or None in case of an error.
    """
    # Dictionary to store word frequencies
    word_count = {}
    try:
        # Open the file and process each line
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split the line into words
                words = line.strip().split()
                for word in words:
                    # Remove punctuation and convert to lowercase
                    word = word.lower()

                    # Keep only alphanumeric characters
                    word = ''.join(char for char in word if char.isalnum())

                    # Check if the word is not empty
                    if word:
                        # Update word frequency in the dictionary
                        word_count[word] = word_count.get(word, 0) + 1
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:  # pylint: disable=broad-except
        # Handle general processing error
        print(f"Error processing file: {e}")
        return None
    return word_count


def write_results(word_count, elapsed_time, file_name):
    """
    Write word frequencies and elapsed time to WordCountResults.txt.

    Parameters:
    - word_count (dict): Dictionary containing word frequencies.
    - elapsed_time (float): Elapsed time for execution and data calculation.
    """
    with open(f"./CountWordsFiles/WordCount{file_name}Results.txt", 'w',
              encoding='utf-8') as result_file:
        result_file.write(f"Word\tCount of {file_name}\n")
        for word, frequency in word_count.items():
            result_file.write(f"{word}\t{frequency}\n")
        result_file.write(f"\nElapsed Time: {elapsed_time} seconds")


def main():
    """
    Main function to execute the word count program.

    Requirements:
    - Req 4: The name of the program shall be word_count.py
    - Req 5: The minimum format to invoke the program shall be as follows:
            python word_count.py fileWithData.txt
    - Req 6: The program shall manage files having from hundreds of items to thousands of items.
    - Req 7: The program should include at the end of the execution the time elapsed for the
            execution and calculus of the data.
            This number shall be included in the results file and on the screen.
    - Req 8: Be compliant with PEP8.
    """
    # Requirement 4: Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python word_count.py fileWithData.txt")
        sys.exit(1)

    # Requirement 7: Record the start time for calculating elapsed time
    start_time = time.time()

    # Requirement 5: Get the file path from command line arguments
    file_name = sys.argv[1]
    file_path = './CountWordsFiles/' + file_name + '.txt'

    # Requirement 3: Process the file, handle errors, and get word frequencies
    word_count = process_file(file_path)

    # Requirement 8: Check if the file processing was successful
    if word_count is not None:
        # Requirement 7: Calculate elapsed time
        elapsed_time = round(time.time() - start_time, 4)

        # Requirement 2: Print word frequencies on the screen
        print(f"Word\tCount of {file_name}")
        for word, frequency in word_count.items():
            print(f"{word}\t{frequency}")

        # Requirement 7: Print elapsed time on the screen
        print(f"\nElapsed Time: {elapsed_time} seconds")

        # Requirement 2: Write results to WordCountResults.txt
        write_results(word_count, elapsed_time, file_name)


# Requirement 6: Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
