# DSA Problems

A curated collection of small Data Structures & Algorithms (DSA) practice problems implemented in this repository. Each problem is intended for learning fundamentals (control flow, loops, recursion, basic algorithms) and can be used as exercises or interview prep.

## How to use

- Browse the folder for a problem you want to practice.
- Open the corresponding script in your editor (VS Code).
- Run with Python 3: `python3 <filename>.py`
- Add tests or rewrite solutions to improve efficiency and readability.

## Problems (continuous numbering)

Day1 Topics: Numbers

1. Even or Odd
2. Leap Year Checker
3. Credit Card Issuer
4. Print digits in a number
5. Sum of digits in a number
6. Sum of even and odd numbers (Assignment)
7. Sum of prime digits
8. Sum of multiples of 3 (Assignment)
9. Count the digits in a number
10. Count the number of times a given digit occurs (Assignment)
11. Check for Duck Number
12. Reverse a number
13. Palindrome or not
14. Palindrome (alternate method)
15. Integer to binary
16. Integer to binary (alternate method)
17. Fibonacci series
18. Recursion fundamentals
19. Fibonacci using recursion
20. Niven Number
21. Special Number
22. Print prime numbers
23. Perfect number check
24. Armstrong number check
25. All special two-digit numbers (Assignment)

## Phase 1 — Basic String Manipulation & Hashing (Easy → Medium)

26. Fizz Buzz

- Problem: Given an integer n, return a 1-indexed string array answer where:
  - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
  - answer[i] == "Fizz" if i is divisible by 3.
  - answer[i] == "Buzz" if i is divisible by 5.
  - answer[i] == i (as a string) otherwise.
- Input: n = 5
- Output: ["1","2","Fizz","4","Buzz"]

27. Valid Anagram

- Problem: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
- Input: s = "anagram", t = "nagaram"
- Output: true

28. Group Anagrams

- Problem: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
- Input: strs = ["eat","tea","tan","ate","nat","bat"]
- Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## Phase 2 — Two Pointers Pattern (Easy → Medium)

29. Valid Palindrome

- Problem: Given a string s, return true if it reads the same forward and backward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.
- Input: s = "A man, a plan, a canal: Panama"
- Output: true

30. Longest Common Prefix

- Problem: Find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
- Input: strs = ["flower","flow","flight"]
- Output: "fl"

31. Longest Palindromic Substring

- Problem: Given a string s, return the longest palindromic substring in s.
- Input: s = "babad"
- Output: "bab" (Note: "aba" is also a valid answer)

32. Palindromic Substrings

- Problem: Return the total count of palindromic substrings in a string s.
- Input: s = "aaa"
- Output: 6

## Phase 3 — Sliding Window Pattern (Medium → Hard)

Focus: tracking a dynamic window using left/right pointers; all sliding-window related problems grouped here and numbered continuously.

33. Longest Substring Without Repeating Characters

- Problem: Given a string s, find the length of the longest substring without repeating characters.
- Input: s = "abcabcbb"
- Output: 3

34. Longest Repeating Character Replacement

- Problem: Given a string s and an integer k, you can change any character to any other uppercase English character at most k times. Return the length of the longest substring containing the same letter.
- Input: s = "AABABBA", k = 1
- Output: 4

35. Minimum Window Substring

- Problem: Given strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included. If no such window exists, return "".
- Input: s = "ADOBECODEBANC", t = "ABC"
- Output: "BANC"

36. Maximum Sum Subarray of Size K

- Question: Find the maximum sum of any contiguous subarray of size K.
- Input: arr = [2, 1, 5, 1, 3, 2], K = 3
- Output: 9

37. Smallest Subarray with Given Sum

- Question: Find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
- Input: arr = [2, 1, 5, 2, 3, 2], S = 7
- Output: 2

38. Maximum Number of Vowels in a Substring of Size K

- Question: Find the maximum number of vowels in any substring of length K.
- Input: s = "abciiidef", K = 3
- Output: 3

39. Longest Subarray with Sum Less Than or Equal to K

- Question: Find the length of the longest contiguous subarray whose sum is less than or equal to K.
- Input: arr = [1, 2, 1, 0, 1, 1, 0], K = 4
- Output: 5

## Phase 4 — Linear Data Structures (Stacks & Linked Lists)

40. Valid Parentheses

- Problem: Given a string s containing just '(', ')', '{', '}', '[', ']', determine if the input string is structurally valid.
- Input: s = "()[]{}"
- Output: true

41. Palindrome Linked List

- Problem: Given the head of a singly linked list, return true if it is a palindrome.
- Input: head = [1,2,2,1]
- Output: true

## Phase 5 — Advanced String Design & Backtracking

42. Encode and Decode Strings

- Problem: Design an algorithm to serialize a list of strings into a single string, and deserialize it back to the original list.
- Input List: ["neet","code","love","you"]
- Intermediate Encoded String: "4#neet4#code4#love3#you"
- Final Output Decoded List: ["neet","code","love","you"]

43. Letter Combinations of a Phone Number

- Problem: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent based on classic phone keypad mapping.
- Input: digits = "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

44. Text Justification

- Problem: Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully left-and-right justified.
- Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
- Output:
  [
  "This is an",
  "example of text",
  "justification. "
  ]

---

## Contributing

- Follow PEP 8 for style (use a formatter like Black or autopep8).
- Add a short description and example usage to any new problem file.
- Open a PR with clear intent and tests where applicable.

## Notes

- Prefer descriptive filenames and avoid naming scripts that shadow Python standard libraries (for example, don't name a file `collections.py`).
- Include error handling for edge cases (e.g.,
