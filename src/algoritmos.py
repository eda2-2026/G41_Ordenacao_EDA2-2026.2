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