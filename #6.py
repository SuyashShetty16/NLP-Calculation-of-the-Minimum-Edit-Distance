def min_edit_distance(word1, word2):
    len_word1 = len(word1)
    len_word2 = len(word2)

    # Initialize the Levenshtein table with zeros
    table = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]

    # Fill in the base cases
    for i in range(len_word1 + 1):
        table[i][0] = i
    for j in range(len_word2 + 1):
        table[0][j] = j

    # Fill in the rest of the table
    for i in range(1, len_word1 + 1):
        for j in range(1, len_word2 + 1):
            cost = 2 if word1[i - 1] != word2[j - 1] else 0
            table[i][j] = min(table[i - 1][j] + 1,       # Deletion
                              table[i][j - 1] + 1,       # Insertion
                              table[i - 1][j - 1] + cost) # Substitution

    return table, table[-1][-1]

def display_table(word1, word2, table):
    # Display the table with words as row and column headers
    header = ["#"] + list(word2)
    print(f"{' ' * 4}{' '.join(header)}")
    for i in range(len(table)):
        if i == 0:
            row = ['#']
        else:
            row = [word1[i - 1]]
        row += [f"{cell:^4}" for cell in table[i]]
        print(f"{row[0]:^4}{' '.join(row[1:])}")

if __name__ == "__main__":
    word1 = "INTENTION"
    word2 = "EXECUTION"

    levenshtein_table, min_distance = min_edit_distance(word1, word2)

    display_table(word1, word2, levenshtein_table)

    print("\nMinimum Edit Distance:", min_distance)

