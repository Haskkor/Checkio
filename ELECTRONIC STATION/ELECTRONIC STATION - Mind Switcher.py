##Les drones de Sophia sont de simples robots auxquels on ne confie aucun travail dangereux. Simplement en cas de panne, Sophia a une machine de sauvegarde pour ces drones. Cette machine peut copier la mémoire d'un robot à l'aide d'une fonction secrète sans documentation. Cette machine de sauvegarde peut aussi servir à échanger la mémoire de deux robots.
##
##Mais Sophia a oublié d'éteindre cette machine, et a laissé les robots seuls avec elle... Quand Sophia est revenue, certains drones avaient déjà échangé leur mémoire entre eux ! Il nous faut les aider à retrouver leur corps d'origine (sinon, ils ne seront plus sous garantie).
##
##La machine a gardé une trace de tous les échanges de mémoire effectués : le journal. Il y a néanmoins un problème supplémentaire : les mémoires peuvent être échangées entre deux corps de drones AU PLUS UNE FOIS. Cependant, en rajoutant deux drones supplémentaires, tout ce chaos peut être remis en ordre. Nikola et Sophia se sont proposés de nous aider en prêtant leur propre drone ("nikola" et "sophia").
##
##Vous disposez d'un journal (list of sets) contenant les informations sur les échanges récents. Chaque entrée est un ensemble (set) de deux noms (string) de robots (les corps). Vous pouvez agir sur les corps dont les noms figurent dans les données, ainsi que sur deux corps supplémentaires : "nikola" et "sophia". Trouvez une suite d'échanges de mémoires qui permette de rendre à chaque corps sa mémoire d'origine. Le résultat sera représenté par une liste/tuple d'ensembles de deux noms (string) chacun.
##
##Input: Un journal, comme tuple d'ensembles (set). Chaque ensemble (set) contient deux noms de drones (string).
##
##Output: La suite des échanges à effectuer, comme list/tuple d'ensembles (set). Chaque ensemble (set) contient deux noms de drones (string).
##
##Exemple:
##
##mind_switcher(({"scout", "super"},)) == ({"super", "nikola"}, {"sophia", "scout"},
##                                         {"nikola", "scout"}, {"sophia", "super"},
##                                         {"nikola", "sophia"})
##​
##Application: Pour cette mission, on utilise un très joli théorème mathématique de théorie des groupes. La théorie des groupes a des applications en cryptographie, physique et chimie.
##
##Préconditions:
##0 < len(journal) ≤ 55
##La donnée journal est correcte.

def del_robots_done(robots_dict):
    """ Delete robots containing their own memory. """
    to_delete = set()
    for key,val in robots_dict.items():                               
        if key == val:to_delete.add(key)
    for elem in to_delete:del robots_dict[elem]

def switch_res(first_val,second_val,journal,result,switch_niksop):
    """ Appending results when switching. """
    if {first_val,second_val} in journal or {second_val,first_val} in journal:
        result.append({first_val,'sophia'})
        result.append({second_val,'nikola'})
        result.append({second_val,'sophia'})
        result.append({first_val,'nikola'})
        return switch_niksop + 1
    else:
        result.append({first_val,second_val})
        return switch_niksop

def mind_switcher(journal):
    result,robots_dict,list_journal,switch_niksop = [],dict(),list(journal),0
    # Filling a dict with each robot and the memory it contains at the end
    for log in list_journal:
        for name in log:
            robots_dict[name] = name
    for log in list_journal:
        list_elem = list(log)
        robots_dict[list_elem[0]],robots_dict[list_elem[1]] = \
            robots_dict[list_elem[1]],robots_dict[list_elem[0]]
    # Switching until every robot has its own memory
    while robots_dict:
        switch_done = False
        # Checks for simple switch : {a:b},{b:a}
        for key,val in robots_dict.items():
            if robots_dict[val] == key and robots_dict[val] != val:
                robots_dict[key],robots_dict[val] = key,val
                switch_niksop = switch_res(key,val,journal,result,switch_niksop)
                switch_done = True
        # Checks for switch not in journal : {a:b},{b:c}
        if not switch_done:
            for key,val in robots_dict.items():
                if {key,val} not in journal and {val,key} not in journal:
                    robots_dict[key],robots_dict[val] = \
                        robots_dict[val],robots_dict[key]
                    result.append({key,val})
                    switch_done = True
                    break
        # Puts a value in the first buffer, switch with keys until there is
        # only two keys left, final switch with the 2 buffers
        if not switch_done:
            keys_list = list(robots_dict.keys())
            temp = robots_dict[keys_list[0]]
            sophia = robots_dict[keys_list[0]]
            robots_dict[keys_list[0]] = 'sophia'
            result.append({'sophia',keys_list[0]})
            while len(robots_dict) > 2:
                result.append({'sophia',sophia})
                temp = robots_dict[sophia]
                robots_dict[sophia] = sophia
                sophia = temp
                del_robots_done(robots_dict)
            for key,val in robots_dict.items():
                if val != 'sophia':
                    result.append({'nikola',key})
                    nikola = val
                    robots_dict[key] = 'nikola'
            for key,val in robots_dict.items():
                if val == 'sophia':
                    result.append({'nikola',key})
                    robots_dict[key] = nikola
                    nikola = 'sophia'
            for key,val in robots_dict.items():
                if val == 'nikola':
                    result.append({'sophia',key})
                    robots_dict[key] = sophia
                    sophia = 'nikola'
                    switch_niksop += 1
        # Delete robots with their own memory
        del_robots_done(robots_dict)
    # Final switch between buffer robots
    if switch_niksop % 2 == 1:
        result.append({'sophia','nikola'})
    return result

