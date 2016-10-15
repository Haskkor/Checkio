##Un réseau IP est un ensemble de routeurs qui communiquent des informations par le biais d'un protocole. Un routeur est identifié de façon univoque par une adresse IP. 
##En IPv4, une adresse IP est composée de 32 bits, canoniquement représentée par 4 nombres décimaux de 8 bits chacun, de l'intervalle des nombres entiers de 0 (00000000) à 255 (11111111).
##Chaque routeur possède une table de routage qui contient une liste d'adresses IP, afin qu'il sache où envoyer des paquets IP.
##"Route summarization" (réduction d'itinéraire) dans les réseaux IP
##Puisque le réseau grossit sans cesse (des centaines de routeurs), le nombre d'adresses IP dans la table de routage croît très vite. Si l'on conserve un grand nombre d'adresses IP dans la table de routage, cela va entraîner une perte de performances (mémoire, bande passante et limitation des ressources CPU).
##Le principe de "route summarization", appelée aussi "route aggregation", consiste à reduire le nombre de "routes" (itinéraires) en les regroupant dans un "summary route" (itinéraire réduit).
##
##Observons l'exemple suivant:
##summary route
##
##Nous avons 4 routeurs connectés à A. A connaît les 4 adresses IP, parce qu'il a une interface directe avec chacune d'entre elles. Toutefois, A ne va pas les envoyer toutes à B.
##Au lieu de cela, il va regrouper les adresses en une "summary route", et envoyer cette nouvelle "route" à B. 
##Ce qui implique que: 
##
##- Le lien entre A et B utilise moins de bande passante
##- B économise de la mémoire: il n'a qu'un chemin à enregistrer dans sa table de routage
##- B économise des ressources CPU: il y a moins d'entrées à considérer lors de la manipulation des paquets IP
##Programmer une "summary route"
##A stocke les 4 adresses IP dans sa table de routage. 
##
##Adresse 1	172.16.12.0
##Adresse 2	172.16.13.0
##Adresse 3	172.16.14.0
##Adresse 4	172.16.15.0
##
##A va convertir ces adresses IP au format binaire, les aligner et trouver la limite entre le préfixe commun situé à gauche (indiqué en rouge), et les bits restants à droite. 
##
##Adresse 1	10101100	00010000	00001100	00000000
##Adresse 2	10101100	00010000	00001101	00000000
##Adresse 3	10101100	00010000	00001110	00000000
##Adresse 4	10101100	00010000	00001111	00000000
##
##A crée une nouvelle adresse IP constituée des bits communs, et tous les autres bits mis à "0".
##Cette nouvelle adresse IP est convertie à son tour en nombre décimaux.
##Pour terminer, A évalue le nombre de bits communs, appelé "subnet".
##La "summary route" est constituée de la nouvelle adresse IP, suivie d'un "slash" puis du "subnet": 172.16.12.0/22
##Input: Une liste de chaînes de caractères qui contient les adresses IP.
##
##Output: Une chaine de caractères qui contient la "summary route", qui représente une adresse IP, suivie d'un "slash" puis du "subnet".
##
##Exemple:
##
##checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"
##checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"
##checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"
##
##Préconditions: 
##all(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",d) for d in data))
##all(-1 < int(n) < 256 for n in d.split(".") for d in data)
##len(data) == len(set(data)) and len(data) > 1

def checkio(data):
    list_bytes = []
    for ip in data:
        list_dec,str_bit = ip.split('.'),""
        for dec in list_dec:
            temp_bit = str(bin(int(dec,10)))[2:]
            if len(temp_bit) < 8:
                temp_bit = "0" * (8 - len(temp_bit)) + temp_bit
            str_bit += temp_bit
        list_bytes.append(str_bit)
    common_bits,found = 0,False
    for i in range(len(list_bytes[0])):
        for j in range(1,len(list_bytes)):
            if list_bytes[j][i] != list_bytes[0][i]:
                common_bits,found = i,True
                break
        if found:break 
    final_binary = list_bytes[0][:common_bits] + "0" * (32 - common_bits)
    to_return = str(int(final_binary[:8],2)) + "." + \
        str(int(final_binary[8:16],2)) + "." + str(int(final_binary[16:24],2)) \
        + "." + str(int(final_binary[24:32],2)) + "/" + str(common_bits)
    return to_return
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
    assert (checkio(["192.168.97.0","192.168.100.0"]) == "192.168.96.0/21"), "Fourth Test"
    assert (checkio(["172.16.14.0","172.16.17.0","172.16.25.0","10.1.57.0","10.1.59.0","10.1.61.0"]) == "0.0.0.0/0"), "Fifth Test"
