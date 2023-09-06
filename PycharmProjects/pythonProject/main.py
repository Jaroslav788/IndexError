def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count


user_input = input("Введіть рядок: ")
result = count_vowels(user_input)
print("Кількість голосних у рядку:", result)
















