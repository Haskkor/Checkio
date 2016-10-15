##En informatique et en mathématiques discrètes, une inversion est un couple d'endroits dans une séquence où les éléments à ces endroits ne suivent pas leur ordre naturel. Ainsi, si nous utilisons l'ordre croissant pour trier un groupe de nombres, une inversion se produit quand, dans une séquence donnée, des nombres plus grands apparaissent devant des nombres plus petits.
##
##Regardez par exemple cette séquence (1, 2, 5, 3, 4, 7, 6) ; nous pouvons voir qu'il y a ici trois inversions :
##- 5 et 3 ; - 5 et 4 ; - 7 et 6.
##
##On vous donne une séquence de nombres uniques et vous devez compter le nombre d'inversions dans cette séquence.
##
##Entrée : Une séquence en tant que tuple d'entiers.
##
##Sortie : Le nombre d'inversions en tant qu'entier.

def count_inversion(sequence):
    count = 0
    for i in range(len(sequence)-1):
        for j in range(i+1,len(sequence)):
            if sequence[i] > sequence[j]:
                count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
