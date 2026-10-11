import pygame
import sys
import random
import os

# Importações dos módulos separados
from src.item import ItemTaverna
from src.algoritmos import bubble_sort_visual, bucket_sort_visual, counting_sort_visual, radix_sort_visual

# Constantes
LARGURA = 1024
ALTURA = 768
FPS = 60
COR_FUNDO = (43, 30, 22)
COR_PRATELEIRA = (92, 64, 51)
COR_ETIQUETA = (230, 215, 180) # Cor do pergaminho para os painéis

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
    
    # Fontes
    fonte_hud = pygame.font.Font(None, 24)
    fonte_titulo = pygame.font.Font(None, 36)
    fonte_destaque = pygame.font.Font(None, 48)

    # Carregamento do Fundo
    usar_bg = False
    fundo_img = None
    possiveis_nomes_bg = ["Background.jpg", "Background.jpeg", "Background.png", "background.jpg", "background.jpeg", "background.png", "Background.jpg.jpg"]
    
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

    # Dicionário de Algoritmos para o Modo Jogo
    algoritmos_dict = {
        1: ("Bubble Sort", bubble_sort_visual),
        2: ("Bucket Sort", bucket_sort_visual),
        3: ("Counting Sort", counting_sort_visual),
        4: ("Radix Sort", radix_sort_visual)
    }

    estoque_atual = gerar_estoque(15)
    ordenando = False
    gerador_ordenacao = None

    # Variáveis de Estado do Modo Jogo
    modo_jogo = False
    esperando_resposta = False
    algoritmo_secreto = None
    resultado_jogo = None # Guarda a string "VITORIA" ou "DERROTA"

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if evento.type == pygame.KEYDOWN:
                # ---------------------------------------------------------
                # LÓGICA DE RESPOSTA (QUANDO O JOGO ESTÁ À ESPERA)
                # ---------------------------------------------------------
                if esperando_resposta:
                    aposta = None
                    if evento.key == pygame.K_1 or evento.key == pygame.K_KP1: aposta = 1
                    elif evento.key == pygame.K_2 or evento.key == pygame.K_KP2: aposta = 2
                    elif evento.key == pygame.K_3 or evento.key == pygame.K_KP3: aposta = 3
                    elif evento.key == pygame.K_4 or evento.key == pygame.K_KP4: aposta = 4
                    
                    if aposta is not None:
                        if aposta == algoritmo_secreto:
                            resultado_jogo = "VITORIA"
                        else:
                            resultado_jogo = "DERROTA"
                        esperando_resposta = False
                        modo_jogo = False
                        
                # ---------------------------------------------------------
                # ATALHOS NORMAIS (SÓ FUNCIONAM SE NÃO ESTIVER À ESPERA)
                # ---------------------------------------------------------
                elif not ordenando:
                    # ESPAÇO: Limpa tudo e gera novo estoque
                    if evento.key == pygame.K_SPACE:
                        estoque_atual = gerar_estoque(15)
                        resultado_jogo = None
                        modo_jogo = False
                    
                    # J: Inicia o Modo Jogo (Mistério)
                    elif evento.key == pygame.K_j:
                        estoque_atual = gerar_estoque(15)
                        resultado_jogo = None
                        algoritmo_secreto = random.randint(1, 4)
                        nome_secreto, func_secreta = algoritmos_dict[algoritmo_secreto]
                        
                        gerador_ordenacao = func_secreta(estoque_atual)
                        ordenando = True
                        modo_jogo = True
                    
                    # Atalhos diretos de demonstração
                    elif evento.key == pygame.K_RETURN:
                        ordenando = True
                        resultado_jogo = None
                        gerador_ordenacao = bubble_sort_visual(estoque_atual)
                    elif evento.key == pygame.K_b:
                        ordenando = True
                        resultado_jogo = None
                        gerador_ordenacao = bucket_sort_visual(estoque_atual)
                    elif evento.key == pygame.K_c:
                        ordenando = True
                        resultado_jogo = None
                        gerador_ordenacao = counting_sort_visual(estoque_atual)
                    elif evento.key == pygame.K_r:
                        ordenando = True
                        resultado_jogo = None
                        gerador_ordenacao = radix_sort_visual(estoque_atual)

        # ---------------------------------------------------------
        # ATUALIZAÇÃO DA ANIMAÇÃO
        # ---------------------------------------------------------
        if ordenando and gerador_ordenacao is not None:
            try:
                next(gerador_ordenacao)
            except StopIteration:
                ordenando = False
                gerador_ordenacao = None
                # Se estava no modo jogo, ao terminar a ordenação, pede a resposta
                if modo_jogo:
                    esperando_resposta = True

        # ---------------------------------------------------------
        # RENDERIZAÇÃO
        # ---------------------------------------------------------
        if usar_bg and fundo_img:
            tela.blit(fundo_img, (0, 0))
        else:
            tela.fill(COR_FUNDO)
            pygame.draw.rect(tela, COR_PRATELEIRA, (0, ALTURA - 100, LARGURA, 100))

        for item in estoque_atual:
            item.desenhar(tela)
            
        # HUD de Atalhos Atualizado
        painel_rect = pygame.Rect(15, 15, 260, 185)
        pygame.draw.rect(tela, COR_FUNDO, painel_rect, border_radius=8)
        pygame.draw.rect(tela, COR_ETIQUETA, painel_rect, width=2, border_radius=8)
        
        textos_hud = [
            "📜 Grimório de Atalhos:",
            "[ESPAÇO] Embaralhar Poções",
            "[ J ] MODO JOGO (Adivinhar!)",
            "[ENTER] Bubble Sort",
            "[ B ] Bucket Sort",
            "[ C ] Counting Sort",
            "[ R ] Radix Sort"
        ]
        
        for i, linha in enumerate(textos_hud):
            if i == 0 or i == 2: cor_texto = COR_ETIQUETA
            else: cor_texto = (255, 255, 255)
            surf_texto = fonte_hud.render(linha, True, cor_texto)
            tela.blit(surf_texto, (30, 25 + (i * 22)))

        # ---------------------------------------------------------
        # RENDERIZAÇÃO DOS PAINÉIS DO MODO JOGO (OVERLAYS)
        # ---------------------------------------------------------
        if esperando_resposta or resultado_jogo:
            # Cria a caixa central de pergaminho
            caixa_centro = pygame.Rect(0, 0, 480, 220)
            caixa_centro.center = (LARGURA // 2, ALTURA // 2 - 80)
            
            # Sombra e fundo
            pygame.draw.rect(tela, (20, 10, 5), caixa_centro.move(5, 5), border_radius=12)
            pygame.draw.rect(tela, COR_FUNDO, caixa_centro, border_radius=12)
            pygame.draw.rect(tela, COR_ETIQUETA, caixa_centro, width=4, border_radius=12)

            if esperando_resposta:
                t1 = fonte_titulo.render("Qual magia organizou as poções?", True, COR_ETIQUETA)
                t2 = fonte_hud.render("1) Bubble  |  2) Bucket  |  3) Counting  |  4) Radix", True, (255, 255, 255))
                
                tela.blit(t1, t1.get_rect(center=(caixa_centro.centerx, caixa_centro.centery - 30)))
                tela.blit(t2, t2.get_rect(center=(caixa_centro.centerx, caixa_centro.centery + 30)))

            elif resultado_jogo:
                nome_real = algoritmos_dict[algoritmo_secreto][0]
                
                if resultado_jogo == "VITORIA":
                    t_res = fonte_destaque.render("✨ ACERTOU! ✨", True, (100, 255, 100))
                    t_desc = fonte_hud.render(f"O feitiço utilizado foi mesmo o {nome_real}!", True, (255, 255, 255))
                else:
                    t_res = fonte_destaque.render("💀 ERROU! 💀", True, (255, 100, 100))
                    t_desc = fonte_hud.render(f"A magia correta era o {nome_real}.", True, (255, 255, 255))
                
                t_cont = fonte_hud.render("Pressione [ESPAÇO] para fechar", True, COR_ETIQUETA)

                tela.blit(t_res, t_res.get_rect(center=(caixa_centro.centerx, caixa_centro.centery - 40)))
                tela.blit(t_desc, t_desc.get_rect(center=(caixa_centro.centerx, caixa_centro.centery + 10)))
                tela.blit(t_cont, t_cont.get_rect(center=(caixa_centro.centerx, caixa_centro.centery + 60)))

        pygame.display.flip()
        
        if ordenando:
            relogio.tick(6) 
        else:
            relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()