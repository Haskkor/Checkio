##Vous recevez une expression contenant des nombres, parenthèses et opérateurs. Pour cette tâche, seulement les parenthèses importent. Elles viennent sous 3 formes: "{}" "()" or "[]". Elles sont utilisées pour déterminer le scope ou restreindre les expressions. Si une parenthèse est ouverte, elle doit être fermée avec une parenthèse de fermeture du même type. Le périmètre d'une parenthèse ne doit pas interférer avec une parenthèse d'un autre type. Dans cette mission,vous devez décider de la cohérence de l'expression suivant les parenthèses. Ne vous occupez pas des opérateurs et opérandes.
##
##Entrée: Une expression avec différents types de parenthèses en chaine de caractères(unicode).
##
##Résultat: une valeur de cohérence de l'expression en valeur booléenne(True or False).
##
##Example:
##
##checkio("((5+3)*2+1)") == True
##checkio("{[(3+1)+2]+}") == True
##checkio("(3+{1-1)}") == False
##checkio("[1+1]+(2*2)-{3/3}") == True
##checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
##checkio("2+3") == True
##
##Utilisation: Quand vous écrivez du code ou des expressions complexes dans un package mathématique, vous pouvez avoir un mal de tête intense quand il y a des erreurs de parenthèses. Ce concept peut-être utile pour votre IDE personnel.
##
##Precondition: 
##Il y a seulement des parenthèses ("{}" "()" or "[]"), nombres ou opérateurs ("+" "-" "*" "/").
##0 < len(expression) < 103

def count_brackets(expression):
    """ Check if brackets come in pairs. """
    if expression.count("(") == expression.count(")") and \
        expression.count("{") == expression.count("}") and \
        expression.count("[") == expression.count("]"):return True
    return False
    
def del_brackets(exp):
    """ Returns a string containing char between the first closing bracket and
    is opening bracket. """
    start,end = "",0
    for i in range(len(exp)):
        if exp[i] == ")" or exp[i] == "}" or exp[i] == "]":
            end = i
            break
    if exp[end] == ")":start = "("
    elif exp[end] == "}":start = "{"
    elif exp[end] == "]":start = "["
    for i in range(end,-1,-1):
        if exp[i] == start:return exp[i:end+1]
    return ""

def checkio(exp):
    while len(exp) > 1 and ("(" in exp or "{" in exp or "[" in exp):
        if len(del_brackets(exp)) < 1:return False
        else:exp = exp.replace(del_brackets(exp),"")
        if not count_brackets(exp):return False
    if not count_brackets(exp):return False
    return True    
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("{") == False, "Only one bracket"
