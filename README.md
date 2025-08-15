# Yng - De volta para casa

**Yng - De volta para casa** é um jogo estilo Platformer inspirado em clássicos side-scrollers, desenvolvido em Python utilizando a biblioteca **Pygame Zero**. O jogador controla um alienígena que deve atravessar plataformas, evitar obstáculos como abelhas e spikes, e alcançar a nave para vencer.  

## Funcionalidades

- Movimento horizontal e pulo com física básica (gravidade e colisão com plataformas).  
- Animação do personagem com sprites de caminhada e idle.  
- Obstáculos dinâmicos, como abelhas voadoras e spikes.  
- Sistema de câmera que segue o personagem principal.  
- Menu interativo com opções para iniciar o jogo, ativar/desativar música e efeitos sonoros ou sair do jogo.  
- Sons de vitória e derrota.  
- Reset do jogo ao perder ou vencer.  

## Estrutura do Código

- **Alien**: classe principal do personagem controlado pelo jogador, incluindo física e animação.  
- **Bee**: inimigos voadores com animação simples e reaparecimento aleatório.  
- **Spikes**: obstáculos fixos que causam derrota ao tocar.  
- **Menu e HUD**: sistema de menu e feedback visual para vitória/derrota.  

## Como Jogar

1. **Baixe o código do jogo** do repositório ou clone usando Git.  
2. **Crie um ambiente virtual**
3. **Instale o Pygame Zero: 'pip install pgzero'
4. Execute o jogo usando o terminal: 'pgzrun main.py'

## Tecnologias

Python 3.12.2
Pygame Zero

   
