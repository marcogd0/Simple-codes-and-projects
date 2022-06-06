import PySimpleGUI as sg
from pytube import YouTube

def OnComplete(stream, filepath):
    window["-PROGRESSBAR-"].update(0)
    #print(filepath)

def ProgressCheck(stream, chunk, bytes_remaining):
    progress_amount = 100 - round(bytes_remaining / stream.filesize * 100)
    window["-PROGRESSBAR-"].update(progress_amount)

sg.theme("DarkBrown4")
starting_layout = [
    [sg.Text("YouTube URL:"), sg.In(key= "-INPUT-"), sg.Button("Submit")]
]

info_tab = [
    [sg.Text("Title:"),sg.Text('', key= "-TITLE-")],
    [sg.Text("Length:"),sg.Text('', key= "-LENGTH-")],
    [sg.Text("Views:"),sg.Text('', key= "-VIEWS-")],
    [sg.Text("Author:"),sg.Text('', key= "-AUTHOR-")],
    [
        sg.Text("Description:"),
        sg.Multiline('', key= "-DESCRIPTION-", size=(40,20),
        no_scrollbar = True, disabled = True)
    ]
]

download_tab = [
    [sg.Frame("Best Quality", [[sg.Button("Download", key= "-BEST-"), sg.Text('', key= "-BESTRES-"), sg.Text('', key="-BESTSIZE-")]])],
    [sg.Frame("Worst Quality", [[sg.Button("Download", key= "-WORST-"), sg.Text('', key= "-WORSTRES-"), sg.Text('', key="-WORSTSIZE-")]])],
    [sg.Frame("Audio", [[sg.Button("Download", key= "-AUDIO-"), sg.Text('', key= "-AUDIOSIZE-")]])],
    [sg.VPush()],
    [sg.Progress(100, size=(20,20), expand_x= True, key="-PROGRESSBAR-")]
]

layout = [
    [sg.TabGroup([[sg.Tab("Info", info_tab), sg.Tab("Download", download_tab)]])]
]

window = sg.Window('YouTube Downloader', starting_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        video_object = YouTube(values["-INPUT-"], on_complete_callback= OnComplete, on_progress_callback= ProgressCheck)
        window.close()

        # Video Info
        window = sg.Window("YouTube Downloader", layout, finalize=True)
        window["-TITLE-"].update(video_object.title)
        mins, secs = divmod(video_object.length, 60)
        window["-LENGTH-"].update(f"{mins:02d} minutes and {secs:02d} seconds")
        window["-VIEWS-"].update(video_object.views)
        window["-AUTHOR-"].update(video_object.author)
        window["-DESCRIPTION-"].update(video_object.description)

        # Download
        window["-BESTSIZE-"].update(f"{(video_object.streams.get_highest_resolution().filesize / 1048576):.1f} MB")
        window["-BESTRES-"].update(video_object.streams.get_highest_resolution().resolution)

        window["-WORSTSIZE-"].update(f"{(video_object.streams.get_lowest_resolution().filesize / 1048576):.1f} MB")
        window["-WORSTRES-"].update(video_object.streams.get_lowest_resolution().resolution)

        window["-AUDIOSIZE-"].update(f"{(video_object.streams.get_audio_only().filesize / 1048576):.1f} MB")

    if event == "-BEST-":
        video_object.streams.get_highest_resolution().download(r"C:\Users\Marco\Downloads")
    if event == "-WORST-":
        video_object.streams.get_lowest_resolution().download(r"C:\Users\Marco\Downloads")
    if event == "-AUDIO-":
        video_object.streams.get_audio_only().download(r"C:\Users\Marco\Downloads")

window.close()