#print(mind_switcher(({"scout", "super"},)))
#print("")
#print(mind_switcher(({'hater', 'scout'}, {'planer', 'hater'})))
#print("")
#print(mind_switcher(({'scout', 'driller'}, {'scout', 'lister'}, {'hater', 'digger'}, {'planer', 'lister'}, {'super', 'melter'})))
#print("")
#print(mind_switcher([{'super', 'melter'}, {'digger', 'lister'}, {'melter', 'planer'}, {'scout', 'digger'}, {'scout', 'drawer'}, {'driller', 'hater'}, {'melter', 'lister'}, {'super', 'digger'},{'planer', 'drawer'},{'planer', 'lister'}, {'super', 'planer'}, {'super', 'lister'}, {'scout', 'lister'}, {'super', 'driller'}, {'lister', 'drawer'}, {'hammer', 'drawer'}, {'lister', 'hater'}, {'scout', 'super'}, {'scout', 'hammer'}, {'digger', 'hater'}, {'planer', 'hater'}, {'digger', 'planer'}, {'hammer', 'hater'}, {'scout', 'melter'}, {'scout', 'planer'}, {'melter', 'driller'},{'scout', 'hater'}, {'melter', 'hammer'}, {'drawer', 'hater'}, {'hammer', 'lister'}, {'super', 'hater'}, {'digger', 'hammer'}, {'digger', 'melter'}, {'driller', 'hammer'}, {'melter', 'drawer'},{'driller', 'drawer'}, {'digger', 'driller'}, {'planer', 'hammer'}, {'super', 'hammer'}, {'melter', 'hater'}, {'scout', 'driller'}, {'super', 'drawer'}, {'driller', 'lister'}, {'digger', 'drawer'},{'planer', 'driller'}]))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(func, data):
        robots = {"nikola": "nikola", "sophia": "sophia"}
        switched = []
        for pair in data:
            switched.append(set(pair))
            r1, r2 = pair
            robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)

        result = func(data)
        if not isinstance(result, (list, tuple)) or not all(isinstance(p, set) for p in result):
            print("The result should be a list/tuple of sets.")
            return False
        for pair in result:
            if len(pair) != 2:
                print(1, "Each pair should contain exactly two names.")
                return False
            r1, r2 = pair
            if not isinstance(r1, str) or not isinstance(r2, str):
                print("Names must be strings.")
                return False
            if r1 not in robots.keys():
                print("I don't know '{}'.".format(r1))
                return False
            if r2 not in robots.keys():
                print("I don't know '{}'.".format(r2))
                return False
            if set(pair) in switched:
                print("'{}' and '{}' already were switched.".format(r1, r2))
                return False
            switched.append(set(pair))
            robots[r1], robots[r2] = robots[r2], robots[r1]
        for body, mind in robots.items():
            if body != mind:
                print("'{}' has '{}' mind.".format(body, mind))
                return False
        return True

    assert check_solution(mind_switcher, ({"scout", "super"},))
    assert check_solution(mind_switcher, ({'hater', 'scout'}, {'planer', 'hater'}))
    assert check_solution(mind_switcher, ({'scout', 'driller'}, {'scout', 'lister'},
                                          {'hater', 'digger'}, {'planer', 'lister'}, {'super', 'melter'}))
