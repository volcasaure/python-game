import time

from fourni import simulateur
from outils import \
    creer_image, \
    creer_caisse, creer_case_vide, creer_cible, creer_mur, creer_personnage, \
    coordonnee_x, coordonnee_y

# Constantes à utiliser

VALEUR_COUP: int = 50

# Fonctions à développer

def jeu_en_cours(caisses: list, cibles: list) -> bool:
    """
    Fonction qui permet de déterminer si la partie est en cours ou finie
    :param caisses: La liste des caisses du niveau en cours
    :param cibles: La liste des cibles du niveau en cours
    :return: True si la partie est finie, False sinon
    """
    #Déclaration et initialisation des variables
    for i in range(len(cibles)):
        if cibles[i] not in caisses:
            return False
    return True


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
    x = 0
    y = 0
    with open(path, "r") as a:
        for ligne in a.readlines():
            for caracters in ligne:
                if caracters == "#":
                    mur = creer_mur(x, y)
                    murs.append(mur)

                elif caracters == ".":
                    cible = creer_cible(x, y)
                    cibles.append(cible)

                elif caracters == "$":
                    caisse = creer_caisse(x, y)
                    caisses.append(caisse)

                elif caracters == "@":
                    player = creer_personnage(x, y)
                    joueur.append(player)

                x += 1
            x = 0
            y += 1

def definir_mouvement(direction: str, can, joueur: list, murs: list, caisses: list, liste_image: list):
    """
    Fonction permettaant de définir les cases de destinations (il y en a 2 si le joueur pousse une caisse) selon la
    direction choisie.
    :param direction: Direction dans laquelle le joueur se déplace (droite, gauche, haut, bas)
    :param can: Canvas (ignorez son fonctionnement), utile uniquement pour créer_image()
    :param joueur: liste des joueurs
    :param murs: liste des murs
    :param caisses: liste des caisses
    :param liste_image: liste des images (murs, caisses etc...) détaillée dans l'énoncé
    :return:
    """
    #Déclaration et initialisation des variables
    coordonnee_destination: int = 0
    deplace_caisse_x = None
    deplace_caisse_y = None


    if direction == "gauche":
        coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]) - 1,
                                                  coordonnee_y(joueur[len(joueur) - 1]))
    elif direction == "droite":
        coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]) + 1,
                                                  coordonnee_y(joueur[len(joueur) - 1]))
    elif direction == "haut":
        coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                  coordonnee_y(joueur[len(joueur) - 1]) - 1)
    elif direction == "bas":
        coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                  coordonnee_y(joueur[len(joueur) - 1]) + 1)
    for lmn in caisses:
        for elt in murs:

            if direction == "gauche":
                if coordonnee_x(joueur[len(joueur) - 1]) - 1 and coordonnee_y(joueur[len(joueur) - 1]) == elt:
                    coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                              coordonnee_y(joueur[len(joueur) - 1]))
                if coordonnee_x(joueur[len(joueur) - 1]) - 1 and coordonnee_y(joueur[len(joueur) - 1]) == lmn:
                    if coordonnee_x(joueur[len(joueur) - 1]) - 2 and coordonnee_y(joueur[len(joueur) - 1]) == elt or lmn:
                        coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                                  coordonnee_y(joueur[len(joueur) - 1]))


            if direction == "droite":
                if coordonnee_x(joueur[len(joueur) - 1]) + 1 and coordonnee_y(joueur[len(joueur) - 1]) == elt:
                    coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                              coordonnee_y(joueur[len(joueur) - 1]))
                if coordonnee_x(joueur[len(joueur) - 1]) + 1 and coordonnee_y(joueur[len(joueur) - 1]) == lmn:
                    if coordonnee_x(joueur[len(joueur) - 1]) + 2 and coordonnee_y(joueur[len(joueur) - 1]) == elt or lmn:
                        coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                                  coordonnee_y(joueur[len(joueur) - 1]))

            if direction == "haut":
                if coordonnee_x(joueur[len(joueur) - 1]) and coordonnee_y(joueur[len(joueur) - 1]) - 1 == elt:
                    coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                              coordonnee_y(joueur[len(joueur) - 1]))
                if coordonnee_x(joueur[len(joueur) - 1]) and coordonnee_y(joueur[len(joueur) - 1]) - 1 == lmn:
                    if coordonnee_x(joueur[len(joueur) - 1]) and coordonnee_y(joueur[len(joueur) - 1]) - 2 == elt or lmn:
                        coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                                  coordonnee_y(joueur[len(joueur) - 1]))


            if direction == "bas":
                if coordonnee_x(joueur[len(joueur) - 1]) and coordonnee_y(joueur[len(joueur) - 1]) + 1 == elt:
                    coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                              coordonnee_y(joueur[len(joueur) - 1]))
                if coordonnee_x(joueur[len(joueur) - 1]) and coordonnee_y(joueur[len(joueur) - 1]) + 1 == lmn:
                    if coordonnee_x(joueur[len(joueur) - 1]) and coordonnee_y(joueur[len(joueur) - 1]) + 2 == elt or lmn:
                        coordonnee_destination = creer_personnage(coordonnee_x(joueur[len(joueur) - 1]),
                                                                  coordonnee_y(joueur[len(joueur) - 1]))


    deplace_joueur_x = coordonnee_x(coordonnee_destination)
    deplace_joueur_y = coordonnee_y(coordonnee_destination)

    # Appel de la fonction effectuer_mouvemement
    effectuer_mouvement(caisses, murs, joueur, can,
                        deplace_caisse_x, deplace_caisse_y, deplace_joueur_x, deplace_joueur_y, liste_image)


def effectuer_mouvement(caisses: list, murs: list, joueur: list, can,
                        deplace_caisse_x: int, deplace_caisse_y: int, deplace_joueur_x: int, deplace_joueur_y: int,
                        liste_image: list):
    """
    Fonction permettant d'effectuer le déplacement ou de ne pas l'effectuer si celui-ci n'est pas possible. Voir énoncé
    "Quelques règles". Cette methode est appelée par mouvement.
    :param coordonnee_destination: variable CaseVide ayant possiblement des coordonnées identiques à une autre variable
    (murs, caisse, casevide)
    :param coordonnee_case_suivante: variable CaseVide ayant possiblement des coordonnées identiques à une autre variable
    (murs, caisse, casevide) mais représente la case après coordonnee_destination
    :param ancienne_caisse: variable utile pour supprimer l'ancienne caisse (après avoir déplacé celle-ci)
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


def enregistre_score(temps_initial: float, nb_coups: int, score_base: int, dict_scores: dict,
                     niveau_en_cours: int) -> int:
    """
    Fonction enregistrant un nouveau score réalisé par le joueur. Le calcul de score est le suivant :
    score_base - (temps actuel - temps initial) - (nombre de coups * valeur d'un coup)
    Ce score est arrondi sans virgule et stocké en tant que int.
    :param temps_initial: le temps initial
    :param nb_coups: le nombre de coups que l'utilisateurs à fait (les mouvements)
    :param score_base: Le score de base identique pour chaque partie
    :param dict_scores: Le dictionnaire stockant les scores
    :param niveau_en_cours: Le numéro du niveau en cours
    :return: le score sous forme d'un int
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
