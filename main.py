import pygame
import sys

# Configurações da Janela
LARGURA = 1024
ALTURA = 768
FPS = 60

# Paleta de Cores (Estilo Taverna)
COR_FUNDO = (43, 30, 22)      # Marrom escuro (madeira)
COR_TEXTO = (245, 245, 220)   # Bege (pergaminho)

def main():
    # Inicialização do Pygame
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("🍻 Organizador de Taverna - Ordenação Mágica")
    relogio = pygame.time.Clock()

    rodando = True

    # Loop Principal
    while rodando:
        # 1. Tratamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # 2. Atualização da Lógica
        # Aqui controlaremos os passos dos algoritmos de ordenação no futuro

        # 3. Renderização
        tela.fill(COR_FUNDO)
        
        # (Futuro: desenhar as prateleiras e as poções/barris aqui)

        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()