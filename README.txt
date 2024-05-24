This program takes in a dataset of DNA sequences (DNA_sequences.txt) and a single query sequence (DNA_query.txt) then determines which sequences are most similar to the query sequence. The user can choose one of 4 algorithms to use for this analysis.

Here are the 4 algorithms:
1) Longest Common Substring : finds the longest substring shared between the 2 sequences
2) Longest Common Subsequence (LCS) : finds the longest match between 2 sequences (matches do not have to be contiguous)
3) Edit Distance : finds the minimum number of operations (insertion, deletion, substitution) needed to transform 1 sequence into another
4) Needleman-Wunsch : assigns scores to every possible alignment (match, mismatch, indel = insertion or deletion) of the characters in the sequences and finds the scenario with the highest score which represents the optimal alignment. Our program asks the user for their desire gap score as that accounts for insertion/deletion within the sequence.

For the Edit Distance algorithm, a lower score is better since that means it takes fewer operations to transform a sequence into another one. A higher score is better for the other algorithms.

Instructions to run the program:
1) Click the run button
2) Enter the names of the query and sequences datasets
3) Choose an algorithm to use
4) Read the analysis
5) Decide whether to quit or continue using the program
