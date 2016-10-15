##"Pendant des siècles, les gauchers ont souffert d'une discrimination injuste dans un monde adapté pour des droitiers." 
##Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.
##"La plupart des Hommes (disons entre 70% et 95%) sont droitiers ; une minorité (disons entre 5% et 30%) sont gauchers, et un nombre indéterminé de personnes sont probablement mieux décrits en tant qu'ambidextres." 
##Scientific American. www.scientificamerican.com
##On a donné une tâche simple à un de nos robots: assembler une séquence de chaines de caractères pour produire des instructions sur la manière de contourner le vaisseau. Mais ce robot est gaucher et a tendance à faire des blagues à ce sujet pour embrouiller ses amis droitiers.
##
##On vous donne une séquence de chaines de caractères. Vous devez assembler ces chaines de caractères en une seule, avec une virgule entre chacune d'entre elles. Pour faire une blague aux robots droitiers, vous devez remplacer toutes les occurences du mot "right" par le mot "left", même si celles-ci font partie d'un autre mot. Toutes les chaines de caractères sont données en minuscule.
##
##Entrée : Une séquence (un tuple) de chaines de caractères (unicode).
##
##Sortie : Le texte en tant que chaine de caractères.

def left_join(phrases):
    chaine = ""
    for i in range(len(phrases)):
        temp = phrases[i]
        if "right" in temp:
            temp = temp.replace("right","left")
        chaine += temp
        if i < len(phrases) - 1:
            chaine += ","
    return chaine

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
