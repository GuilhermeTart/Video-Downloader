import os
import subprocess
#
from colors import colors
from sys import exit



while True:
        
    def download_movie(movie_url, path):
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                print('Pasta Criada!')
            else:
                print(colors.red +'Pasta já existe'+ colors.reset)
            #
        except OSError:
            print("Não foi possível encontrar o caminho! Verifique!!")
            raise
        except Exception:
            raise
        
        path = 'Videos_Download' 
        command = ['yt-dlp', movie_url, '-o', f'{path}/%(title)s.%(ext)s']
        output = subprocess.check_output(command) 
        
        # 
        print(colors.blue + output.decode('latin-1') + colors.reset)
    

                

    def download_audio(audio_url,path_audio ):  
        try:
            if not os.path.exists(path_audio):
                os.mkdir(path_audio)
                print('Pasta Criada!')
            else:
                print(colors.red +'Pasta já existe'+ colors.reset)
            #
        except OSError:
            print("Não foi possível encontrar o caminho! Verifique!!")
            raise
        except Exception:
            raise
        
        path_audio = 'Audio_Download' 
        command_audio = ["yt-dlp","-x","--audio-format", "mp3",audio_url, "-o", f"{path_audio}/%(title)s.%(ext)s" ]
        output_audio = subprocess.check_output(command_audio) 
        
        
        # 
        print(colors.blue + output_audio.decode('latin-1') + colors.reset)

            
    def playlist_audio(playlist_url,path_audio_playlist ):
        try:
            if not os.path.exists(path_audio_playlist):
                os.mkdir(path_audio_playlist)
                print('Pasta Criada!')
            else:
                print(colors.red +'Pasta já existe'+ colors.reset)
            #
        except OSError:
            print("Não foi possível encontrar o caminho! Verifique!!")
            raise
        except Exception:
            raise
        
        path_audio_playlist = 'Audios_Download' 
        command_playlist = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--yes-playlist",
        "--ignore-errors",
        playlist_url,
        "-o", f"{path_audio_playlist}/%(title)s.%(ext)s"
    ]
        try:
            result = subprocess.run(command_playlist, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o comando: {e}")
            print(e.stderr)
            raise
           
  
 
   
   
   
   




   
   
    def main():
    
        interation = input(colors.green +'Deseja baixar [V]ideo  [A]udio  ou [Ap]Audio_playlist? :  '+ colors.reset).lower()

        match interation:
            case 'v':
                movie_url = input(colors.green +'Informe o link do vídeo: '+ colors.reset)
                output = download_movie(movie_url, './Videos_Download')
        
            case 'a':         
                audio_url = input(colors.green +'Informe o link do vídeo que você deseja obter o audio: '+ colors.reset)
                output = download_audio(audio_url, './Audio_Download')
    
            case 'ap':         
                playlist_url = input(colors.green +'Informe o link da playlist que você deseja obter o áudio: '+ colors.reset)
                output =  playlist_audio(playlist_url, './Audios_Download')

            case _:
                print(colors.red +'parâmetro inválido'+ colors.reset)
                exit(1)     
            


    
    print(f"""{colors.red}
            

 __      ____    _              _____                      _                 _           
 \ \    / /_/   | |            |  __ \                    | |               | |          
  \ \  / / _  __| | ___  ___   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \ \/ / | |/ _` |/ _ \/ _ \  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    \  /  | | (_| |  __/ (_) | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
     \/   |_|\__,_|\___|\___/  |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   



                                                                                            
                                                                                            


            
    {colors.reset}""")

   
    
    Exit = input(colors.green +'Deseja sair? (y/n) '+ colors.reset).lower()
    if Exit == 'y':
        break   
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        
if __name__ == '__main__':
    main()   
            
