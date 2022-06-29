def palindrome(s):
    st = "".join(s.lower().split())
    if st == st [::-1]:
        return "Палиндром"
    return "Непалиндром"


print(palindrome('А роза упала на лапу Азора'))