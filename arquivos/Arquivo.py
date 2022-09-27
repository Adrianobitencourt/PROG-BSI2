
def dados():
    with open('Judas:Romance lirico em quatro jornadas.txt') as file:
        texto = file.read().lower()
        return texto        

def limpaDados():
    Limpeza = [c for c in dados() if c.isalpha()]
    return Limpeza

def letraunica():
    LetrasSolo = {}
    for letra in limpaDados():
        LetrasSolo[letra] = LetrasSolo.get(letra, 0) + 1
    return LetrasSolo


if __name__ == '__main__':

    from collections import Counter
    lestrasMaisComun = Counter(letraunica())
    dado = dados()
    limpadado = limpaDados()
    letrasunicas = letraunica()

    import matplotlib.pyplot as plt

    rotulos, valores = zip(*lestrasMaisComun.most_common(10))
    plt.title('Frequencia de letras em portugues')
    plt.bar(rotulos, valores)
    plt.show()
    plt.savefig('top_dominios.png')
    plt.close()

    print (f'\n{len(dado)} characters carregados')

    print(f'com a limpeza {len(limpadado)} characters carregados\n')

    print (f'Quanditades de letras unicas no texto:{len(letrasunicas)}\n')

