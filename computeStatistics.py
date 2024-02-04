# pylint: disable=invalid-name
"""
computeStatistics.py

This script computes descriptive statistics (mean, median, mode, standard deviation, variance)
from a file containing numbers. The results are printed on the screen and saved in a file
named StatisticsResults.txt.
"""

import time
import sys


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


def compute_statistics(numbers):
    """
    Compute descriptive statistics.

    Parameters:
    - numbers (list): List of numbers.

    Returns:
    - dict or None: Dictionary containing mean, median, mode, standard deviation, and variance,
                   or None if computation is not possible.
    """
    try:
        # Amount of values
        count = len(numbers)

        # Mean calculation
        mean = sum(numbers) / len(numbers)

        # Median calculation
        sorted_numbers = sorted(numbers)
        middle = len(sorted_numbers) // 2
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2 \
            if len(sorted_numbers) % 2 == 0 \
            else sorted_numbers[middle]

        # Mode calculation
        frequency_dict = {number: numbers.count(number) for number in set(numbers)}
        mode = max(frequency_dict, key=frequency_dict.get)

        # Standard deviation calculation
        squared_diff = [(num - mean) ** 2 for num in numbers]
        variance = sum(squared_diff) / len(numbers)
        std_deviation = variance ** 0.5  # Square root without using math library

        return {
            'Count': count,
            'Mean': mean,
            'Median': median,
            'Mode': mode,
            'Standard Deviation': std_deviation,
            'Variance': variance
        }
    except ZeroDivisionError:
        print("Error: Cannot compute statistics with an empty list of numbers.")
        return None
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error computing statistics: {e}")
        return None


def write_results(statistics, elapsed_time, file_name):
    """
    Write computed statistics and elapsed time to StatisticsResults.txt.

    Parameters:
    - statistics (dict): Dictionary containing descriptive statistics.
    - elapsed_time (float): Elapsed time for execution and data calculation.
    """
    with open(f"./ComputeStatisticsFiles/Statistics{file_name}Results.txt", 'w',
              encoding='utf-8') as result_file:
        result_file.write("Descriptive Statistics\n")
        for stat_name, stat_value in statistics.items():
            result_file.write(f"{stat_name}: {stat_value}\n")
        result_file.write(f"\nElapsed Time: {elapsed_time} seconds")


def main():
    """
    Main function to execute the statistics computation program.

    Requirements:
    - Req 4: The name of the program shall be computeStatistics.py
    - Req 5: The minimum format to invoke the program shall be as follows:
            python computeStatistics.py fileWithData.txt
    - Req 6: The program shall manage files having from hundreds of items to thousands of items.
    - Req 7: The program should include at the end of the execution the time elapsed for
            the execution and calculus of the data. This number shall be included in the
            results file and on the screen.
    - Req 8: Be compliant with PEP8.
    """
    # Requirement 4: Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    # Requirement 7: Record the start time for calculating elapsed time
    start_time = time.time()

    # Requirement 5: Get the file path from command line arguments
    file_name = sys.argv[1]
    file_path = './ComputeStatisticsFiles/' + sys.argv[1] + '.txt'

    # Requirement 3: Read and parse the file, handle errors
    numbers = read_file(file_path)

    # Requirement 8: Check if file reading was successful
    if numbers is not None:
        # Requirement 6: Compute descriptive statistics
        statistics = compute_statistics(numbers)

        # Requirement 8: Check if computation was successful
        if statistics is not None:
            # Requirement 7: Calculate elapsed time
            elapsed_time = round(time.time() - start_time, 5)

            # Requirement 2: Print computed statistics on the screen
            print("Descriptive Statistics")
            for stat_name, stat_value in statistics.items():
                print(f"{stat_name}: {stat_value}")

            # Requirement 7: Print elapsed time on the screen
            print(f"\nElapsed Time: {elapsed_time} seconds")

            # Requirement 2: Write results to StatisticsResults.txt
            write_results(statistics, elapsed_time, file_name)


# Requirement 6: Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
