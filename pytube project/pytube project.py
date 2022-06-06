from pytube import YouTube
from colorama import init, Fore

def OnComplete(stream, filepath):
    print("Download complete")
    print(filepath)

def OnProgress(stream, chunk, bytes_remaining):
    #progress_string = f"{100 - round((bytes_remaining / stream.filesize * 100),2)}%"
    progress_string = f"{(100 - (bytes_remaining / stream.filesize * 100)):.2f}%"
    print(progress_string)

init()
url = input("YouTube link: ")
video_object = YouTube(url, on_complete_callback= OnComplete, on_progress_callback= OnProgress)

# Information
mins, secs = divmod(video_object.length, 60)
print(Fore.RED + f"Title: \033[39m  {video_object.title}")
print(Fore.RED + f"Length: \033[39m {mins:02d}:{secs:02d}")
print(Fore.RED + f"Views: \033[39m  {video_object.views / 1000000} million")
print(Fore.RED + f"Author: \033[39m {video_object.author}")

# Download

print(
    Fore.RED + "Download options: " + 
    Fore.GREEN + "(B)est \033[39m|" + 
    Fore.YELLOW + " (W)orst \033[39m|" + 
    Fore.BLUE + " (A)udio \033[39m| (E)xit")
download_choice = input('Enter the first letter of the options listed above: ').lower()

match download_choice:
    case 'b':
        video_object.streams.get_highest_resolution().download(r"C:\Users\Marco\Downloads")
    case 'w':
        video_object.streams.get_lowest_resolution().download(r"C:\Users\Marco\Downloads")
    case 'a':
        video_object.streams.get_audio_only.download(r"C:\Users\Marco\Downloads")