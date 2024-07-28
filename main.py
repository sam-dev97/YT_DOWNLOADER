import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_youtube_video(url, output_path):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            messagebox.showinfo("Successo", f"Video baixado com sucesso e salvo no diretório: {output_path}")
        except yt_dlp.utils.DownloadError as e:
            messagebox.showerror("Erro", f"Erro ao tentar baixar o vídeo: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_path_var.set(folder_selected)

def start_download():
    url = url_entry.get()
    output_path = output_path_var.get()
    if not url:
        messagebox.showwarning("Input Error", "Por favor insira uma URL do YouTube.")
    elif not output_path:
        messagebox.showwarning("Input Error", "Por favor selecione um caminho.")
    else:
        download_youtube_video(url, output_path)


root = tk.Tk()
root.title("SS Video Downloader")


tk.Label(root, text="URL do Vídeo do YouTube:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Onde deseja salvar:").grid(row=1, column=0, padx=10, pady=10)
output_path_var = tk.StringVar()
output_path_entry = tk.Entry(root, textvariable=output_path_var, width=50)
output_path_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Selecionar Pasta", command=browse_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Download", command=start_download).grid(row=2, column=1, padx=10, pady=20)

root.mainloop()
