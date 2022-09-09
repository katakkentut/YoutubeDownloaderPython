import time
from pytube import YouTube
import os
import colorama
from colorama import Fore


def video_downloader():
    path = r" put your destination path here"
    ys = link.streams.get_lowest_resolution()
    print("Downloading...")
    ys.download(output_path=path)
    print("Video Download completed!!")


def mp3_downloader():
    video = link.streams.filter(only_audio=True).first()
    destination = r" put your destination path here "
    print("Downloading...")
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    print("Downloading...")
    os.rename(out_file, new_file)
    print("Audio Download completed!!")


if __name__ == '__main__':
    colorama.init()
    red = Fore.RED

    while True:
        os.system("cls")
        print(rf"""{red}
                    __   _______ _   _ _____ _   _______ _____                      
                    \ \ / /  _  | | | |_   _| | | | ___ \  ___|                     
                     \ V /| | | | | | | | | | | | | |_/ / |__                       
                      \ / | | | | | | | | | | | | | ___ \  __|                      
                      | | \ \_/ / |_| | | | | |_| | |_/ / |___                      
                      \_/  \___/ \___/  \_/  \___/\____/\____/                                                                                                                                                    
            ______ _____  _    _ _   _  _     _____  ___ ______ ___________ 
            |  _  \  _  || |  | | \ | || |   |  _  |/ _ \|  _  \  ___| ___ \
            | | | | | | || |  | |  \| || |   | | | / /_\ \ | | | |__ | |_/ /
            | | | | | | || |/\| | . ` || |   | | | |  _  | | | |  __||    / 
            | |/ /\ \_/ /\  /\  / |\  || |___\ \_/ / | | | |/ /| |___| |\ \ 
            |___/  \___/  \/  \/\_| \_/\_____/\___/\_| |_/___/ \____/\_| \_| 
           {Fore.YELLOW}                                                                                                                             
        """)
        link = YouTube(str(input("~~ Enter URL of youtube video:  ")))
        print(Fore.RED, "\n    Title: ", link.title)
        print( f"""
        [1] Download Video
        [2] Download Audio
            {Fore.YELLOW}
    """)

        select = int(input("~~ Enter Option: "))
        print("")

        try:
            if select == 1:
                video_downloader()
                time.sleep(1)
            else:
                mp3_downloader()
                time.sleep(1)
        except Exception as e:
            print(e)
