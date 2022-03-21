import tkinter
import bs4 as bs
import urllib.request
from pylab import *
from tkinter import * 

def occurence(dico):
    fichier = open('texte-lino.txt', 'r')
    texte = fichier.read()
    texte_minuscule = texte.lower()
    
    dicofin = {}
    for key in dico.keys():
        nbmot = 0 
        for mot in dico[key]:
            nbmot += len(boyer_moore(texte_minuscule, mot))
        dicofin[key]= nbmot
    cle_resultats = [] 
    resultats=dicofin
    for keys in resultats:
        cle_resultats.append(keys)
    print(cle_resultats)
    val_resultats = []
    for val in resultats:
        val_resultats.append(int(resultats[val]))
    print(val_resultats)
        


    texte3 = Label (fenetre, text = cle_resultats[0] + " : " +  str(val_resultats[0]) + " fois", font= ('Aerial 17 bold italic'))
    texte3.pack(pady=1)
    texte4 = Label (fenetre, text = cle_resultats[1] + " : " +  str(val_resultats[1]) + " fois", font= ('Aerial 17 bold italic'))
    texte4.pack(pady=1)
    texte5 = Label (fenetre, text = cle_resultats[2] + " : " +  str(val_resultats[2]) + " fois", font= ('Aerial 17 bold italic'))
    texte5.pack(pady=1)
    texte6 = Label (fenetre, text = cle_resultats[3] + " : " +  str(val_resultats[3]) + " fois", font= ('Aerial 17 bold italic'))
    texte6.pack(pady=1)
    texte7 = Label (fenetre, text = cle_resultats[4] + " : " +  str(val_resultats[4])+ " fois", font= ('Aerial 17 bold italic'))
    texte7.pack(pady=1)
    texte8 = Label (fenetre, text = cle_resultats[5] + " : " +  str(val_resultats[5])+ " fois", font= ('Aerial 17 bold italic'))
    texte8.pack(pady=1)

    couleurs = ['blue', 'red', 'green', 'yellow', 'cyan', 'purple']

    pie(val_resultats, labels=cle_resultats, colors=couleurs, autopct='%1.1f%%')
    axis('equal')

    show()

def table_sauts(cle) :
    # crée un dico qui à chaque lettre renvoie son décalage
    d = {}
    for i in range(len(cle)-1):
        d[cle[i]] = len(cle) - i - 1
    return d

def boyer_moore (texte, cle):
    long_txt = len(texte)
    long_cle = len(cle)
    positions = [] #liste des positions où l'on trouve le motif
    if long_cle <= long_txt :
        decalage = table_sauts(cle) #on charge la table des décalages
    i=0
    trouve = False
    while (i <= long_txt-long_cle):
        for j in range (long_cle -1, -1, -1): #On part du dernier indice de la cle jusque 0 en décalant de -1 à chaque fois
            trouve = True
            if texte[i+j] != cle[j] : # Si on tombe sur une lettre différentes de celle de la clé
                if (texte[i+j] in decalage and decalage[texte[i+j]]<=j):
                    i+=decalage[texte[i+j]] # on décale dans le texte en utilisant la table de décalage
                else :
                    i+=j+1 # si la lettre n'est pas dans la table de décalage alors on décale du nombre de lettres restantes à explorer sur la clé
                trouve = False
                break #on sort de la boucle for car on a trouvé une lettre qui ne convient pas
        if trouve : #si toutes les lettres convenait donc on a trouvé une occurence de la clé dans texte
            positions.append(i) #on ajoute à la liste des positions où l'on trouve la clé dans le texte
            i=i+1
            trouve = False #on remet trouvé à False car on cherche la prochaine occurence
    return positions

def splittexte(texte):
    liste = texte.split(",")
    print(liste)


def search():
    url = entrée1.get()
    sauce1=urllib.request.urlopen(url)
    soup1 = bs.BeautifulSoup(sauce1,'html5lib')
    fichier = open('texte-lino.txt','w')
    tmp = soup1.find('div','song-text').text
    fichier.write(tmp)
    fichier.close()

