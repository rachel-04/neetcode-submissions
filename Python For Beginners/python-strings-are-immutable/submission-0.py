def remove_fourth_character(word: str) -> str:
    spliceString1 = word[:3]
    spliceString2 = word[4:]
    newString = spliceString1 +spliceString2
    return newString

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
