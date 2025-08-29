import pandas as pd
import numpy as np

global m
def calc_C(X, U):
    lista = []
    for i, uu in enumerate(U):
        lista.append([])
        for j in range(len(X)):
            lista[i].append(calc_V(X[j],uu))
    return lista

def calc_dist(xyz: list, CK: list):
    b = 0
    for i, cord in enumerate(xyz):
        b+= (CK[i] - cord)**(2)
    return (b)**0.5

def calc_V(X,U1):
    i = 0
    soma1 = 0
    soma2 = 0
    for u in U1:
        soma1 += (X[i] * u**m)
        soma2 += u**m
        i+=1
    if soma2 == 0:
        print("zero soma2 calc_v)")
    return soma1/soma2

def calc_perti(cords, C, I):
    dists = []
    soma = 0
    global m
    for c in C:
        dists.append(calc_dist(cords, c))
    I = calc_dist(cords, I)
    
    for i in range(len(C)):
        soma += (I/dists[i])**(2/(m-1))
    return 1/soma

def calc_novo_u(dados, C):
    num_licoes = len(dados[0])
    US = [[] for _ in range(len(C))]

    for i in range(num_licoes):
        passar = []
        for dado in dados:
            passar.append(dado[i])
        for us in range(len(C)):
            US[us].append(calc_perti(passar, C, C[us]))
    return US



def K_FUZZY(dataf, num_clusters, rodadas_max=100):
    global m
    m = 2 # Fuzzificação, não deve ser menor que 2!
    
    dataf

    X = [data[nome] for nome in data.columns]

    
    U = [[np.random.random() for _ in range(len(X))] for kk in range(num_clusters)]
    for i in range(rodadas_max):
        CENTR = calc_C(X, U)
        U = calc_novo_u(X, CENTR)
    U_round = [[round(x) for x in linha] for linha in U]
    for i in range(len(U_round)):
        U_round[i] = np.array(U_round[i])
        U_round[i] *= (i+1)
    U_round = sum(U_round)
    dataf['cluster'] = U_round
    return dataf


# data deve conter seu dataframe de dados já tratados
data = pd.read_excel("NAZEMI.xlsx")


if __name__ == "__main__":
    K_FUZZY(dataf=data, num_clusters=10, rodadas_max=100).to_excel("resultado.xlsx", index=False) # A função retorna um dataframe atualizado com a coluna 'cluster' adicionada



