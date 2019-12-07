import numpy as np

#intenção de usar metodos parecido com pandas
def read_csv(url):
    return np.genfromtxt(url, delimiter=',', dtype='|S20', encoding=None, skip_header=1)


# Mostra os 5 primeiros itens do dataset por default
def head(dataset, quantidade=5):
    print(dataset[:quantidade + 1])


# Mostra os 5 ultimos itens do dataset por default
def tail(dataset, quantidade=5):
    print(dataset[-quantidade:])


# Busca todas as gerações e a quantidade de pokemons em cada uma delas
def getGens(poke):
    gen = poke[:, 8].astype('str')
    return np.unique(gen, return_counts=True)


# Busca todos os tipos_1 e a quantidade de pokemons em cada um desses tipos
def getTypes_1(poke):
    types1 = poke[:, 1].astype('str')
    print(np.unique(types1, return_counts=True))


# Busca todos os tipos_1 e a quantidade de pokemons em cada um desses tipos
def getTypes_2(poke):
    types2 = poke[:, 2].astype('str')
    print(np.unique(types2, return_counts=True))


def getHeights(pok):
    return pok[:, 13].astype('float')


def getWeitghts(pok):
    return pok[:, 14].astype('float')


# Mostra a média, mediana e percentil da altura
def getSummerizeHeights(pok):
    pesos = getHeights(pok)
    print(f"Peso Média: {pesos.mean():.2f}")
    print(f"Peso Mediana: {np.median(pesos):.2f}")
    print(f"25th Percentil: {np.percentile(pesos, 25):.2f}")
    print(f"75th Percentil: {np.percentile(pesos, 75):.2f}")


# Mostra a média, mediana e percentil do peso
def getSummerizeWeights(pok):
    pesos = getWeitghts(pok)
    print(f"Altura Média: {pesos.mean():.2f}")
    print(f"Altura Mediana: {np.median(pesos):.2f}")
    print(f"25th Percentil: {np.percentile(pesos, 25):.2f}")
    print(f"75th Percentil: {np.percentile(pesos, 75):.2f}")


# Mostra os pokemons com maior poder, hp, ataque e defesa...
def summarize(pok):
    nomes = pok[:, 0].astype('|S20')
    total = pok[:, 3].astype('float')
    hp = pok[:, 4].astype('float')
    ataque = pok[:, 5].astype('float')
    defesa = pok[:, 6].astype('float')
    velocidade = pok[:, 7].astype('float')

    print("********************************************************")
    print(f"Pokemon {nomes[total == total.max()]}  com maior poder:{total.max():.2f}")
    print(f"Pokemon {nomes[hp == hp.max()]}  com maior hp:{hp.max():.2f}")
    print(f"Pokemon {nomes[ataque == ataque.max()]}  com maior ataque:{ataque.max():.2f}")
    print(f"Pokemon {nomes[defesa == defesa.max()]}  com maior defesa:{defesa.max():.2f}")
    print(f"Pokemon {nomes[velocidade == velocidade.max()]}  com maior velocidade:{velocidade.max():.2f}")
    print("********************************************************")
    getSummerizeHeights(pok)
    getSummerizeWeights(pok)



# Mostra quantidades de pokemons lendarios e quais sao eles
def getLegendaries(poke):
    quantidade = np.count_nonzero(poke[:, 9].astype('int') == 1)
    print(f"Existem {quantidade:d} pokemons lendários")
    legendaries = (poke[:, 9].astype('int') == 1)
    for x in poke[legendaries, 0]:
        print(x)


# ordena os nomes dos pokemons em ordem alfabetica
def sortbyName(poke):
    nomesOrdenados = np.sort(poke[:, 0])
    for x in nomesOrdenados:
        print(x)


def correlac(valor1, valor2):
    return np.corrcoef(valor1, valor2)