#https://www.paroles.net/jul/paroles-bande-organisee


listeamour= ['amoureux', 'tendresse', 'amitié', 'baiser', 'Cupidon', 'Aphrodite', 'passion', 'Éros', 'désir','sentiment', 'amant', 'affection', 'idylle', 'Vénus', 'attachement', 'attirance', 'platonique', 'compassion','plaisir', 'charité', 'érotique', 'haine', 'relation', 'beauté', 'adoration', 'aimer', 'philtre', 'altruisme','amourette', 'bien-aimé', 'érotisme', 'joie', 'mariage', 'romantique', 'courtois', 'émotion', 'déesse', 'éternel','luxure', 'bonheur', 'conjugal', 'jalousie', 'psyché', 'cœur', 'filial', 'fraternel', 'charnel', 'chaste','sexualité', 'dévotion', 'ivresse', 'philanthropie', 'amour platonique', 'couple', 'fidélité', 'flamme','tendre', 'sincère', 'volupté', 'Dieu', 'idolâtrie', 'piété', 'souffrance', 'troubadour', 'chant','chasteté', 'désespoir', 'libertinage', 'romantisme', 'solitude', 'désamour', 'poésie', 'sacrifice','mépris', 'poème', 'sensualité', 'sexuel', 'chagrin', 'feu', 'loyauté', 'Marivaux', 'romance', 'épris','hymen', 'séduction', 'âme', 'dilection', 'lyrique', 'ode', 'thème', 'abnégation', 'bagatelle', 'bien-aimée','chanson', 'conquête', 'déclaration', 'désintéressement', 'fou', 'indifférence', 'passionné', 'adultère','amor', 'enchantement', 'femme', 'inceste', 'mystique', 'passionnel', 'paternel', 'respect', 'romanesque','concupiscence', 'heureux', 'Juliette', 'Musset', 'sonnet', 'tourment', 'tristesse', 'agapè', 'follement','fraternité', 'infini', 'mari', 'maternel', 'narcissisme', 'sentimental', 'adorable', 'ardeur', 'baise','chevaleresque', 'drame', 'égoïste', 'étreinte', 'fille', 'jeunesse', 'malheur', 'mélancolie', 'nymphe','tragique', 'volage', 'admiration', 'charme', 'coït', 'époux', 'ferveur', 'folie', 'générosité', 'Hélène','intrigue', 'Jésus', 'poète', 'tragédie', 'accouplement', 'Adonis', 'amour maternel', 'amoureusement', 'caprice','contemplation', 'coup de foudre', 'éprouver', 'héroïne', 'homosexuel', 'intimité', 'timide', 'Tristan','vénération', 'affective', 'Andromaque', 'aventure', 'confidente', 'coquetterie', 'délice', 'extase','galanterie', 'rédemption', 'adolescent', 'amante', 'ami', 'carquois', 'désintéressé', 'divin', 'égoïsme','enflammer', 'fidèle', 'film', 'gloire', 'hyménée', 'idéal', 'idyllique', 'mère', 'véritable', 'virginité','beau', 'cour', 'dévouement', 'garçon', 'immodéré', 'inconstance', 'Lancelot', 'naissant', 'récit', 'sensuel','aphrodisiaque', 'badinage', 'Boccace', 'chéri', 'coquin', 'fleurette', 'Héra', 'malheureux', 'mutuel','Thésée', 'ange', 'berger', 'croire', 'culte', 'débauche', 'délicatesse', 'effusion', 'élan', 'enivrant','enthousiasme', 'estime', 'exprimer', 'fée', 'homosexualité', 'Horace', 'inclination', 'mysticisme','partagé', 'penchant', 'petit copain', 'pulsion', 'relation amoureuse', 'rut', 'soupirant', 'sympathie','bisou', 'Chimène', 'coucher', 'cruel', 'Dante', 'effréné', 'fiançailles', 'foi', 'foutre', 'gaieté','Hippolyte', 'infidélité', 'inquiétude', 'jaloux', 'love', 'Phèdre', 'pitié', 'premier amour', 'Rodrigue','sacrifier', 'Saint-Valentin', 'sans espoir', 'sexe', 'sincérité', 'Truffaut', 'zoophileAstarté','aveugle', 'belle âme', 'bonté', 'caresse', 'chérir', 'compagne', 'confidence', 'débordant', 'inaltérable','incommensurable', 'instinctif', 'intérêt', 'lyrisme', 'peinture', 'réciproque', 'rédempteur', 'roman', 'Roméo','sagesse', 'soufi', 'Stendhal', 'vénal', 'aimable', 'Antéros', 'ardent', 'billet doux', 'consume', 'copulation','courage', 'enchanteur', 'espérance', 'exaltation', 'fantôme', 'fol', 'folle', 'fusionnel', 'Héloïse']

