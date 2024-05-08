 # Download de videos e áudios do YouTube,Likedin,Instagram e Facebook

**Este script Python permite baixar vídeos, áudios e playlist do Youtube de forma simples e prática.**

**Funcionalidades:**

- Baixar vídeos individuais em formato MP4.
- Extrair áudio de vídeos individuais em formato MP3.
- Baixar áudio  de playlists completas do Youtube em formato MP3.

**Requisitos:**

- Python 3
- Bibliotecas: subprocess, os, colors
- Programa yt-dlp (instale com `pip install yt-dlp`)

**Uso:**

1. Clone o repositório.
2. Execute o script com `Video_Downloader.py`.
3. Siga as instruções no terminal para escolher o tipo de download desejado e informar a URL do vídeo ou da playlist.
4. Para executar a opção de baixar áudios de playlist no windows (AP) faça essa alteração no código ---> command_playlist = f'yt-dlp --extract-audio --audio-format mp3 "{playlist_url}" -o {path_audio_playlist}/%(title)s'
   ![image](https://github.com/GuilhermeTart/Video-Downloader/assets/136984328/1b5a13b3-223c-47ee-839e-7e24506f225c)


**Observações:**

- Os vídeos serão salvos na pasta "Videos_Download".
- Os áudios serão salvos na pasta "Audio_Download".
- As playlists de áudio serão salvas na pasta "Audios_Download".
- As pastas serão criadas automaticamente se não existirem.


