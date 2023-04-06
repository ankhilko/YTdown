import pytube

url = 'https://www.youtube.com/watch?v=7t2alSnE2-I'

s = pytube.YouTube(url)

s = s.streams.get_highest_resolution()

s.download()