listetristesse = ['mélancolie', 'deuil', 'chagrin', 'nostalgie', 'ennui', 'dégoût', 'désespoir', 'triste', 'amertume', 'émotion', 'sentiment', 'souffrance', 'larme', 'découragement', 'mélancolique', 'désolation', 'dépression', 'douleur', 'morne', 'abattement', 'affliction', 'solitude', 'lassitude', 'inquiétude', 'langueur', 'nuage', 'cafard', 'gaieté', 'malheur', 'angoisse', 'glauque', 'peur', 'amer', 'consternation', 'désespérance', 'regret', 'spleen', 'infinie', 'ressentir', 'colère', 'effroi', 'résignation', 'acédie', 'haine', 'humeur', 'mal', 'neurasthénie', 'pleurer', 'rancœur', 'âme', 'blues', 'déchirement', 'désenchantement', 'écœurement', 'laideur', 'morosité', 'sombre', 'compassion', 'consolation', 'idées noires', 'abattu', 'envahit', 'éprouve', 'accablé', 'accablement', 'affligé', 'déplaisir', 'indéfinissable', 'passion', 'profonde', 'anxiété', 'bile', 'exprimer', 'indicible', 'morose', 'peine', 'adieu', 'contrariété', 'dépit', 'drame', 'fatigue', 'incurable', 'monotonie', 'noirceur', 'rage', 'tourment', 'tracas', 'atrabile', 'contrition', 'déception', 'déprime', 'écroulé', 'lugubre', 'serrer le cœur', 'inconsolable', 'incommensurable', 'lamentation', 'inexprimable', 'isolement', 'repentir', 'stupeur', 'abandon', 'aigreur', 'aspect morne', 'assombrissement', 'asthénie', 'attristé', 'austérité', 'bourdon', 'brumaille', 'calamité', 'componction', 'contrit', 'dépressif', 'désabusement', 'désœuvrement', 'élancement', 'embarras', 'endolorissement', 'éplorement', 'épreuve', 'fiel', 'froid', 'grisaille', 'hypocondrie', 'lypémanie', 'malaise', 'maussaderie', 'mocheté', 'navrement', 'noir', 'papillons noirs', 'pauvreté', 'platitude', 'rigueurs', 'saudade', 'serrement de cœur', 'sévérité', 'solennité', 'sombreur', 'souci', 'tristounet', "vague à l'âme", 'voilé']

