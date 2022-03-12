from pytube import YouTube

link=str(input("Paste the URL of the video you want to download: "))

video=YouTube(link)

vid_resln=video.streams.get_highest_resolution()

vid_resln.download()

print("Downloaded Completed.")