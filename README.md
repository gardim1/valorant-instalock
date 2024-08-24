# Valorant Agent Selector Automation

Este script automatiza o processo de seleção de personagem no jogo Valorant utilizando a biblioteca `PyAutoGUI`. O script detecta a tela de "Iniciar Partida", aguarda até que a tela de "Seleção de Agentes" seja carregada, e então seleciona automaticamente o agente `Jett` e confirma a escolha.

## Requisitos

- Python 3.x
- Biblioteca `PyAutoGUI`
- Capturas de tela (screenshots) dos elementos do jogo que serão utilizados no script:
  - Botão "Iniciar Partida"
  - Tela de "Seleção de Agentes"
  - Ícone da `Jett`
  - Botão de "Lock" (confirmar agente)

## Instalação

1. Clone este repositório ou faça o download dos arquivos.
2. Instale as dependências necessárias usando `pip`:

```bash
pip install pyautogui
