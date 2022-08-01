#   swap the case of the given character

#  using in-built method
def swap(char):
    if char.islower():
        return char.upper()
    elif char.isupper():
        return char.lower()

print(swap('a'))    #    A

#  without using in-built method
def swap_case(char):
    if ord("a") <= ord(char) <= ord("z"):
        print(chr(ord(char) - 32))
    elif ord("A") <= ord(char) <= ord("Z"):
        print(chr(ord(char) + 32))

swap_case("D")      #    d