listejoie = ['allégresse', 'bonheur', 'émotion', 'enthousiasme', 'plaisir', 'jubilation', 'liesse', 'réjouissance', 'tristesse', 'satisfaction', 'joyeux', 'gaieté', 'sentiment', 'euphorie', 'félicité', 'cri', 'amour', 'espérance', 'sérénité', 'ravissement', 'sourire', 'triomphe', 'consolation', 'fierté', 'hymne', 'gaité', 'indicible', 'jubiler', 'rire', 'désir', 'fou', 'cœur', 'béatitude', 'exaltation', 'intense', 'Spinoza', 'contentement', 'exultation', 'transport', 'délectation', 'folle', 'ode', 'volupté', 'délice', 'pleurer', 'réjouir', 'euphorique', 'inexprimable', 'optimisme', 'transporté', 'Beethoven', 'hilarité', 'ineffable', 'rayonnant', 'aise', 'alléluia', 'âme', 'extase', 'fête', 'joyeusement', 'tendresse', 'exclamation', 'exulter', 'humour', 'soulagement', 'acclamation', 'débordant', 'épanouissement', 'Euphrosyne', 'exprimer', 'festin', 'ivresse', 'manifestation', 'mélange', 'visage', 'bienveillance', 'comble', 'compassion', 'éprouver', 'goûter', 'cantique', 'indescriptible', 'pleurant', 'rayonne', 'surprise', 'bien-être', 'bienfait', 'humeur', 'jouissance', 'paix', 'passion', 'sauter', 'vivre', 'entrain', 'gambader', 'donner', 'douceur', 'éclatement', 'éphémère', 'incommensurable', 'larme', 'ressentir', 'revoir', 'applaudissement', 'comblera', 'contenir', 'délirante', 'démonstration', 'ébaudir', 'effusion', 'emplit', 'enfantine', 'exubérant', 'gratitude', 'manifester', 'plénitude', 'pleurs', 'réconfort', 'remplit', 'savourer', 'symphonie', 'célébration', 'communicative', 'embrasser', 'expansive', 'explosion', 'immense', 'infinie', 'amusement', 'bondir', 'exhortation', 'extatique', 'illumine', 'radieux', 'agrément', 'alacrité', 'ami', 'ardeur', 'assouvissement', 'avantage', 'débordement', 'détente', 'distraction', 'divertissement', 'élan', 'emballement', 'émerveillement', 'enchantement', 'enjouement', 'espoir', 'folichonnerie', 'fun', 'griserie', 'heureuse', 'honneur', 'humeur joyeuse', 'interjection', 'jovialité', 'joyeuseté', 'jubilatoire', 'noce', 'panard', 'pied', 'plaisanterie', 'rayonnement', 'régal', 'rigolade', 'schadenfreude', 'vivat']

listepeur = ['phobie', 'panique', 'émotion', 'crainte', 'frousse', 'trouille', 'angoisse', 'épouvante', 'terreur', 'anxiété', 'danger', 'frayeur', 'cauchemar', 'sentiment', 'trac', 'horreur', 'pétoche', 'claustrophobie', 'frisson', 'haine', 'appréhension', 'épouvantail', 'timidité', 'flipper', 'insécurité', 'agoraphobie', 'culpabilité', 'irrationnelle', 'trembler', 'claustrophobe', 'dégoût', 'folie', 'menace', 'solitude', 'spectre', 'loup', 'phobique', 'taf', 'amygdale', 'avoir les chocottes', 'courage', 'craintif', 'intimidation', 'tristesse', 'honte', 'stress', 'paranoïa', 'sensation', 'vertige', 'fuir', 'joie', 'araignée', 'avoir la chienne', 'avoir les jetons', 'chocottes', 'couardise', 'foutre les jetons', 'hydrophobie', 'obscurité', 'russophobie', 'saisissement', 'trouble', 'grande peur', 'hantise', 'impavide', 'répulsion', 'effrayant', 'effroi', 'frémir', 'hanté', 'lâcheté', 'pusillanimité', 'surmonter', 'alarme', 'effrayé', 'faire peur', 'hallucination', 'inquiétude', 'irraisonnée', 'monstre', 'sorcière', 'arachnophobie', 'inconnu', 'rejet', 'serpents', 'agitation', 'chienne', 'croque-mitaine', 'douleur', 'fantastique', 'ogre', 'poltron', 'stimulus', 'sueur', 'affolement', 'arachnophobe', 'aversion', 'détresse', 'émotionnel', 'évitement', 'nomophobie', 'psychologique', 'rassurer', 'violence', 'à faire peur', 'anuptaphobie', 'anxieux', 'apeuré', 'apopathodiaphulatophobie', 'attaquer', 'barre', 'craindre', 'effraie', 'enfer', 'fantôme', 'foie', 'surnaturel', 'tremblant', 'tremble', 'adrénaline', 'cacher', 'colère', 'figer', 'hésitation', 'homophobie', 'loup-garou', 'mouiller', 'paralyse', 'peureux', 'Phobos', 'ressentir', 'symptôme', 'toute seule', 'transir', 'trypanophobie', 'acrophobie', 'chair de poule', 'croyance', 'démon', 'enfuir', 'Halloween', 'maléfique', 'méfiance', 'ose', 'zoophobie', 'coulrophobie', 'cri', 'fuite', 'maladive', "prendre l'avion", 'pressentiment', 'scopophobie', 'tremblement', 'ablutophobie', 'acarophobie', 'achluophobie', 'affres', 'ailurophobie', 'alerte', 'aquaphobie', 'autophobie', 'baliser', 'chantage', 'chier dans ses culottes', 'chier dans son froc', 'consternation', 'dédain', 'déraison', 'désarroi', 'détestation', 'doute', 'égarement', 'emmerde', 'émoi', 'éreutophobie', 'exécration', 'flip', 'haptophobie', 'herpétophobie', 'hétérophobie', 'jetons', 'malepeur', 'mysophobie', 'obusite', 'parthénophobie', 'péfli', 'pépettes', 'peur bleue', 'pisser dans son froc', 'pleutrerie', 'poltronnerie', 'prémonition', 'préoccupation', 'provoquer', 'prudence', 'répugnance', 'reup', 'se déballonner', 'se dégonfler', 'souci', 'souleur', 'stupéfaction', 'stupeur', 'suée', 'superstition', 'thanatophobie', 'tourment', 'train fantôme', 'transe', 'Trémeur', 'venette', 'veulerie']

