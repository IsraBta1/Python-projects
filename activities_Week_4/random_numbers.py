import random
words = ["hello", "world", "python", "big", "baby"]
def main():
    numbers = [16.2, 75.1, 52.3]
    word_list = []
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)

    append_random_words(word_list)
    print(word_list)
    append_random_words(word_list, 4)
    print(word_list)

def append_random_words(word_list, quantity=1):
    for _ in range(quantity):
        word_list.append(random.choice(words))

def append_random_numbers(nun_list, quantity=1):
    for _ in range(quantity):
        nun = random.uniform(0, 100)
        nun = round(nun, 1)
        nun_list.append(nun)

if __name__ == "__main__":   
    main()