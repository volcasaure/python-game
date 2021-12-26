
from fourni import simulateur
from outils import \
    creer_image, \
    creer_caisse, creer_cible, creer_mur, creer_personnage

# Constante à utiliser

VALEUR_COUP: int = 50


# Fonctions à développer

def jeu_en_cours(caisses: list, cibles: list) -> bool:
    """
    Fonction testant si le jeu est encore en cours et retournant un booléen comme réponse sur l'état de la partie.
    :param caisses: La liste des caisses du niveau en cours
    :param cibles: La liste des cibles du niveau en cours
    :return: True si la partie est finie, False sinon
    """

    pass


def charger_niveau(joueur: list, caisses: list, cibles: list, murs: list, path: str):
    """
    Fonction permettant de charger depuis un fichier.txt et de remplir les différentes listes permettant le
    fonctionnement du jeu (joueur, caisses, murs, cibles)
    :param joueur: liste des personnages
    :param caisses: liste des caisses
    :param cibles: liste des cibles
    :param murs: liste des murs
    :param path: chemin du fichier.txt
    :return:
    """
    x: int = 0
    y: int = 0
    with open(path, "r") as file:
        for ligne in file.readlines():
            for char in ligne:
                if char == '#':
                    mur = creer_mur(x, y)
                    murs.append(mur)

                elif char == '$':
                    caisse = creer_caisse(x, y)
                    caisses.append(caisse)

                elif char == '.':
                    cible = creer_cible(x, y)
                    cibles.append(cible)

                elif char == '@':
                    perso = creer_personnage(x, y)
                    joueur.append(perso)
                x += 1
            x = 0
            y += 1


