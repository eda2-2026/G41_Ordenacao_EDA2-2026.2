import pygame
import sys
import random
import os

# Importações dos módulos separados
from src.item import ItemTaverna
from src.algoritmos import bubble_sort_visual, bucket_sort_visual

# Constantes
LARGURA = 1024
ALTURA = 768
FPS = 60
COR_FUNDO = (43, 30, 22)
COR_PRATELEIRA = (92, 64, 51)

def gerar_estoque(quantidade):
    estoque = []
    margem = 90
    largura_util = LARGURA - (margem * 2)
    largura_item = largura_util // quantidade
    
    for i in range(quantidade):
        valor = random.randint(10, 100)
        x = margem + (i * largura_item)
        y = ALTURA - 280 
        estoque.append(ItemTaverna(valor, x, y, largura_item, 250))
    return estoque

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("🍻 Organizador de Taverna - Ordenação Mágica")
    relogio = pygame.time.Clock()
    
    # Fonte para o HUD de atalhos
    fonte_hud = pygame.font.Font(None, 24)

    usar_bg = False
    fundo_img = None
    
    possiveis_nomes_bg = [
        "Background.jpg", "Background.jpeg", "Background.png",
        "background.jpg", "background.jpeg", "background.png",
        "Background.jpg.jpg"
    ]
    
    for nome in possiveis_nomes_bg:
        caminho_bg = os.path.join("assets", nome)
        if os.path.exists(caminho_bg):
            try:
                fundo_img = pygame.image.load(caminho_bg).convert()
                fundo_img = pygame.transform.scale(fundo_img, (LARGURA, ALTURA))
                usar_bg = True
                break
            except pygame.error:
                continue

    estoque_atual = gerar_estoque(15)
    ordenando = False
    gerador_ordenacao = None

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if evento.type == pygame.KEYDOWN:
                # ESPAÇO: Gera novo estoque
                if evento.key == pygame.K_SPACE and not ordenando:
                    estoque_atual = gerar_estoque(15)
                
                # ENTER: Bubble Sort
                if evento.key == pygame.K_RETURN and not ordenando:
                    ordenando = True
                    gerador_ordenacao = bubble_sort_visual(estoque_atual)
                    
                # B: Bucket Sort
                if evento.key == pygame.K_b and not ordenando:
                    ordenando = True
                    gerador_ordenacao = bucket_sort_visual(estoque_atual)

        if ordenando and gerador_ordenacao is not None:
            try:
                next(gerador_ordenacao)
            except StopIteration:
                ordenando = False
                gerador_ordenacao = None

        # Renderização do Fundo
        if usar_bg and fundo_img:
            tela.blit(fundo_img, (0, 0))
        else:
            tela.fill(COR_FUNDO)
            pygame.draw.rect(tela, COR_PRATELEIRA, (0, ALTURA - 100, LARGURA, 100))

        # Renderização dos Itens
        for item in estoque_atual:
            item.desenhar(tela)
            
        # Renderização do HUD de Atalhos
        painel_rect = pygame.Rect(15, 15, 260, 110)
        pygame.draw.rect(tela, COR_FUNDO, painel_rect, border_radius=8)
        pygame.draw.rect(tela, (230, 215, 180), painel_rect, width=2, border_radius=8)
        
        textos_hud = [
            "📜 Grimório de Atalhos:",
            "[ESPAÇO] Embaralhar Poções",
            "[ENTER] Bubble Sort",
            "[ B ] Bucket Sort"
        ]
        
        for i, linha in enumerate(textos_hud):
            cor_texto = (230, 215, 180) if i == 0 else (255, 255, 255)
            surf_texto = fonte_hud.render(linha, True, cor_texto)
            tela.blit(surf_texto, (30, 25 + (i * 22)))

        pygame.display.flip()
        
        if ordenando:
            relogio.tick(15) 
        else:
            relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()