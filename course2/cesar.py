#lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr
#riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm
#mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj
#rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
#vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr
#vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd
#ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi
#hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt
#bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb

#- Déchiffrer le texte.

#- Qui à écrit le texte ?

#On reçoit le texte suivant :

#xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpit ghlxiwiwtxgqadds

#Procéder à une attaque de ce chiffre basée sur la fréquence d’apparition des lettres.




majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscules = majuscules.lower()

def lettre(c):
    return c in majuscules or c in minuscules

def decalage(c,k):
    if lettre(c):
        if c in majuscules :
            alphabet = majuscules
        else:
            alphabet = minuscules
        car = alphabet.find(c)
        car += k
        while car >= len(alphabet):
            car -= len(alphabet)
        while car < 0:
            car += len(alphabet)
        return alphabet[car]
    else:
        return ""

def cesar(message,d,crypte):
    chiffre=''
    for c in message:
        if lettre(c):
            if c in majuscules :
                alphabet = majuscules
            else:
                alphabet = minuscules
            if crypte:
                chiffre += decalage(c,d)
            else:
                chiffre += decalage(c,-d)
        else:
            chiffre += c
    return chiffre


texte="un deux trois quatre cinq six sept huit neuf dix"
texte_code = cesar(texte,3,True)
print(texte_code)
texte_decode = cesar(texte_code,3,False)
print(texte_decode)
