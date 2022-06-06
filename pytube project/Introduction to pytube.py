from pytube import YouTube as yt

def OnComplete(stream, file_path):
    print("Complete")

def OnProgress(stream, chunk, bytes_remaining):
    print(100 - (bytes_remaining / stream.filesize * 100))

#video_object = YouTube('https://www.youtube.com/watch?v=T9vYgZJCmeI')
video_object = yt('https://www.youtube.com/watch?v=NtzDjNhPZgU&list=PLVwTKWhCb6I8QnXyMisA51t_A-QeFUEsx&index=26&t=128s', on_complete_callback= OnComplete, on_progress_callback= OnProgress)
print(video_object)

# Video Information
# print(video_object.title)
# mins, secs = divmod(video_object.length, 60)
# print(f"{mins:02d}:{secs:02d}")
# print(video_object.length)
# print(video_object.views)
# print(video_object.author)

# Video Streams
# for stream in video_object.streams:
#     print(stream)

print(video_object.streams.get_highest_resolution())
print(video_object.streams.get_lowest_resolution())
print(video_object.streams.get_audio_only())

# Download
video_object.streams.get_highest_resolution().download()