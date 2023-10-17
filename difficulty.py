def set_difficulty(difficulty):
    """Trois niveau de difficulté :
        Sympa / Sévère / Mystère"""
    opts = ["sympa", "severe", "mystere"]


    diff = 0
    if difficulty == "sympa":
        diff = 1
    elif difficulty == "severe":
        diff = 2
    else:
        diff = 3
    return diff


"""
Le param Q est le paramètre qui permet de savoir à quel questions on se trouve
Le param D est le niveau de difficulté choisi avant (1, 2 ou 3)
"""
def quoting(answer, q, d):
    return False

