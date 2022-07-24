from pytube import YouTube
link = "https://www.youtube.com/watch?v=PHWHxbg9dQU"
yt = YouTube(link)
yt.streams.get_highest_resolution().download()