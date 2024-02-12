# def duplicate_encode(word):
#     word = list(word)
#     cache = []
#     output = ""
#     for x in word:
#         if x not in cache:
#             cache.append(x)
#             output += "("
#         else:
#             output += ")"
        
#     return output



# word = "Success"
# wyniki = duplicate_encode(word)
# print(wyniki)



def duplicate_encode(word):
    word = word.lower()
    result = ''

    for char in word:
        if word.count(char) > 1:
            result += ')'
        else:
            result += '('

    return result



# # print(duplicate_encode("Success"))
#  The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
# Examples

# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

# Notes

# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!



# def zlicz_litery(slowo):
#     slowo = slowo.lower()
#     unikalne_litery = set(slowo)

#     wyniki = ', '.join([f'{litera}:{slowo.count(litera)}' for litera in unikalne_litery])

#     sloro = list(slowo)
#     cache = []
#     for x in word:
#         pass
#     return wyniki


# slowo = "Success"
# wyniki = zlicz_litery(slowo)
# print(wyniki)

