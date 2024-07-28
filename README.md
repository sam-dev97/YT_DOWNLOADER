# SS Video Downloader

SS Video Downloader é uma aplicação simples em Python para baixar vídeos do YouTube utilizando a biblioteca `yt-dlp` e uma interface gráfica construída com `tkinter`.

## Funcionalidades

- Baixa vídeos do YouTube no formato de melhor qualidade disponível.
- Permite selecionar o diretório onde o vídeo será salvo.
- Interface gráfica amigável para facilitar o uso.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `yt-dlp`
  - `tkinter`

## Instalação

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/ss-video-downloader.git
cd ss-video-downloader
```

Caso queira, crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

Instale a lib:
```bash
pip install yt-dlp
```

Execute o código:
```bash
python main.py
```

Caso queira transformar em um executável para facilitar sua vida:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed your_script_name.py
```
