#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_WORDS 100
#define MAX_WORD_LENGTH 50

// Simple structure to hold word and its next word
typedef struct {
    char word[MAX_WORD_LENGTH];
    char next[MAX_WORD_LENGTH];
} Bigram;

Bigram bigrams[] = {
    {"Hello", "are"},
    {"Hello", "is"},
    {"how", "are"},
    {"how", "is"},
    {"are", "you"},
    {"is", "it"},
    {"", ""} // End of list marker
};

char* predict_next_word(const char* input) {
    for (int i = 0; strcmp(bigrams[i].word, "") != 0; i++) {
        if (strcmp(bigrams[i].word, input) == 0) {
            return bigrams[i].next;
        }
    }
    return "unknown"; // If no match found
}

int main() {
    char input[2 * MAX_WORD_LENGTH];
    printf("Enter two words: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0; // Remove trailing newline

    char* words[2];
    char* token = strtok(input, " ");
    int i = 0;
    while (token != NULL && i < 2) {
        words[i++] = token;
        token = strtok(NULL, " ");
    }

    if (i == 2) {
        char* next1 = predict_next_word(words[1]);
        char* next2 = predict_next_word(next1);
        printf("Next two predicted words: %s %s\n", next1, next2);
    } else {
        printf("Please enter exactly two words.\n");
    }

    return 0;
}
