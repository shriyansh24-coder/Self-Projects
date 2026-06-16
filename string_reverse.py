def rev(str):
    rev_str = ""
    for char in str:
        rev_str = char + rev_str
    return rev_str
print(rev("hello"))