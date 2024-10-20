def analise_vendas(vendas):
    # Total de vendas 
    total_vendas = sum(vendas) 
    # Média mensal, evitando divisão por zero
    media_vendas = total_vendas / len(vendas) if vendas else 0  
    
    return f"{total_vendas}, {media_vendas:.2f}"  # Retorna o total e a média formatada com 2 casas decimais

def obter_entrada_vendas():
    # Entrada em linha única separada por vírgula
    entrada = input("Digite as vendas em linha única separadas por vírgula:")
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(','))) 

    # Método split: divide a string de entrada em elementos separados por vírgula, criando assim uma lista de strings
    # Função map: para converter cada elemento dessa lista de strings em um inteiro neste caso
    # Função list: para converter o objeto map resultante em uma lista de inteiros 
    
    return vendas  # Retorna a lista de vendas

vendas = obter_entrada_vendas()  # Obtém as vendas do usuário
print(analise_vendas(vendas))  # Imprime o resultado da análise

