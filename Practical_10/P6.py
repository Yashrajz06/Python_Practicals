import matplotlib.pyplot as plt


def char_frequency_histogram(text):
    # Create a dictionary to store character frequencies
    freq_dict = {}

    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Print the dictionary
    print("Character Frequency Dictionary:")
    for char, freq in freq_dict.items():
        print(f"'{char}': {freq}")

    # Print histogram
    print("\nHistogram:")
    for char, freq in freq_dict.items():
        print(f"{char}: {'#' * freq}")

    # Plot the histogram using matplotlib
    plt.figure(figsize=(10, 5))
    plt.bar(freq_dict.keys(), freq_dict.values(), color='skyblue')
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.title("Character Frequency Histogram")
    plt.show()


# Read input from user
text = input("Enter a string: ")
char_frequency_histogram(text)
