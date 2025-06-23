import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

# Load and parse CSV data
filename = 'sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            # Skip rows with missing data
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plotting functions
def plot_highs():
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.set_title("Daily High Temperatures - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def plot_lows():
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    ax.set_title("Daily Low Temperatures - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Menu loop
def main():
    print("Welcome to the Sitka Weather Viewer!")
    print("You can view high or low temperatures from 2018.")
    
    while True:
        print("\nMenu:")
        print("1 - View High Temperatures")
        print("2 - View Low Temperatures")
        print("3 - Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            plot_highs()
        elif choice == '2':
            plot_lows()
        elif choice == '3':
            print("Thanks for using the weather viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

# Run the main program
if __name__ == "__main__":
    main()
