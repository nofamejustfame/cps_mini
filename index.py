import time
import random
import matplotlib.pyplot as plt

def typing_test():
    phrases = [
       "Virat kohli is the best batsmen in the world.",
        "Life can put u in pickle just laugh through like its tickle.",
        "Believe in god's plan when your down.",
        "Python is a easy programming language.",
        "Will Artificial intelligence replace human in future? ."
    ]

    selected_phrase = random.choice(phrases)
    print("\nType the following phrase as fast as you can:")
    print(f"Phrase: \"{selected_phrase}\"")

    input("Press Enter to start...")
    start_time = time.time()
    user_input = input("\nYour input: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words = len(selected_phrase.split())
    speed = words / (elapsed_time / 60)  # Words per minute (WPM)

    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(user_input, selected_phrase) if a == b)
    accuracy = (correct_chars / len(selected_phrase)) * 100

    if user_input.strip() == selected_phrase.strip():
        print(f"\nGreat! Your typing speed is {speed:.2f} WPM with {accuracy:.2f}% accuracy.")
    else:
        print(f"\nYou made a mistake. Your typing speed is {speed:.2f} WPM with {accuracy:.2f}% accuracy.")

    return speed, accuracy

def plot_chart(speeds, accuracies):
    print("\nChoose a chart type:")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Pie Chart")
    chart_type = int(input("Enter the number of your choice: "))

    if chart_type == 1:
        x = range(1, len(speeds) + 1)
        plt.bar(x, speeds, color='blue', label='Speed (WPM)')
        plt.bar(x, accuracies, color='orange', alpha=0.7, label='Accuracy (%)')
        plt.title("Typing Speed and Accuracy - Bar Chart")
        plt.xlabel("Test Number")
        plt.ylabel("Value")
        plt.legend()  # Adding legend
    elif chart_type == 2:
        x = range(1, len(speeds) + 1)
        plt.plot(x, speeds, marker='o', color='blue', label='Speed (WPM)')
        plt.plot(x, accuracies, marker='s', color='orange', label='Accuracy (%)')
        plt.title("Typing Speed and Accuracy - Line Chart")
        plt.xlabel("Test Number")
        plt.ylabel("Value")
        plt.legend()  # Adding legend
    elif chart_type == 3:
        total_speed = sum(speeds)
        total_accuracy = sum(accuracies)
        labels = ['Speed (WPM)', 'Accuracy (%)']
        values = [total_speed, total_accuracy]
        colors = ['blue', 'orange']
        plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors)
        plt.title("Typing Speed and Accuracy - Pie Chart")
        plt.legend(labels, title="Metrics", loc="center left", bbox_to_anchor=(1, 0.5))
    else:
        print("Invalid choice. Please run the script again.")
        return

    plt.tight_layout()
    plt.show()

def main():
    print("Welcome to the Speed Typing Test!")
    speeds = []
    accuracies = []

    while True:
        speed, accuracy = typing_test()
        speeds.append(speed)
        accuracies.append(accuracy)

        cont = input("\nDo you want to take another test? (yes/no): ").strip().lower()
        if cont != 'y':
            break

    print("\nResults Summary:")
    for i, (speed, accuracy) in enumerate(zip(speeds, accuracies), start=1):
        print(f"Test {i}: Speed = {speed:.2f} WPM, Accuracy = {accuracy:.2f}%")

    plot_chart(speeds, accuracies)
    print("Thank you for participating in the typing test!")

if _name_ == "_main_":
    main()
