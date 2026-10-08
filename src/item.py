import pygame
import os

# Cores da Etiqueta
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
            
        texto = self.fonte.render(f"{self.valor}g", True, COR_TEXTO_ETIQ)
        centro_etiqueta_y = topo_pocao_y - 25
        retangulo_texto = texto.get_rect(center=(centro_x, centro_etiqueta_y))
        
        tag_rect = retangulo_texto.inflate(12, 8)
        
        pygame.draw.line(tela, COR_FIO, tag_rect.midbottom, (centro_x, topo_pocao_y), 2)
        pygame.draw.rect(tela, COR_ETIQUETA, tag_rect, border_radius=4)
        pygame.draw.rect(tela, COR_BORDA_ETIQ, tag_rect, width=2, border_radius=4)
        tela.blit(texto, retangulo_texto)