def definir_mouvement(direction: str, can, joueur: list, murs: list, caisses: list, liste_image: list):
    """
    Fonction permettant de définir les cases de destinations (il y en a 2 si le joueur pousse une caisse) selon la
    direction choisie.
    :param direction: Direction dans laquelle le joueur se déplace (droite, gauche, haut, bas)
    :param can: Canvas (ignorez son fonctionnement), utile uniquement pour créer_image()
    :param joueur: liste des joueurs
    :param murs: liste des murs
    :param caisses: liste des caisses
    :param liste_image: liste des images (murs, caisses etc...) détaillée dans l'énoncé
    :return:
    """
    x: int = joueur[0].get_x()
    y: int = joueur[0].get_y()
    x_caisse: int = 0
    y_caisse: int = 0
    index_caisse: int = -1

    peutBouger: bool = True # Jusqu'à preuve du contraire, le joueur peut bouger -> si il y a un mur ou une caisse, il ne peut pas
    peutBougerCaisse: bool = False # Jusqu'à preuve du contraire, aucune caisse ne peut être bougée

        
    for mur in murs : # Vérification de la position de chaque mur pour voir si il y en a un dans la case adjacente, où le joueur va
        if direction == "haut" :
            peutBouger = caisse_ou_mur_pas_dans_coordonee(x, y - 1, caisses, murs)
            #if mur.get_y() == y - 1 and mur.get_x() == x :
            #    peutBouger = False
            #    break

        elif direction == "bas" :
            peutBouger = caisse_ou_mur_pas_dans_coordonee(x, y + 1, caisses, murs)
            #if mur.get_y() == y + 1 and mur.get_x() == x :
            #    peutBouger = False
            #    break

        elif direction == "gauche" :
            peutBouger = caisse_ou_mur_pas_dans_coordonee(x - 1, y, caisses, murs)
            #if mur.get_x() == x - 1 and mur.get_y() == y  :
            #    peutBouger = False
            #    break

        elif direction == "droite" :
            peutBouger = caisse_ou_mur_pas_dans_coordonee(x + 1, y, caisses, murs)
            #if mur.get_x() == x + 1 and mur.get_y() == y :
            #    peutBouger = False
            #    break

    if peutBouger == False : # Vérification de si une caisse peut être bougée
        for index in range(len(caisses)) :
            if direction == "haut" :
                if caisses[index].get_y() == y - 1 and caisses[index].get_x() == x :
                    peutBougerCaisse = caisse_ou_mur_pas_dans_coordonee(x, y - 2, caisses, murs)
            elif direction == "bas" :
                if caisses[index].get_y() == y + 1 and caisses[index].get_x() == x :
                    peutBougerCaisse = caisse_ou_mur_pas_dans_coordonee(x, y + 2, caisses, murs)
            elif direction == "gauche" :
                if caisses[index].get_x() == x - 1 and caisses[index].get_y() == y :
                    peutBougerCaisse = caisse_ou_mur_pas_dans_coordonee(x - 2, y, caisses, murs)
            elif direction == "droite" :
                if caisses[index].get_x() == x + 1 and caisses[index].get_y() == y :
                    peutBougerCaisse = caisse_ou_mur_pas_dans_coordonee(x + 2, y, caisses, murs)
            index_caisse = index

            if peutBougerCaisse:
                x_caisse = caisses[index].get_x()
                y_caisse = caisses[index].get_y()
                break

        for caisse in caisses :
            if direction == "haut" :
                if caisse.get_y() == y - 1 and caisse.get_x() == x :
                    peutBougerCaisse = caisse_ou_mur_pas_dans_coordonee(x, y - 2, caisses, murs)
            elif direction == "bas" :
                if caisse.get_y() == y + 1 and caisse.get_x() == x :
                    peutBougerCaisse = caisse_ou_mur_pas_dans_coordonee(x, y + 2, caisses, murs)
            elif direction == "gauche" :
                if caisse.get_x() == x - 1 and caisse.get_y() == y :
                    peutBougerCaisse = caisse_ou_mur_pas_dans_coordonee(x - 2, y, caisses, murs)
            elif direction == "droite" :
                if caisse.get_x() == x + 1 and caisse.get_y() == y :
                    peutBougerCaisse = caisse_ou_mur_pas_dans_coordonee(x + 2, y, caisses, murs)
    if peutBouger :
        if direction == "haut":
            y -= 1
            effectuer_mouvement(caisses, murs, joueur, can, 0, 0, x, y, liste_image)

        elif direction == "bas":
            y += 1
            effectuer_mouvement(caisses, murs, joueur, can, 0, 0, x, y, liste_image)

        elif direction == "gauche":
            x -= 1
            effectuer_mouvement(caisses, murs, joueur, can, 0, 0, x, y, liste_image)

        elif direction == "droite":
            x += 1
            effectuer_mouvement(caisses, murs, joueur, can, 0, 0, x, y, liste_image)

    if peutBougerCaisse :
        if direction == "haut":
            y_caisse -= 1
            effectuer_mouvement(caisses, murs, joueur, can, x_caisse, y_caisse, x, y, liste_image, index_caisse)

        elif direction == "bas":
            y_caisse += 1
            effectuer_mouvement(caisses, murs, joueur, can, x_caisse, y_caisse, x, y, liste_image, index_caisse)

        elif direction == "gauche":
            x_caisse -= 1
            effectuer_mouvement(caisses, murs, joueur, can, x_caisse, y_caisse, x, y, liste_image, index_caisse)

        elif direction == "droite":
            x_caisse += 1
            effectuer_mouvement(caisses, murs, joueur, can, x_caisse, y_caisse, x, y, liste_image, index_caisse)

    pass

def caisse_ou_mur_pas_dans_coordonee(coordonee_x: int, coordonee_y: int, caisses: list, murs: list):
    for caisse in caisses :
        if caisse.get_x() == coordonee_x and caisse.get_y() == coordonee_y :
            return False
    for mur in murs:
        if mur.get_x() == coordonee_x and mur.get_y() == coordonee_y :
            return False

    return True
    pass

