def bubble_sort_visual(estoque):
    """Algoritmo base de ordenação manual (Trocas adjacentes)."""
    n = len(estoque)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estoque[j].valor > estoque[j + 1].valor:
                estoque[j], estoque[j + 1] = estoque[j + 1], estoque[j]
                estoque[j].x, estoque[j + 1].x = estoque[j + 1].x, estoque[j].x
                yield True 
    yield False

def bucket_sort_visual(estoque):
    """Algoritmo Bucket Sort: Distribui os itens em baldes e ordena cada balde."""
    n = len(estoque)
    if n <= 1:
        yield False
        return

    valor_max = max(item.valor for item in estoque)
    num_baldes = 5
    baldes = [[] for _ in range(num_baldes)]
    
    for item in estoque:
        indice = int((item.valor / (valor_max + 1)) * num_baldes)
        baldes[indice].append(item)
        
    xs_originais = sorted([item.x for item in estoque])
    
    idx_atual = 0
    for balde in baldes:
        for item in balde:
            estoque[idx_atual] = item
            estoque[idx_atual].x = xs_originais[idx_atual]
            idx_atual += 1
            yield True 
            
    inicio_segmento = 0
    for balde in baldes:
        tamanho_balde = len(balde)
        if tamanho_balde > 1:
            for i in range(inicio_segmento + 1, inicio_segmento + tamanho_balde):
                j = i
                while j > inicio_segmento and estoque[j - 1].valor > estoque[j].valor:
                    estoque[j], estoque[j - 1] = estoque[j - 1], estoque[j]
                    estoque[j].x, estoque[j - 1].x = estoque[j - 1].x, estoque[j].x
                    yield True 
                    j -= 1
        inicio_segmento += tamanho_balde
        
    yield False

def counting_sort_visual(estoque):
    """
    Algoritmo Counting Sort: Conta a frequência dos valores e os aloca diretamente
    em suas posições finais sem comparações diretas.
    """
    n = len(estoque)
    if n <= 1:
        yield False
        return

    valor_max = max(item.valor for item in estoque)
    contagem = [[] for _ in range(valor_max + 1)]

    for item in estoque:
        contagem[item.valor].append(item)

    xs_originais = sorted([item.x for item in estoque])

    idx_atual = 0
    for lista_itens in contagem:
        for item in lista_itens:
            estoque[idx_atual] = item
            estoque[idx_atual].x = xs_originais[idx_atual]
            idx_atual += 1
            yield True 

    yield False

def radix_sort_visual(estoque):
    """
    Algoritmo Radix Sort: Ordena os elementos processando os dígitos individualmente.
    Começa pelas unidades, depois dezenas, centenas, etc.
    """
    n = len(estoque)
    if n <= 1:
        yield False
        return

    valor_max = max(item.valor for item in estoque)
    xs_originais = sorted([item.x for item in estoque])
    
    # O exp é 1 para as unidades, 10 para as dezenas, 100 para centenas...
    exp = 1
    while valor_max // exp > 0:
        # Sub-rotina de Counting Sort baseada apenas no dígito atual
        output = [None] * n
        contagem = [0] * 10
        
        # Conta as ocorrências do dígito
        for i in range(n):
            indice = (estoque[i].valor // exp) % 10
            contagem[indice] += 1
            
        # Calcula as posições exatas no array de saída
        for i in range(1, 10):
            contagem[i] += contagem[i - 1]
            
        # Constrói o array de saída ordenado pelo dígito atual (lendo de trás para frente para manter a estabilidade)
        i = n - 1
        while i >= 0:
            indice = (estoque[i].valor // exp) % 10
            output[contagem[indice] - 1] = estoque[i]
            contagem[indice] -= 1
            i -= 1
            
        # Aplica a ordenação parcial ao estoque e anima a troca
        for i in range(n):
            estoque[i] = output[i]
            estoque[i].x = xs_originais[i]
            yield True
            
        exp *= 10
        
    yield False