listemort = ['défunt', 'cadavre', 'résurrection', 'tombeau', 'cercueil', 'agonie', 'euthanasie', 'vie', 'dépouille', 'deuil', 'décès', 'meurtre', 'suicide', 'pendu', 'ressusciter', 'posthume', 'exécution', 'Mânes', 'tombe', 'funèbre', 'cimetière', 'disparu', 'supplice', 'immortalité', 'mourir', 'vivant', 'assassinat', 'enterrement', 'faucheuse', 'autopsie', 'mortel', 'mortuaire', 'noyé', 'trépas', 'enfer', 'funéraire', 'blessé', 'perte', 'strangulation', 'survivant', 'crémation', 'éternité', 'glas', 'pendaison', 'tué', 'claqué', 'noyade', 'destruction', 'immortel', 'catastrophe', 'disparition', 'feu', 'meurtrier', 'ombre', 'spiritisme', 'tragique', 'trépassé', 'assassin', 'Hadès', 'paradis', 'repos', 'succession', 'vieillesse', 'corbillard', 'dernier souffle', 'extrême-onction', 'funérailles', 'funeste', 'ivre', 'mourant', 'belle mort', 'bourreau', 'camarde', 'fossoyeur', 'inanimé', 'macchabée', 'mort-vivant', 'Thanatos', 'âme', 'crevé', 'désolation', 'sépulture', 'thanatologie', 'enterré', 'épitaphe', 'porté disparu', 'spectre', 'taxidermie', 'embaumement', 'linceul', 'martyr', 'martyre', 'matador', 'métempsycose', 'nécromancie', 'religion', 'Requiem', 'vampire', 'châtiment', 'coroner', 'dernier soupir', 'guillotine', 'mémoire', 'néant', 'poison', 'sauver', 'suicider', 'apoptose', 'évanoui', 'infarctus du myocarde', 'macabre', 'nécrose', 'relique', 'survie', 'torture', 'assassiné', 'bûcher', 'canné', 'désert', 'échafaud', 'fatigué', 'foutu', 'naze', 'sépulcre', 'chagrin', 'charogne', 'condamné', 'crime', 'empoisonnement', 'malemort', 'mort-né', 'proscription', 'pulsion', 'puni', 'régicide', 'six pieds sous terre', 'victime', 'violente', 'cénotaphe', 'cinéraire', 'décédé', 'ensevelissement', 'gisant', 'limbe', 'maladie', 'messe', 'mortalité', 'nuit', 'peine capitale', 'pendre', 'regretter', 'venger', 'cendre', 'fosse', 'gibet', 'parque', 'pécheur', 'sommeil', 'supplicié', 'testament', 'charnier', 'commémoration', 'danger', 'ensevelir', 'heure suprême', 'piqûre', 'prématurée', 'purgatoire', 'seuil', 'veuve', 'certaine', 'décapité', 'étranglé', 'imminente', 'menacer', 'venin', 'vie éternelle', 'asphyxie', 'Charon', 'corps', 'esprit', 'exécuter', 'foudroyant', 'inerte', 'post-mortem', 'ruine', 'achever', 'anéantissement', 'apothéose', 'croque-mort', 'crucifié', 'crypte', 'éteint', 'exténué', 'extinction', 'fantôme', 'morgue', 'mors', 'Nécrologie', 'Odin', 'péché', 'pourriture', 'Vallée de la mort', 'attentat', 'autre monde', 'champ de bataille', 'crématoire', 'décapitation', 'dernier adieu', 'déterrer', 'empoisonné', 'génocide', 'heure dernière', 'inhumé', 'intestat', 'nécromasse', 'nécrophile', 'outre-tombe', 'psychopompe', 'regret', 'repos éternel', 'reste', 'sarcophage', 'suaire', 'survivance', 'valkyrie', 'viatique', 'accidentelle', 'agonisant', 'descente aux enfers', 'douloureuse', 'épuisé', 'fin', 'frôlé', 'fusillade', 'instantanée', 'lente', 'létal', 'monument', 'mortifère', 'naissance', 'nécrophilie', 'oraison funèbre', 'succéder', 'suppression', 'accident de la route', 'atroces', 'condamnation', 'décimer', 'délivrera', 'élégie', 'épouvante', 'éternelle', 'honorer', 'incinération', 'inhumation', 'jonchée', 'menace', 'mort subite', 'naufrage', 'obsèques', 'ossements', 'peine', 'pleurer', 'présage', 'souffrance', 'surdose', 'survenue', 'terrible', 'vaincu', 'annoncée', 'anticipée', 'au-delà', 'blessure', 'coma', 'condamnent', 'cruel', 'écroulement', 'homicide', 'horrible', 'ignominie', 'messager', 'parricide', 'sauveur', 'tuant', 'vengeance', 'à plat', 'aboutissement', 'ankylosé', 'apathique', 'bienheureux', 'bousillé', 'brisé', 'cassé', 'chute', 'conclusion', 'décomposition', 'défunction', 'délavé', 'dénouement']