def effectuer_mouvement(caisses: list, murs: list, joueur: list, can,
                        deplace_caisse_x: int, deplace_caisse_y: int, deplace_joueur_x: int, deplace_joueur_y: int,
                        liste_image: list, ind_caisse: int = -1):
    """
    Fonction permettant d'effectuer le déplacement ou de ne pas l'effectuer si celui-ci n'est pas possible.
    Voir énoncé "Quelques règles".
    Cette methode est appelée par mouvement.
    :param caisses: liste des caisses
    :param murs: liste des murs
    :param joueur: liste des joueurs
    :param can: Canvas (ignorez son fonctionnement), utile uniquement pour créer_image()
    :param deplace_caisse_x: coordonnée à laquelle la caisse va être déplacée en x (si le joueur pousse une caisse)
    :param deplace_caisse_y: coordonnée à laquelle la caisse va être déplacée en y (si le joueur pousse une caisse)
    :param deplace_joueur_x: coordonnée en x à laquelle le joueur va être après le mouvement
    :param deplace_joueur_y: coordonnée en y à laquelle le joueur va être après le mouvement
    :param liste_image: liste des images (murs, caisses etc...) détaillée dans l'énoncé
    :return:
    """
    for j in joueur:
        if j == joueur[0]:
            creer_image(can, joueur[len(joueur) - 1].get_x(), joueur[len(joueur) - 1].get_y(),
                        liste_image[6])  # Remplacement de l'image du joueur par l'image du sol
            joueur.remove(j)
            joueur.append(creer_personnage(deplace_joueur_x,
                                           deplace_joueur_y))  # Création du nouveau joueur avec ses nouvelles valeurs
    if ind_caisse != -1:
        creer_image(can, caisses[ind_caisse].get_x(), caisses[ind_caisse].get_y(),
                    liste_image[6]) # Remplacement de l'image de la caisse par l'image du sol
        caisses.remove(caisses[ind_caisse])
        caisses.append(creer_caisse(deplace_caisse_x,
                                    deplace_caisse_y)) # Création d'une nouvelle caisse avec ses nouvelles valeurs
    pass


def chargement_score(scores_file_path: str, dict_scores: dict):
    """
    Fonction chargeant les scores depuis un fichier.txt et les stockent dans un dictionnaire
    :param scores_file_path: le chemin d'accès du fichier
    :param dict_scores:  le dictionnaire pour le stockage
    :return:
    """
    pass


def maj_score(niveau_en_cours: int, dict_scores: dict) -> str:
    """
    Fonction mettant à jour l'affichage des scores en stockant dans un str l'affichage visible
    sur la droite du jeu.
    ("Niveau x
      1) 7699
      2) ... ").
    :param niveau_en_cours: le numéro du niveau en cours
    :param dict_scores: le dictionnaire pour stockant les scores
    :return str: Le str contenant l'affichage pour les scores ("\n" pour passer à la ligne)
    """
    pass


def calcule_score(temps_initial: float, nb_coups: int, score_base: int) -> int:
    """
    calcule le score du jouer
    :param temps_initial: debut du jeu
    :param nb_coups: nombre des mouvements
    :param score_base: score de base
    :return: le score du jouer
    """
    pass


def enregistre_score(temps_initial: float, nb_coups: int, score_base: int, dict_scores: dict,
                     niveau_en_cours: int):
    """
    Fonction enregistrant un nouveau score réalisé par le joueur. Le calcul de score est le suivant :
    score_base - (temps actuel - temps initial) - (nombre de coups * valeur d'un coup)
    Ce score est arrondi sans virgule et stocké en tant que int. Le score est mis à jour dans le
    dictionnaire.
    :param temps_initial: le temps initialm
    :param nb_coups: le nombre de coups que l'utilisateurs à fait (les mouvements)
    :param score_base: Le score de base identique pour chaque partie
    :param dict_scores: Le dictionnaire stockant les scores
    :param niveau_en_cours: Le numéro du niveau en cours
    """
    pass


def update_score_file(scores_file_path: str, dict_scores: dict):
    """
    Fonction sauvegardant tous les scores dans le fichier.txt.
    :param scores_file_path: le chemin d'accès du fichier de stockage des scores
    :param dict_scores: Le dictionnaire stockant les scores
    :return:
    """
    pass


if __name__ == '__main__':
    simulateur.simulate()
