def bubble_sort_visual(estoque):
    """
    Algoritmo base de ordenação manual usando yield para animação.
    Será substituído gradualmente pelos algoritmos do Módulo 2.
    """
    n = len(estoque)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estoque[j].valor > estoque[j + 1].valor:
                # Troca manual (sem usar sort nativo)
                estoque[j], estoque[j + 1] = estoque[j + 1], estoque[j]
                
                # Troca de coordenadas X para a interface visual
                estoque[j].x, estoque[j + 1].x = estoque[j + 1].x, estoque[j].x
                
                yield True 
    yield False