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
    """
    Algoritmo Bucket Sort: Distribui os itens em baldes e ordena cada balde.
    """
    n = len(estoque)
    if n <= 1:
        yield False
        return

    # 1. Encontrar o valor máximo para definir o tamanho dos intervalos
    valor_max = max(item.valor for item in estoque)
    
    # Vamos criar 5 "baldes" conceituais
    num_baldes = 5
    baldes = [[] for _ in range(num_baldes)]
    
    # 2. Distribuição: Colocar cada item no seu balde correspondente
    for item in estoque:
        # Calcula o índice do balde (0 a 4)
        indice = int((item.valor / (valor_max + 1)) * num_baldes)
        baldes[indice].append(item)
        
    # Salvar as coordenadas X originais para os itens não saírem do lugar na tela
    xs_originais = sorted([item.x for item in estoque])
    
    # 3. Remontar o estoque agrupado pelos baldes (Ainda não ordenado internamente)
    idx_atual = 0
    for balde in baldes:
        for item in balde:
            estoque[idx_atual] = item
            # Atualiza o X para a nova posição no grupo e renderiza o frame
            estoque[idx_atual].x = xs_originais[idx_atual]
            idx_atual += 1
            yield True # Anima a distribuição inicial
            
    # 4. Ordenar cada balde individualmente (Usando Insertion Sort)
    inicio_segmento = 0
    for balde in baldes:
        tamanho_balde = len(balde)
        if tamanho_balde > 1:
            # Ordena apenas o segmento correspondente a este balde na prateleira
            for i in range(inicio_segmento + 1, inicio_segmento + tamanho_balde):
                j = i
                while j > inicio_segmento and estoque[j - 1].valor > estoque[j].valor:
                    # Troca os itens
                    estoque[j], estoque[j - 1] = estoque[j - 1], estoque[j]
                    # Troca as posições X na tela
                    estoque[j].x, estoque[j - 1].x = estoque[j - 1].x, estoque[j].x
                    yield True # Anima a troca interna do balde
                    j -= 1
        inicio_segmento += tamanho_balde
        
    yield False