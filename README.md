# 🍻 Organizador de Taverna - Simulador de Ordenação Mágica

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=flat-square" alt="Status do projeto">
  <img src="https://img.shields.io/badge/Linguagem-Python-3776AB?logo=python&logoColor=white" alt="Linguagem Python">
  <img src="https://img.shields.io/badge/Interface-Pygame-F4C935?logo=python&logoColor=black" alt="Pygame">
</p>

## 📝 Descrição

O "Organizador de Taverna" é um simulador interativo desenvolvido em Python utilizando a biblioteca Pygame. O jogo coloca o jogador no papel de um taverneiro encarregado de organizar os caóticos estoques de poções e suprimentos mágicos que chegam diariamente. 

O projeto tem como foco a implementação 100% manual de algoritmos de ordenação, proporcionando uma interface visual (GUI) onde é possível observar, em tempo real, o comportamento de diferentes métodos de ordenação atuando sobre os itens do inventário. O objetivo é categorizar itens por atributos como raridade e poder mágico.

## 🎬 Apresentação em Vídeo

Assista à apresentação completa do projeto no YouTube:

[![Apresentação do Organizador de Taverna](https://img.shields.io/badge/▶_Assistir_no_YouTube-red?logo=youtube&logoColor=white&style=for-the-badge)](LINK_DO_SEU_VIDEO_AQUI)

## 💡 Diferenciais Técnicos

O principal destaque deste projeto é a união da lógica algorítmica rigorosa com feedback visual dinâmico:

- **Implementação Manual:** Todos os algoritmos de ordenação foram codificados do zero, sem o uso de funções nativas como `sort()`.
- **Renderização Visual (Pygame):** Animações em tempo real mostrando os *swaps* (trocas) e realocações dos itens nas prateleiras da taverna.
- **Categorização em Múltiplos Níveis:** Aplicação de algoritmos estáveis para organizar primeiro por grupos (ex: baldes de raridade) e, em seguida, por valores específicos (ex: poder da poção).

Essas abordagens tornam o estudo de ordenação mais tangível e demonstram na prática os conceitos de Estruturas de Dados 2.

## 🔎 Algoritmos de Ordenação Implementados

### 🪣 Bucket Sort

Utilizado para a triagem inicial dos suprimentos. O algoritmo distribui os itens recebidos em diferentes "baldes" (prateleiras) baseados na sua categoria principal ou nível de raridade, permitindo dividir o problema caótico da taverna em subgrupos menores com complexidade média $O(n + k)$.

### 🔢 Counting Sort

Aplicado para ordenar atributos com intervalos de valores bem definidos e discretos, como o nível das poções (ex: nível 1 a 10). Ideal para organizar rapidamente uma prateleira específica sem a necessidade de comparações diretas entre os itens, atingindo complexidade $O(n + k)$.

### 📊 Radix Sort

Utilizado para organizar artefatos com valores numéricos maiores e mais complexos (como o valor de venda em moedas de ouro). O algoritmo processa os dígitos individualmente, garantindo uma ordenação estável e linear para os itens mais valiosos do inventário.

## 🛠️ Tecnologias Utilizadas

- **Linguagem Python 3**
- **Pygame** para renderização gráfica e controle de *framerate*
- **Algoritmos de Ordenação** desenvolvidos manualmente
- **Git/GitHub** para versionamento na organização da disciplina

## ⚙️ Como Instalar e Executar

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina e o gerenciador de pacotes `pip`.

### Passo a passo

1. Clone o repositório:

```bash
git clone [https://github.com/eda2-2026/G41_Ordenacao_EDA2-2026.2.git](https://github.com/eda2-2026/G41_Ordenacao_EDA2-2026.2.git)
```
2. Acesse a pasta do projeto:

```bash
cd G41_Ordenacao_EDA2-2026.2
```
3. Instale as dependências (Pygame):

```bash
pip install pygame
```
4. Execute o simulador:

```bash
python main.py
```

## 🧪 Funcionalidades do Sistema

- Geração aleatória de lotes de suprimentos e poções caóticas;

- Interface gráfica interativa para escolha do método de ordenação;

- imação em tempo real da organização das prateleiras;

- Exibição de métricas de desempenho (tempo de execução e número de trocas);

- Reinício rápido para testar diferentes algoritmos com novos itens.

## 🌐 Prints da Interface

### Menu da Taverna

### Ordenações em Andamento

## 📝 Política de Commits (Conventional Commits)

O repositório segue um histórico de **commits graduais obrigatórios**, registrando cada etapa do desenvolvimento de maneira clara e rastreável. As implementações, correções e documentação devem ser organizadas em commits pequenos e objetivos.

As mensagens devem utilizar as seguintes tags padronizadas:

- `feat:` novas implementações;
- `fix:` correções de bugs e ajustes de comportamento;
- `docs:` atualizações no README ou comentários;
- `refactor:` melhorias estruturais sem alterar a funcionalidade.

Exemplos:

```text
feat: implementa busca de produtos por SKU
feat: cria arvore binaria de busca por preco
fix: corrige consulta por nome exato
docs: atualiza instrucoes de compilacao
refactor: organiza funcoes do catalogo
```

## 👤 Autor

<p align="center">
    <img src="assets/Profile.jpg" alt="Foto de Bernardo Watanabe Venzi" width="220">
</p>

- **Nome:** Bernardo Watanabe Venzi
- **Matrícula:** 232001120
- **Modalidade:** execução individual

## 🎓 Contexto Acadêmico

Trabalho da disciplina de **Estruturas de Dados 2**, turma 2026.2.