import pandas as pd

def Preencher_Tabela(df):
    #cria uma matriz com zeros de tamanho (quantidade de itens+1 x capacidade+1)
    matrix = pd.DataFrame(0, index= (['Vazia']+list(df['Item'])), columns=range(capacidade+1))

    #matrix[coluna][linha]
    for i in range(1, len(df['Item'])+1):
        for j in range(1, capacidade+1):
            #se o peso do item atual for menor igual a capacidade atual da mochila
            if df['Peso'][i-1] <= j:
                                  #valor anterior #valor do item atual + #valor da linha acima na coluna (capacidade atual - peso do item atual)
                matrix[j][i] = max(matrix[j][i-1], df['Valor'][i-1] + matrix[j-df['Peso'][i-1]][i-1])#escolhe o maximo entre o valor imediatamente acima ou o do item atual + valor da melhor solução para a capacidade atual menos o peso do item
            else:
                matrix[j][i] = matrix[j][i-1] #valor da solução anterior acima
    return matrix

def Solucao(matrix, df):
    itens = []
    linhas, colunas = matrix.shape
    # 'i e j' são os indices do elemento final da matriz 
    i = linhas - 1
    j = colunas - 1 

    while i>0:
        #se a 'linha atual for toda de zeros' ou 'a coluna atual é a 0' quebra o loop
        if (matrix.iloc[i] == 0).all() or j==0:
            break
        else:
            #se o item atual é melhor que o imediatamente acima
            if matrix[j][i]> matrix[j][i-1]:
                itens.append(df['Item'][i-1]) #adiciona o item na lista
                j-= df['Peso'][i-1] #subtrai da capacidade daqui para frente o peso do item atual
                i-=1 #vai para a linha acima
            else:
                i-=1 #vai para a linha acima, mesma coluna
    
    #retorna os itens da lista e o ultimo elemento da matriz
    return itens, matrix[colunas-1][linhas-1]

if __name__ == '__main__':

    capacidade = 7

    itens = {
        'Item': ['joia', 'celular', 'tablet', 'notebook', 'som'],
        'Valor': [2, 2, 4, 5, 3],
        'Peso': [3, 1, 3, 4, 2]
    }

    df_mochila = pd.DataFrame(itens)
    print("\n",df_mochila,"\n")
    
    #preenche a tabela
    matrix = Preencher_Tabela(df_mochila)
    print(matrix)

    #percorre a tabela e busca a solução
    solucao, total = Solucao(matrix, df_mochila)
    print(f'\nSolução: {solucao}')
    print(f'Valor total: {total}')