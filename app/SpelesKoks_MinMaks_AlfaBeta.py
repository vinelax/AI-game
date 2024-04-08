#!/usr/bin/env python
# coding: utf-8

# In[153]:


# Klase, kas atbilst vienai virsotnei spēles kokā

class Virsotne:

    # Klases konstruktors, kas izveido virsotnes eksemplāru
    # Katrā virsotnes eksmeplārā glabājas virsotnes unikāls identifikators (id), skaitliskā virkne (virkne)
    # pirmā spēlētāja punkti (p1), otrā spēlētāja punkti(p2), un virsotnes atrašanās līmeņa numurs
    # Glabātie dati tiek padoti kā konstruktora argumenti
    def __init__(self, id, virkne, p1, p2, limenis):
        self.id = id
        self.virkne = virkne
        self.p1 = p1
        self.p2 = p2
        self.limenis = limenis
        self.virs_kval = None


# Klase, kas atbilst spēles kokam
class Speles_koks:

    # Klases konstruktors, kas izveido spēles koka eksemplāru
    # Spēles koka eksemplārs ietver sevī virsotņu kopu, kas tiek veidota kā Python saraksts un
    # loku kopu, kas tiek veidota kā Python vārdnīca (dictionary)
    # Gan virsotņu kopa, gan loku kopa sākotnējie ir tukšas
    # Virsotņu kopā glabāsies virsotnes viena aiz otras
    # Loku kopā glabāsies virsotnes unikāls identifikators kā vārdnīcas atslēga (key) un
    # ar konkrētu virsotni citu saistītu virsotņu unikālie identifikatori kā vērtības (values)
    def __init__(self):
        self.virsotnu_kopa = []
        self.loku_kopa = dict()

    # Klases Speles_koks metode, kas pievieno spēles kokam jaunu virsotni, kuru saņem kā argumentu
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)

    # Klases Speles_koks metode, kura papildina loku kopu, saņemot kā argumentus
    # virsotnes identifikatoru, no kuras loks iziet, un virsotnes identifikatoru, kurā loks ieiet
    def pievienot_loku(self, sakumvirsotne_id, beiguvirsotne_id):
        self.loku_kopa[sakumvirsotne_id] = self.loku_kopa.get(sakumvirsotne_id, []) + [beiguvirsotne_id]


# Funkcija, kas atbilstoši veiktajam gājienam iegūst jaunu spēles koka virsotni un
# papildina speles koka virsotņu kopu un loku kopu
# Funkcija kā argumentus saņem veiktā gājiena tipu, sarakstu ar jau iepriekš saģenerētajām virsotnēm, kuras apskata
# vienu pēc otras, un pašreiz apskatāmo virsotni
def gajiena_parbaude(gajiena_tips, generetas_virsotnes, pasreizeja_virsotne):
    if gajiena_tips == '1':
        skaitlis = '1'
    elif gajiena_tips == '2':
        skaitlis = '2'
    else:
        skaitlis = '3'
    if skaitlis in pasreizeja_virsotne[1]:
        global j
        id_new = 'A' + str(j)
        j += 1
        mainita_virkne = pasreizeja_virsotne[1]
        pozicija = mainita_virkne.find(skaitlis)
        if (pozicija == 0):
            if (gajiena_tips == '1'):
                mainita_virkne = mainita_virkne[1:]
            elif (gajiena_tips == '2'):
                if (len(mainita_virkne) > 1):
                    mainita_virkne = mainita_virkne[1:]
                else:
                    mainita_virkne = mainita_virkne.replace("2", "")
            else:
                if (len(mainita_virkne) > 1):
                    mainita_virkne = mainita_virkne[1:]
                else:
                    mainita_virkne = mainita_virkne.replace("3", "")
        else:
            mainita_virkne = mainita_virkne[:pozicija] + mainita_virkne[pozicija + 1:]
        if (pasreizeja_virsotne[4] % 2) == 0:
            p1_new = pasreizeja_virsotne[2]
            p2_new = pasreizeja_virsotne[3] - int(gajiena_tips)
        else:
            p1_new = pasreizeja_virsotne[2] - int(gajiena_tips)
            p2_new = pasreizeja_virsotne[3]

        limenis_new = pasreizeja_virsotne[4] + 1;
        jauna_virsotne = Virsotne(id_new, mainita_virkne, p1_new, p2_new, limenis_new)
        # Pārbauda, lai jaunā virsotne nebūtu kādas jau esošās virsotnes dublikāts
        parbaude = False
        i = 0
        while (not parbaude) and (i <= len(sp.virsotnu_kopa) - 1):
            if (sp.virsotnu_kopa[i].virkne == jauna_virsotne.virkne) and (
                    sp.virsotnu_kopa[i].p1 == jauna_virsotne.p1) and (sp.virsotnu_kopa[i].p2 == jauna_virsotne.p2) and (
                    sp.virsotnu_kopa[i].limenis == jauna_virsotne.limenis):
                parbaude = True
            else:
                i += 1
        # Sekmīgi izejot pārbaudi pievieno jauno virsotni un loku sarakstam un vārdnīcai
        if not parbaude:
            sp.pievienot_virsotni(jauna_virsotne)
            generetas_virsotnes.append([id_new, mainita_virkne, p1_new, p2_new, limenis_new])
            sp.pievienot_loku(pasreizeja_virsotne[0], id_new)
        # Nesekmīgās pārbaudes gadījumā, atgriež virsotņu skaitītāju atpakaļ par vienu
        # un veido loku starp pašreizējo virsotni un atrastā duplikāta oriģinālu
        else:
            j -= 1
            sp.pievienot_loku(pasreizeja_virsotne[0], sp.virsotnu_kopa[i].id)


# tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku
def sp_gen():
    global sp
    sp = Speles_koks()
    # tiek izveidots tukšs ģenerēto virsotņu saraksts
    global generetas_virsotnes
    generetas_virsotnes = []
    # tiek izveidota sākumvirsotne spēles kokā
    sp.pievienot_virsotni(Virsotne('A1', '111233', 80, 80, 1))
    # tiek pievienota pirmā virsotne ģenerēto virsotņu sarakstam
    generetas_virsotnes.append(['A1', '111233', 80, 80, 1])
    # mainīgais, kurš skaita virsotnes
    global j
    j = 2
    # ģenerētā koka dziļuma ierobežojums
    global gen_lim
    gen_lim = 6
    # kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras
    while len(generetas_virsotnes) > 0 and gen_lim >= generetas_virsotnes[0][4]:
        # par pašreiz apskatāmo virsotni kļūst pirmā virsotne saģenerēto virsotņu sarakstā
        pasreizeja_virsotne = generetas_virsotnes[0]
        # tiek pārbaudīts gājiens, kad spēlētājs atņem (no saviem punktiem) un izņem (no virknes) vieninieku
        gajiena_parbaude('1', generetas_virsotnes, pasreizeja_virsotne)
        # tiek pārbaudīts gājiens, kad spēlētājs atņem (no saviem punktiem) un izņem (no virknes) divnieku
        gajiena_parbaude('2', generetas_virsotnes, pasreizeja_virsotne)
        # tiek pārbaudīts gājiens, kad spēlētājs atņem (no saviem punktiem) un izņem (no virknes) trijnieku
        gajiena_parbaude('3', generetas_virsotnes, pasreizeja_virsotne)
        # kad visi gājieni no pašreiz apskatāmās virsotnes ir apskatīti, šo virsotni dzēš no ģenerēto virsotņu saraksta
        generetas_virsotnes.pop(0)
    return sp


# In[154]:


def minimaks(virsotnu_kopa, loku_kopa):
    for x in reversed(sp.virsotnu_kopa):  # pārmeklējam no apakšas uz augšu

        if x.virkne == "":  # pilns koks
            if x.p1 > x.p2:
                x.virs_kval = -1
            elif x.p1 == x.p2:
                x.virs_kval = 0
            else:
                x.virs_kval = 1
            continue

        elif x.limenis == gen_lim + 1:  # nepilns koks
            if x.limenis % 2 == 1:  # datora gājiens
                x.virs_kval = x.p2 - x.p1 + int(str(x.virkne)[0])  # heiristiska funk.
            else:  # cilvēka gājiens
                x.virs_kval = x.p2 - x.p1 - int(str(x.virkne)[0])  # heiristiska funk.

            continue

        if x.limenis % 2 == 1:  # minimizētājs
            x.virs_kval = 80
            for pectec in loku_kopa[x.id]:
                if virsotnu_kopa[int(pectec[1:]) - 1].virs_kval < x.virs_kval:
                    x.virs_kval = virsotnu_kopa[int(pectec[1:]) - 1].virs_kval
        else:
            x.virs_kval = -80  # maksimizētājs
            for pectec in sp.loku_kopa[x.id]:
                if virsotnu_kopa[int(pectec[1:]) - 1].virs_kval > x.virs_kval:
                    x.virs_kval = virsotnu_kopa[int(pectec[1:]) - 1].virs_kval

    return virsotnu_kopa[0].virs_kval


# minimaks(sp.virsotnu_kopa,sp.loku_kopa)


# In[155]:


def alfabeta(virsotnu_kopa, loku_kopa, index, alpha, beta):
    if virsotnu_kopa[index].virkne == "":  # rekursijas base case pilnajam kokam

        if virsotnu_kopa[index].p1 > virsotnu_kopa[index].p2:
            virsotnu_kopa[index].virs_kval = -1
            return -1
        elif virsotnu_kopa[index].p1 == virsotnu_kopa[index].p2:
            virsotnu_kopa[index].virs_kval = 0
            return 0
        else:
            virsotnu_kopa[index].virs_kval = 1
            return 1

    if virsotnu_kopa[index].limenis == gen_lim + 1:  # rekursijas base case nepilnajam kokam
        if virsotnu_kopa[index].limenis % 2 == 1:  # datora gājiens
            virsotnu_kopa[index].virs_kval = virsotnu_kopa[index].p2 - virsotnu_kopa[index].p1 + int(
                virsotnu_kopa[index].virkne[0])  # heiristiska funk.
            return int(virsotnu_kopa[index].virs_kval)
        else:  # cilvēka gājiens
            virsotnu_kopa[index].virs_kval = virsotnu_kopa[index].p2 - virsotnu_kopa[index].p1 - int(
                virsotnu_kopa[index].virkne[0])  # heiristiska funk.
            return int(virsotnu_kopa[index].virs_kval)

    if virsotnu_kopa[index].limenis % 2 == 1:  # minimizētājs
        min_eval = float('inf')
        for pectec in loku_kopa[virsotnu_kopa[index].id]:
            eval = alfabeta(virsotnu_kopa, loku_kopa, int(pectec[1:]) - 1, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha nogriešana
        virsotnu_kopa[index].virs_kval = min_eval
        return min_eval
    else:  # maksimizētājs
        max_eval = float('-inf')
        for pectec in loku_kopa[virsotnu_kopa[index].id]:
            eval = alfabeta(virsotnu_kopa, loku_kopa, int(pectec[1:]) - 1, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta nogriešana
        virsotnu_kopa[index].virs_kval = max_eval
        return max_eval

# alfabeta(sp.virsotnu_kopa, sp.loku_kopa, 0, float('-inf'), float('inf'))