# NLP-Calculation-of-the-Minimum-Edit-Distance

Write a code to achieve the following tasks:

Calculate the minimum edit distance to transform the word “INTENTION” to “EXECUTION” using Levenshtein table.

The algorithm fills in the table by considering three possible operations at each position:
1.	Deletion: D(i-1, j) + 1
2.	Insertion: D(i, j-1) + 1
3.	Substitution: D(i-1, j-1) + 2 if X(i) ≠ Y(j), else 0

![image](https://github.com/SuyashShetty16/NLP-Calculation-of-the-Minimum-Edit-Distance/assets/84004378/dfdc3562-b3ee-4c5a-94ba-3ea94aa3e813)
