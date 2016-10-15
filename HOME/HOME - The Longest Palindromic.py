##Il s'agit d'écrire une fonction qui trouve la plus longue sous-chaîne qui soit un palindrome dans une chaîne de caractères. Votre code doit être le plus efficace possible !
##
##Si vous trouvez plus d'une sous-chaîne, il faut retourner celle qui est plus proche du début.
##
##Input: Un texte - chaîne de carcatères (string).
##
##Output: La plus longue sous-chaîne qui soit un palindrome.
##
##Précondition: 1 < |text| ≤ 20
##Le texte ne contient que des carcatères ASCII.

def get_substrings(str):
  return [str[i:j+1] for i in range(len(str)) for j in range(i,len(str))]
​
def get_palindomes(texts):
    palindromes = []
    for text in texts:
        palin = True
        for i in range(len(text)//2):
            if text[i] != text[-(i+1)]:
                palin = False
        if palin:palindromes.append(text)
    return palindromes
​
def longest_palindromic(text):
    palindromes = get_palindomes(get_substrings(text))
    longest_palindrome = palindromes[0]
    for palindrome in palindromes:
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
    return longest_palindrome
​
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
