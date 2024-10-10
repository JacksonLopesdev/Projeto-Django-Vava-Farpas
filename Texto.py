def print_art(letra):
    art = {
        'A': [
            "────────────────",
            "─██████████████─",
            "─██░░░░░░░░░░██─",
            "─██░░██████░░██─",
            "─██░░██──██░░██─",
            "─██░░██████░░██─",
            "─██░░░░░░░░░░██─",
            "─██░░██████░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██████──██████─",
            "────────────────"
        ],
        'B': [
            "──────────────────",
            "─██████████████───",
            "─██░░░░░░░░░░██───",
            "─██░░██████░░██───",
            "─██░░██──██░░██───",
            "─██░░██████░░████─",
            "─██░░░░░░░░░░░░██─",
            "─██░░████████░░██─",
            "─██░░██────██░░██─",
            "─██░░████████░░██─",
            "─██░░░░░░░░░░░░██─",
            "─████████████████─",
            "──────────────────"
        ],
        'C': [
            "────────────────",
            "─██████████████─",
            "─██░░░░░░░░░░██─",
            "─██░░██████████─",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██████████─",
            "─██░░░░░░░░░░██─",
            "─██████████████─",
            "────────────────"
        ],
        'D': [
            "────────────────",
            "─████████████───",
            "─██░░░░░░░░████─",
            "─██░░████░░░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░████░░░░██─",
            "─██░░░░░░░░████─",
            "─████████████───",
            "────────────────"
        ],
        'E': [
            "────────────────",
            "─██████████████─",
            "─██░░░░░░░░░░██─",
            "─██░░██████████─",
            "─██░░██─────────",
            "─██░░██████████─",
            "─██░░░░░░░░░░██─",
            "─██░░██████████─",
            "─██░░██─────────",
            "─██░░██████████─",
            "─██░░░░░░░░░░██─",
            "─██████████████─",
            "────────────────"
        ],
        'F': [
            "────────────────",
            "─██████████████─",
            "─██░░░░░░░░░░██─",
            "─██░░██████████─",
            "─██░░██████████─",
            "─██░░██████████─",
            "─██░░░░░░░░████─",
            "─██░░██████████─",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██████─────────",
            "────────────────"
        ],
        'G': [
            "────────────────",
            "─██████████████─",
            "─██░░░░░░░░░░██─",
            "─██░░██████████─",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██──██████─",
            "─██░░██──██░░██─",
            "─██░░██████░░██─",
            "─██░░░░░░░░░░██─",
            "─██████████████─",
            "────────────────"
        ],
        'H': [
            "────────────────",
            "─██████──██████─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██████░░██─",
            "─██░░░░░░░░░░██─",
            "─██░░██████░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██████──██████─",
            "────────────────"
        ],
        'I': [
            "────────────",
            "─██████████─",
            "─██░░░░░░██─",
            "─████░░████─",
            "───██░░██───",
            "───██░░██───",
            "───██░░██───",
            "───██░░██───",
            "───██░░██───",
            "─████░░████─",
            "─██░░░░░░██─",
            "─██████████─",
            "────────────"
        ],
        'J': [
            "────────────────",
            "─────────██████─",
            "─────────██░░██─",
            "─────────██░░██─",
            "─────────██░░██─",
            "─────────██░░██─",
            "─────────██░░██─",
            "─██████──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██████░░██─",
            "─██░░░░░░░░░░██─",
            "─██████████████─",
            "────────────────"
        ],
        'K': [
            "──────────────────",
            "─██████──████████─",
            "─██░░██──██░░░░██─",
            "─██░░██──██░░████─",
            "─██░░██──██░░██───",
            "─██░░██████░░██───",
            "─██░░░░░░░░░░██───",
            "─██░░██████░░██───",
            "─██░░██──██░░██───",
            "─██░░██──██░░████─",
            "─██░░██──██░░░░██─",
            "─██████──████████─",
            "──────────────────"
        ],
        'L': [
            "────────────────",
            "─██████─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██████████─",
            "─██░░░░░░░░░░██─",
            "─██████████████─",
            "────────────────"
        ],
        'M': [
            "────────────────────────",
            "─██████──────────██████─",
            "─██░░██████████████░░██─",
            "─██░░░░░░░░░░░░░░░░░░██─",
            "─██░░██████░░██████░░██─",
            "─██░░██████░░██████░░██─",
            "─██░░██──██░░██──██░░██─",
            "─██░░██──██░░██──██░░██─",
            "─██░░██──██████──██░░██─",
            "─██░░██──────────██░░██─",
            "─██░░██──────────██░░██─",
            "─██████──────────██████─",
            "────────────────────────"
        ],
        'N': [
            "────────────────────────",
            "─██████──────────██████─",
            "─██░░██████████──██░░██─",
            "─██░░░░░░░░░░██──██░░██─",
            "─██░░██████░░██──██░░██─",
            "─██░░██──██░░██──██░░██─",
            "─██░░██──██░░██──██░░██─",
            "─██░░██──██░░██──██░░██─",
            "─██░░██──██░░██████░░██─",
            "─██░░██──██░░░░░░░░░░██─",
            "─██░░██──██████████░░██─",
            "─██████──────────██████─",
            "────────────────────────"
        ],
        'O': [
            "──────────────────",
            "─████████████████─",
            "─██░░░░░░░░░░░░██─",
            "─██░░████████░░██─",
            "─██░░██────██░░██─",
            "─██░░██────██░░██─",
            "─██░░██────██░░██─",
            "─██░░██────██░░██─",
            "─██░░██────██░░██─",
            "─██░░████████░░██─",
            "─██░░░░░░░░░░░░██─",
            "─████████████████─",
            "──────────────────"
        ],
        'P': [
            "────────────────",
            "─██████████████─",
            "─██░░░░░░░░░░██─",
            "─██░░██████░░██─",
            "─██░░██──██░░██─",
            "─██░░██████░░██─",
            "─██░░░░░░░░░░██─",
            "─██░░██████████─",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██░░██─────────",
            "─██████─────────",
            "────────────────"
        ],
        'Q': [
            "──────────────────",
            "─██████████████───",
            "─██░░░░░░░░░░██───",
            "─██░░██████░░██───",
            "─██░░██──██░░██───",
            "─██░░██──██░░██───",
            "─██░░██──██░░██───",
            "─██░░██──██░░██───",
            "─██░░██──██░░██───",
            "─██░░██████░░████─",
            "─██░░░░░░░░░░░░██─",
            "─████████████████─",
            "──────────────────"
        ],
        'R': [
            "        ",
            "─████████████████───",
            "─██░░░░░░░░░░░░██───",
            "─██░░████████░░██───",
            "─██░░██────██░░██───",
            "─██░░████████░░██───",
            "─██░░░░░░░░░░░░██───",
            "─██░░██████░░████───",
            "─██░░██──██░░██─────",
            "─██░░██──██░░██████─",
            "─██░░██──██░░░░░░██─",
            "─██████──██████████─",
            "        "
        ],
        'S': [
            "────────────────",
            "─██████████████─",
            "─██░░░░░░░░░░██─",
            "─██░░██████████─",
            "─██░░██─────────",
            "─██░░██████████─",
            "─██░░░░░░░░░░██─",
            "─██████████░░██─",
            "─────────██░░██─",
            "─██████████░░██─",
            "─██░░░░░░░░░░██─",
            "─██████████████─",
            "────────────────"
        ],
        'T': [
            "────────────────",
            "─██████████████─",
            "─██░░░░░░░░░░██─",
            "─██████░░██████─",
            "─────██░░██─────",
            "─────██░░██─────",
            "─────██░░██─────",
            "─────██░░██─────",
            "─────██░░██─────",
            "─────██░░██─────",
            "─────██░░██─────",
            "─────██████─────",
            "────────────────"
        ],
        'U': [
            "────────────────",
            "─██████──██████─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██████░░██─",
            "─██░░░░░░░░░░██─",
            "─██████████████─",
            "────────────────"
        ],
        'V': [
            "────────────────",
            "─██████──██████─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░██──██░░██─",
            "─██░░░░██░░░░██─",
            "─████░░░░░░████─",
            "───████░░████───",
            "─────██████─────",
            "────────────────"
        ],
        'W': [
            "────────────────────────",
            "─██████──────────██████─",
            "─██░░██──────────██░░██─",
            "─██░░██──────────██░░██─",
            "─██░░██──────────██░░██─",
            "─██░░██──██████──██░░██─",
            "─██░░██──██░░██──██░░██─",
            "─██░░██──██░░██──██░░██─",
            "─██░░██████░░██████░░██─",
            "─██░░░░░░░░░░░░░░░░░░██─",
            "─██░░██████░░██████░░██─",
            "─██████──██████──██████─",
            "────────────────────────"
        ],
        'X': [
            "        ",
            "─████████──████████─",
            "─██░░░░██──██░░░░██─",
            "─████░░██──██░░████─",
            "───██░░░░██░░░░██───",
            "───████░░░░░░████───",
            "─────██░░░░░░██─────",
            "───████░░░░░░████───",
            "───██░░░░██░░░░██───",
            "─████░░██──██░░████─",
            "─██░░░░██──██░░░░██─",
            "─████████──████████─",
            "        "
        ],
        'Y': [
            "        ",
            "─████████──████████─",
            "─██░░░░██──██░░░░██─",
            "─████░░██──██░░████─",
            "───██░░░░██░░░░██───",
            "───████░░░░░░████───",
            "─────████░░████─────",
            "───────██░░██───────",
            "───────██░░██───────",
            "───────██░░██───────",
            "───────██░░██───────",
            "───────██████───────",
            "        "
        ],
        'Z': [
            "        ",
            "─██████████████████─",
            "─██░░░░░░░░░░░░░░██─",
            "─████████████░░░░██─",
            "─────────████░░████─",
            "───────████░░████───",
            "─────████░░████─────",
            "───████░░████───────",
            "─████░░████─────────",
            "─██░░░░████████████─",
            "─██░░░░░░░░░░░░░░██─",
            "─██████████████████─",
            "        "
        ],
        ' ': [
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",       
        ],
    }

    letra = letra.upper()
    if letra in art:
        return art[letra]
    else:
        return ["Letra inválida!"]


def art_frase(frase):
    linhas = [""] * 13  

    for letra in frase:
        arte_letra = print_art(letra)
        if arte_letra[0] == "Letra inválida!":
            continue  
        for i in range(13):
            linhas[i] += arte_letra[i] 

    for linha in linhas:
        print(linha)


art_frase('facio ggez')