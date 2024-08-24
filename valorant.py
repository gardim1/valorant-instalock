#dar pip install  pyautogui no cmd
import pyautogui
import time

# Função que aguarda até que uma imagem seja encontrada na tela
def wait_for_image(image_path, confidence=0.8):
    print(f'Aguardando a imagem {image_path}')
    while True:
        # Tenta localizar a imagem na tela
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            print(f'Imagem {image_path} encontrada!')
            return location
        time.sleep(1)

# Tamanho de tela é 1920x1080, então o script está otimizado para esse tamanho
def main():
    # Espera a tela de "Iniciar Partida"
    wait_for_image('iniciar_partida.png')

    # Agora aguarda a tela de "Seleção de Agentes"
    wait_for_image('selecao_agentes.png')

    # Localiza a Jett na tela de seleção de agentes
    jett_location = wait_for_image('jett.png')

    # Clica na Jett
    pyautogui.click(jett_location)

    # Espera o botão de "Lock ou selecionar agente" aparecer e clica
    time.sleep(0.3)
    lock_location = wait_for_image('lock.png')
    pyautogui.click(lock_location)

    print("Instalock feito com sucesso! tmj lek")

if __name__ == '__main__':
    main()
