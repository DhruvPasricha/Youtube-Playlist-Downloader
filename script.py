from pytube import Playlist

def download_playlist(url, quality = '360p'):
    playlist = Playlist(url)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    videoNum = 1
    for video in playlist.videos:
        print('downloading: video -', videoNum)
        video.streams.filter(res=quality).first().download()    
        print('downloaded: video -', videoNum)
        videoNum += 1

url = 'https://www.youtube.com/playlist?list=PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_'
download_playlist(url, '360p')
