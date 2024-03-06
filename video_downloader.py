# install pytube first
# download from: https://pytube.io
# install instruction: https://pytube.io/en/latest/user/install.html


from pytube import YouTube

link = input("Enter URL of Video: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