listeviolence = ['terrorisme', 'viol', 'non-violence', 'brutalité', 'agressivité', 'agression', 'extrême', 'exaction', 'intimidation', 'émeute', 'cruauté', 'racisme', 'violenter', 'attentat', 'délinquance', 'force', 'oppression', 'répression', 'contrainte', 'Gandhi', 'injustice', 'intolérance', 'violent', 'furie', 'mutilation', 'incitation', 'pogrom', 'violemment', 'haine', 'insécurité', 'inouïe', 'férocité', 'torture', 'tyrannie', 'racket', 'virulence', 'dictature', 'frénésie', 'terroriste', 'voie de fait', 'déchaînement', 'extorquer', 'guerre', 'harcèlement', 'légitime défense', 'barbarie', 'impétuosité', 'meurtrière', 'excès', 'manifestant', 'pillage', 'psychologique', 'conjugal', 'humiliation', 'massacre', 'meurtre', 'outrance', 'physique', 'puissance', 'sédition', 'conflit', 'crime', 'criminalité', 'fureur', 'grossièreté', 'non-violente', 'ouragan', 'policier', 'rage', 'sexuel', 'souffrance', 'animosité', 'assaut', 'colère', 'horreur', 'paroxysme', 'tourbillon', 'apologie', 'âpreté', 'bagarre', 'choc', 'criminel', 'déferlement', 'emportement', 'infraction', 'manifestation', 'menace', 'pacifisme', 'pacifiste', 'passion', 'terreur', 'véhémence', 'violence conjugale', 'anarchisme', 'commise', 'explosion', 'gang', 'incitant', 'islamiste', 'prévention', 'rapine', 'rejet', 'représaille', 'skinhead', 'surenchère', 'verbale', 'droit', 'opprimé', 'rébellion', 'réprimer', 'tabou', 'dureté', 'flambé', 'mal', 'persécution', 'provocation', 'belliqueux', 'bestialité', 'contraindre', 'débordement', 'fougue', 'justifier', 'militant', 'rapt', 'révolution', 'acte', 'brigandage', 'brusquerie', 'crudité', 'effraction', 'égarement', 'faction', 'folie', 'heurt', 'inhumanité', 'légitimé', 'nervi', 'peur', 'révolte', 'sauvagerie', 'sévices', 'soulèvement', 'spoliation', 'subversion', 'acharnement', 'aggravante', 'anarchie', 'assassinat', 'attaque', 'brutal', 'enlèvement', 'ethnique', 'exercée', 'forcer', 'impunité', 'institutionnelle', 'insulte', 'légitimation', 'proie', 'prône', 'recourir', 'recours', 'violence psychologique', 'antisémite', 'brute', 'extrémiste', 'homicide', 'perfidie', 'proférer', 'psychique', 'subie', 'systémique', 'maltraitance', 'sans défense', 'affrontement', 'bouc', 'délit', 'désir', 'extorsion', 'gifle', 'ratonnade', 'structurelle', 'tension', 'action', 'agitation', 'agresseur', 'ardeur', 'atteindre', 'atteinte', 'bouillonnement', 'calotte', 'casseur', 'chaleur', 'chiquenaude', 'claque', 'cogner', 'comportement', 'contenue', 'coup', 'coups et blessures', 'courroux', 'déchaînée', 'défloraison', 'dégénérer', 'démence', 'démesure', 'emballement', 'énergie', 'énervement', 'éréthisme', 'exacerbation', 'exaltation', 'fascination', 'fascisme', 'feu', 'fièvre', 'horion', 'idéologique', 'intempérance', 'intensité', 'intrusion', 'invasion', 'irascibilité', 'irritabilité', 'kidnapping', 'larcin', 'paramilitaire', 'pétulance', 'pichenette', 'profanation', 'répressive', 'sévice', 'situation', 'soufflet', 'tape', 'torrent', 'vigueur', 'violer', 'vitalité', 'vivacité', 'volcan', 'voyou']

