import pygame
import sys
import random
import os

# Importações dos módulos separados
from src.item import ItemTaverna
from src.algoritmos import bubble_sort_visual

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
                if evento.key == pygame.K_SPACE and not ordenando:
                    estoque_atual = gerar_estoque(15)
                
                # Controle de execução da ordenação
                if evento.key == pygame.K_RETURN and not ordenando:
                    ordenando = True
                    gerador_ordenacao = bubble_sort_visual(estoque_atual)

        if ordenando and gerador_ordenacao is not None:
            try:
                next(gerador_ordenacao)
            except StopIteration:
                ordenando = False
                gerador_ordenacao = None

        if usar_bg and fundo_img:
            tela.blit(fundo_img, (0, 0))
        else:
            tela.fill(COR_FUNDO)
            pygame.draw.rect(tela, COR_PRATELEIRA, (0, ALTURA - 100, LARGURA, 100))

        for item in estoque_atual:
            item.desenhar(tela)

        pygame.display.flip()
        
        if ordenando:
            relogio.tick(15) 
        else:
            relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()