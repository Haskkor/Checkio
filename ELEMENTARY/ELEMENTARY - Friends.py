##Pour cette mission "How to find friends" , c'est pratique d'avoir accès à une structure spécialement crée pour cela. Dans cette mission nous réaliserons une structure de données que nous utiliserons pour stocker et travailler avec un réseau d'amis.
##
##La classe "Friends" contiendra des noms et les relations entre eux. Les noms sont représentés par des chaines de caractères prenant en compte les majuscules. Les relations sont réciproques, c'est à dire que si "sophia" est liée à "nikola", l'inverse est également valide.
##
##class Friends(relations)
##
##Résulte en une nouvelle instance de "Friends". "relations" est un "sets" itérable comprenant deux éléments dans chaque itération. Chaque relation contient deux noms sous la forme de chaine de caractères. Les relations peuvent être répétées dans les données initiales, mais ne sont stockées qu'une seule fois. chaque relation a seulement deux valeurs - existante ou pas.
##
##>>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
##>>> Friends([{"1", "2"}, {"3", "1"}])
##
##add(relation)
##
##Ajoute une relation dans une instance. "relation" est un "set" de deux noms (chaine de caractères). Résulte en "True" si la relation est nouvelle. Résulte en "False" si cette relation existe déjà.
##
##>>> f = Friends([{"1", "2"}, {"3", "1"}])
##>>> f.add({"1", "3"})
##False
##>>> f.add({"4", "5"})
##True
##
##remove(relation)
##
##supprime une relation de l'instance. "relation" est un "sets" de deux noms (chaine de caractères). Résulte en "True" si la relation existe. Résulte en "False" si la relation n'existe pas dans l'instance.
##
##>>> f = Friends([{"1", "2"}, {"3", "1"}])
##>>> f.remove({"1", "3"})
##True
##>>> f.remove({"4", "5"})
##False
##
##names()
##
##Résulte en un "sets" de noms. Le "set" contient seulement les noms reliés avec quelqu'un.
##
##>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
##>>> f.names()
##{"a", "b", "c", "d"}
##>>> f.remove({"d", "c"})
##True
##>>> f.names()
##{"a", "b", "c"}
##
##connected(name)
##
##Résulte en un "set" de noms qui sont liés avec le nom en paramètre "name". Si "name" n'existe pas dans l'instance, la fonction résulte en un "set" vide.
##
##>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
##>>> f.connected("a")
##{"b", "c"}
##>>> f.connected("d")
##set()
##>>> f.remove({"c", "a"})
##True
##>>> f.connected("c")
##{"b"}
##>>> f.remove({"c", "b"})
##True
##>>> f.connected("c")
##set()
##
##Dans cette mission toutes les données sont correctes, par conséquent vous n'avez pas besoin d'implémenter des contrôles.
##
##Entrée: états et expression de la classe "Friends".
##
##Résultats: Le fonctionnement tel que décris.
##
##Utilisation: Ici vous implémentez une classe avec des changements. Ce n'est pas une structure simple avec quelques fonctions, mais une réprésentation d'objets avec une structure complexe.
##
##Precondition: Toutes les données sont correctes.

class Friends:
    def __init__(self, connections):
        self.relations = []
        for elem in connections:
            self.relations.append(elem)

    def add(self, connection):
        if connection in self.relations:
            return False
        else:
            self.relations.append(connection)
            return True

    def remove(self, connection):
        try:
            self.relations.remove(connection)
            return True
        except:
            return False

    def names(self):
        temp = []
        for relation in self.relations:
            for item in relation:
                temp.append(item)
        setTemp = set()
        for item in temp:
            setTemp.add(item)
        return setTemp        
        
    def connected(self, name):
        temp = []
        for relation in self.relations:
            if name in relation:
                for item in relation:
                    if name != item:
                        temp.append(item)
        setTemp = set()
        for item in temp:
            setTemp.add(item)
        return setTemp 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
