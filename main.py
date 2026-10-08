import pygame
import sys
import random
import os

# Configurações da Janela
LARGURA = 1024
ALTURA = 768
FPS = 60

# Paleta de Cores (Fallback caso a imagem falhe)
COR_FUNDO = (43, 30, 22)
COR_PRATELEIRA = (92, 64, 51)
COR_ETIQUETA = (230, 215, 180)
COR_BORDA_ETIQ = (139, 69, 19)
COR_TEXTO_ETIQ = (60, 40, 20)
COR_FIO = (200, 180, 150)

class ItemTaverna:
    def __init__(self, valor, x, y, largura_slot, altura_max):
        self.valor = valor 
        self.x = x
        self.y = y
        self.largura_slot = largura_slot
        
        if self.valor <= 40:
            nome_arquivo = "potion1.png"
        elif self.valor <= 70:
            nome_arquivo = "potion2.png"
        else:
            nome_arquivo = "potion3.png"
            
        try:
            caminho_imagem = os.path.join("assets", nome_arquivo)
            imagem_original = pygame.image.load(caminho_imagem).convert_alpha()
            
            largura_orig, altura_orig = imagem_original.get_size()
            proporcao = largura_orig / altura_orig
            
            percentual = 0.6 + ((self.valor / 100) * 0.6)
            self.nova_largura = int((self.largura_slot * 1.3) * percentual)
            self.altura = int(self.nova_largura / proporcao)
            
            # Limita a altura para não ultrapassar o topo da tela ou cobrir o cenário
            if self.altura > altura_max:
                self.altura = altura_max
                self.nova_largura = int(self.altura * proporcao)
            
            self.imagem = pygame.transform.scale(imagem_original, (self.nova_largura, self.altura))
            self.offset_x = (self.largura_slot - self.nova_largura) // 2
            self.usar_sprite = True
            
        except (FileNotFoundError, pygame.error):
            self.usar_sprite = False
            self.altura = int((self.valor / 100) * altura_max)
            self.nova_largura = self.largura_slot
            self.offset_x = 0
            if self.valor <= 40: self.cor = (50, 100, 255)
            elif self.valor <= 70: self.cor = (50, 255, 100)
            else: self.cor = (255, 50, 50)
            
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 22)
        self.fonte.set_bold(True)

    def desenhar(self, tela):
        centro_x = self.x + self.largura_slot // 2
        topo_pocao_y = self.y - self.altura
        
        if self.usar_sprite:
            tela.blit(self.imagem, (self.x + self.offset_x, topo_pocao_y))
        else:
            pygame.draw.rect(tela, self.cor, (self.x, topo_pocao_y, self.nova_largura, self.altura))
            pygame.draw.rect(tela, (255, 255, 255), (self.x, topo_pocao_y, self.nova_largura, self.altura), 1)
            
        # Etiqueta de Preço
        texto = self.fonte.render(f"{self.valor}g", True, COR_TEXTO_ETIQ)
        centro_etiqueta_y = topo_pocao_y - 25
        retangulo_texto = texto.get_rect(center=(centro_x, centro_etiqueta_y))
        
        tag_rect = retangulo_texto.inflate(12, 8)
        
        pygame.draw.line(tela, COR_FIO, tag_rect.midbottom, (centro_x, topo_pocao_y), 2)
        pygame.draw.rect(tela, COR_ETIQUETA, tag_rect, border_radius=4)
        pygame.draw.rect(tela, COR_BORDA_ETIQ, tag_rect, width=2, border_radius=4)
        tela.blit(texto, retangulo_texto)

def bubble_sort_visual(estoque):
    n = len(estoque)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estoque[j].valor > estoque[j + 1].valor:
                estoque[j], estoque[j + 1] = estoque[j + 1], estoque[j]
                estoque[j].x, estoque[j + 1].x = estoque[j + 1].x, estoque[j].x
                yield True 
    yield False

def gerar_estoque(quantidade):
    estoque = []
    margem = 90
    largura_util = LARGURA - (margem * 2)
    largura_item = largura_util // quantidade
    
    for i in range(quantidade):
        valor = random.randint(10, 100)
        x = margem + (i * largura_item)
        
        # Subimos mais 15 pixels para alinhar com o topo do balcão
        y = ALTURA - 280 
        
        estoque.append(ItemTaverna(valor, x, y, largura_item, 250))
    return estoque

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("🍻 Organizador de Taverna - Ordenação Mágica")
    relogio = pygame.time.Clock()

    # Sistema robusto de carregamento de fundo
    usar_bg = False
    fundo_img = None
    
    # Lista de possíveis nomes/extensões que o arquivo pode ter assumido
    possiveis_nomes_bg = [
        "Background.jpg", "Background.jpeg", "Background.png",
        "background.jpg", "background.jpeg", "background.png",
        "Background.jpg.jpg" # Caso comum do Windows ocultar extensão
    ]
    
    for nome in possiveis_nomes_bg:
        caminho_bg = os.path.join("assets", nome)
        if os.path.exists(caminho_bg):
            try:
                fundo_img = pygame.image.load(caminho_bg).convert()
                fundo_img = pygame.transform.scale(fundo_img, (LARGURA, ALTURA))
                usar_bg = True
                print(f"Sucesso: Fundo carregado através de {nome}")
                break # Para de tentar assim que encontra
            except pygame.error:
                continue

    if not usar_bg:
        print("Aviso: Imagem de fundo não encontrada na pasta assets.")

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
                if evento.key == pygame.K_RETURN and not ordenando:
                    ordenando = True
                    gerador_ordenacao = bubble_sort_visual(estoque_atual)

        # Atualização lógica (com correção do Pylance)
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

        pygame.display.flip()
        
        if ordenando:
            relogio.tick(15) 
        else:
            relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()