# ---------------------------------------------------------
# 1. BUBBLE SORT (COMPLEXIDADE: O(n^2))
# Flutua o maior elemento para o final do vetor através de
# trocas adjacentes. Usado como base de comparação.
# ---------------------------------------------------------
def bubble_sort_visual(estoque):
    n = len(estoque)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estoque[j].valor > estoque[j + 1].valor:
                # Troca os elementos de posição no vetor
                estoque[j], estoque[j + 1] = estoque[j + 1], estoque[j]
                
                # Troca as coordenadas visuais para a interface gráfica
                estoque[j].x, estoque[j + 1].x = estoque[j + 1].x, estoque[j].x
                
                yield True # Pausa a execução para renderizar o frame
    yield False


# ---------------------------------------------------------
# 2. BUCKET SORT (COMPLEXIDADE MÉDIA: O(n + k))
# Divide o vetor em 'baldes' baseados em faixas de valor, 
# distribui os elementos e ordena cada balde individualmente.
# ---------------------------------------------------------
def bucket_sort_visual(estoque):
    n = len(estoque)
    if n <= 1:
        yield False
        return

    valor_max = max(item.valor for item in estoque)
    
    # Criação dos baldes
    num_baldes = 5
    baldes = [[] for _ in range(num_baldes)]
    
    # Fase de Distribuição (Scatter)
    for item in estoque:
        indice = int((item.valor / (valor_max + 1)) * num_baldes)
        baldes[indice].append(item)
        
    xs_originais = sorted([item.x for item in estoque])
    
    # Fase de Reagrupamento (Gather)
    idx_atual = 0
    for balde in baldes:
        for item in balde:
            estoque[idx_atual] = item
            estoque[idx_atual].x = xs_originais[idx_atual]
            idx_atual += 1
            yield True # Anima a distribuição inicial dos baldes
            
    # Ordenação Interna (Insertion Sort local)
    inicio_segmento = 0
    for balde in baldes:
        tamanho_balde = len(balde)
        if tamanho_balde > 1:
            for i in range(inicio_segmento + 1, inicio_segmento + tamanho_balde):
                j = i
                while j > inicio_segmento and estoque[j - 1].valor > estoque[j].valor:
                    estoque[j], estoque[j - 1] = estoque[j - 1], estoque[j]
                    estoque[j].x, estoque[j - 1].x = estoque[j - 1].x, estoque[j].x
                    yield True # Anima a ordenação dentro do balde
                    j -= 1
        inicio_segmento += tamanho_balde
        
    yield False


# ---------------------------------------------------------
# 3. COUNTING SORT (COMPLEXIDADE: O(n + k))
# Ordenação linear sem comparações. Conta a frequência de 
# cada elemento e reconstrói o vetor usando os índices.
# ---------------------------------------------------------
def counting_sort_visual(estoque):
    n = len(estoque)
    if n <= 1:
        yield False
        return

    valor_max = max(item.valor for item in estoque)
    
    # Array de frequência
    contagem = [[] for _ in range(valor_max + 1)]

    # Conta as ocorrências
    for item in estoque:
        contagem[item.valor].append(item)

    xs_originais = sorted([item.x for item in estoque])

    # Reconstrói o vetor original
    idx_atual = 0
    for lista_itens in contagem:
        for item in lista_itens:
            estoque[idx_atual] = item
            estoque[idx_atual].x = xs_originais[idx_atual]
            idx_atual += 1
            yield True # Anima a realocação direta da poção

    yield False


# ---------------------------------------------------------
# 4. RADIX SORT (COMPLEXIDADE: O(n * d))
# Ordena processando um dígito de cada vez (unidades, 
# dezenas...), começando do dígito menos significativo.
# ---------------------------------------------------------
def radix_sort_visual(estoque):
    n = len(estoque)
    if n <= 1:
        yield False
        return

    valor_max = max(item.valor for item in estoque)
    xs_originais = sorted([item.x for item in estoque])
    
    exp = 1
    while valor_max // exp > 0:
        output = [None] * n
        contagem = [0] * 10 
        
        for i in range(n):
            indice = (estoque[i].valor // exp) % 10
            contagem[indice] += 1
            
        for i in range(1, 10):
            contagem[i] += contagem[i - 1]
            
        i = n - 1
        while i >= 0:
            indice = (estoque[i].valor // exp) % 10
            output[contagem[indice] - 1] = estoque[i]
            contagem[indice] -= 1
            i -= 1
            
        for i in range(n):
            estoque[i] = output[i]
            estoque[i].x = xs_originais[i]
            yield True # Anima o agrupamento por casa decimal
            
        exp *= 10
        
    yield False