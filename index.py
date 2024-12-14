import random
import time

def get_random_sentence():
    sentences = [
        "Virat kohli is the best batsmen in the world.",
        "Life can put u in pickle just laugh through like its tickle.",
        "Believe in god's plan when your down.",
        "Python is a easy programming language.",
        "Will Artificial intelligence replace human in future? ."
    ]
    return random.choice(sentences)

def typing_test():
    print("Welcome to the Speed Typing Test!")
    print("You will be given a random sentence to type as quickly and accurately as possible.")
    input("Press Enter to start...")
    
    sentence = get_random_sentence()
    print("\nType the following sentence:")
    print(sentence)

    
    start_time = time.time()
    user_input = input("\nYour input: ")
    end_time = time.time()

    time_taken = end_time - start_time

    correct = sum(1 for a, b in zip(sentence, user_input) if a == b)
    accuracy = (correct / len(sentence)) * 100

    print("\nResults:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

    words = len(user_input.split())
    wpm = (words / time_taken) * 60
    print(f"Words per minute (WPM): {wpm:.2f}")

if __name__ == "__main__":
    typing_test()
