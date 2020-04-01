import csv

from translate import translate


def test(race):
    failures = []
    total = 0
    with open(f'test_data/{race}_words.csv', 'r', newline='') as f:
        data = csv.reader(f)
        for row in data:
            word = row[1]
            word_capitalized = word.capitalize()
            # Compare the lower case words.
            expected_trans_lower = row[2]
            trans_lower = translate(word, race)
            if trans_lower != expected_trans_lower:
                failures.append(f'{word}: {trans_lower} - '
                                f'({expected_trans_lower})')
            total += 1
            # Compare the capitalized words.
            if len(row) >= 4:
                expected_trans_capitalized = row[3]
                trans_capitalized = translate(word_capitalized, race)
                if trans_capitalized != expected_trans_capitalized:
                    failures.append(f'{word_capitalized}: '
                                    f'{trans_capitalized} - '
                                    f'({expected_trans_capitalized})')
            total += 1
            if len(row) == 5:
                word_uppercase = word.upper()
                expected_trans_uppercase = row[4]
                trans_uppercase = translate(word_uppercase, race)
                if trans_uppercase != expected_trans_uppercase:
                    failures.append(f'{word_uppercase}: {trans_uppercase} - '
                                    f'({expected_trans_uppercase})')
                total += 1
    print(f'Results: {len(failures)}/{total}')
    with open(f'test_results_{race}.txt', 'w') as f:
        f.write('\n'.join(failures))


if __name__ == "__main__":
    test('explorers')
    test('warriors')
    test('traders')