D = {'amour' : listeamour, 'tristesse' :listetristesse, 'joie' : listejoie, 'mort' : listemort, 'violence' : listeviolence, 'peur' : listepeur}

#resultats = occurence(D)
#print(resultats)
#tracer_camember(resultats)

# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *
# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Parole.net Thèmes de Chanson")
# Affichage de la fenêtre créée :
# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")
# Limiter les dimensions d’affichage de la fenêtre principale :
fenetre.maxsize(800,600)
fenetre.minsize(300,400)

texte1 = Label (fenetre, text = "Parole.net : Thèmes de Chanson", font= ('Aerial 17 bold italic'))
texte1.pack(pady=30)

texte2 = Label (fenetre, text = "Ex : https://www.paroles.net/jul/paroles-bande-organisee", font= ('Aerial 17 bold italic'))
texte2.pack(pady=2)

entrée1 = Entry (fenetre, width=60)
entrée1.pack(pady=5)

# Ajout d'un bouton dans la fenêtre :
bouton1 = Button (fenetre, text = "Rechercher", font= ('Aerial 17 bold italic'), relief= RIDGE, cursor = "circle", fg = 'blue', command=lambda: search())
bouton1.pack(pady=5)

bouton2 = Button (fenetre, text = "Tracer le Camember", relief = RIDGE, cursor="circle", fg= "blue", font= ('Aerial 17 bold italic'), command=lambda: occurence(D))
bouton2.pack(pady=5)


fenetre.mainloop()



