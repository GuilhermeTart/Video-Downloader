import subprocess
import os
from colors import colors



    
def download_movie(movie_url, path):
    path = 'Videos_Download' 
    
    command = f"yt-dlp -f mp4 {movie_url} -o '{path}/%(title)s.%(ext)s'" 
    output = subprocess.check_output(command,shell=True) 
    if not os.path.exists(path):
        os.mkdir(path)
        print('Pasta Criada!')
    else:
        print(colors.red +'Pasta já existe'+ colors.reset)
        
    print(colors.blue + output.decode('latin-1') + colors.reset)
 

            

def download_audio(audio_url,path_audio ):  
    path_audio = 'Audio_Download' 
    command_audio = f"yt-dlp -x --audio-format mp3 {audio_url}  -o '{path_audio}/%(title)s.%(ext)s'"
    
    if not os.path.exists(path_audio):
        os.mkdir(path_audio)
        print('Pasta Criada!')
    else:
        print(colors.red +'Pasta já existe'+ colors.reset)
    
    output_audio = subprocess.check_output(command_audio, shell=True) 
    print(colors.blue + output_audio.decode('latin-1') + colors.reset)


        
def playlist_audio(playlist_url,path_audio_playlist ):
    path_audio_playlist = 'Audios_Download' 
    
    command_playlist = f"yt-dlp --extract-audio --audio-format mp3 '{playlist_url}' -o '{path_audio_playlist}/%(title)s'"
    
    if not os.path.exists(path_audio_playlist):
        os.mkdir(path_audio_playlist)
        print('Pasta Criada!')
    else:
        print(colors.red +'Pasta já existe'+ colors.reset)
    
    output_audio_playlist = subprocess.check_output(command_playlist, shell=True)   

    print(colors.blue + output_audio_playlist.decode('utf-8') + colors.reset)

           
  
 
   
   
   
if __name__ == '__main__':
   

 def main():
    
    print(f"""{colors.red}
          




 __      ____    _              _____                      _                 _           
 \ \    / /_/   | |            |  __ \                    | |               | |          
  \ \  / / _  __| | ___  ___   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \ \/ / | |/ _` |/ _ \/ _ \  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    \  /  | | (_| |  __/ (_) | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
     \/   |_|\__,_|\___|\___/  |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                                         
                                                                                         




        
 {colors.reset}""")


main()   
   
   
   
   
interation = input(colors.green +'Deseja baixar [V]ideo  [A]udio  ou [Ap]Audio_playlist? :  '+ colors.reset).lower()

if interation == 'v':
    movie_url = input(colors.green +'Informe o link do vídeo ou playlist: '+ colors.reset)
    output = download_movie(movie_url, './Videos_Download')

elif interation == 'a':         
    audio_url = input(colors.green +'Informe o link do vídeo que você deseja obter o audio: '+ colors.reset)
    output = download_audio(audio_url, './musica_Download')
   
elif interation == 'ap':         
    playlist_url = input(colors.green +'Informe o link da playlist que você deseja obter o áudio: '+ colors.reset)
    output =  playlist_audio(playlist_url, './musicas_Download')

else:
 print(colors.red +'parâmetro inválido'+ colors.reset)     
        
        
