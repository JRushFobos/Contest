def letter_combinations(digits, dictionary, current='', combinations=[]):
    if len(digits) == 0:
        combinations.append(current)
    else:
        for letter in dictionary[digits[0]]:
            letter_combinations(
                digits[1:], dictionary, current + letter, combinations
            )
    return combinations


dictionary = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

digits = input()

combinations = letter_combinations(digits, dictionary)

print(' '.join(combinations))
