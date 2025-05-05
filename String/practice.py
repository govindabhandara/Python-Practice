def are_anagram(s1,s2):
    return sorted(s1.lower())==sorted(s2.lower())
print(are_anagram("listen","silent"))