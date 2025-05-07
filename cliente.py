import cv2
import tkinter as tk
from tkinter import messagebox


# Função para capturar e exibir a imagem da câmera
def capture_image():
    # Inicia a captura de vídeo (usando a câmera padrão)
    video_capture = cv2.VideoCapture(1)
    if not video_capture.isOpened():
        messagebox.showerror("Erro", "Não foi possível acessar a câmera.")
        return

    # Captura um único frame
    ret, frame = video_capture.read()
    if not ret:
        messagebox.showerror("Erro", "Falha ao capturar a imagem.")
        return

    # Exibe o frame em uma janela OpenCV
    cv2.imshow("Imagem Capturada", frame)

    # Espera pela confirmação do botão
    confirm_button["state"] = "normal"  # Habilita o botão para confirmar
    video_capture.release()  # Libera a câmera

    return frame  # Retorna a imagem capturada


# Função para confirmar a captura
def confirm_capture():
    global captured_frame

    # Verifica se a imagem foi capturada
    if captured_frame is not None:
        # Salva a imagem capturada
        cv2.imwrite("captured_image.jpg", captured_frame)
        messagebox.showinfo("Sucesso", "Imagem capturada e salva com sucesso!")
        cv2.destroyAllWindows()  # Fecha a janela da imagem
        root.quit()  # Fecha a janela Tkinter
    else:
        messagebox.showwarning("Aviso", "Nenhuma imagem foi capturada ainda!")


# Criar a janela Tkinter
root = tk.Tk()
root.title("Captura de Imagem")

# Variável para armazenar a imagem capturada
captured_frame = None

# Botão para capturar a imagem
capture_button = tk.Button(root, text="Capturar Imagem", command=lambda: capture_image())
capture_button.pack(pady=20)

# Botão para confirmar a captura
confirm_button = tk.Button(root, text="Confirmar Captura", state="disabled", command=confirm_capture)
confirm_button.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()
