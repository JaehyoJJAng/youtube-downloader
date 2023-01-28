from pytube import YouTube
from typing import List
import os


def create_download_dir(path:str):
    dir : str = path.split('\\')[-1]
    if not os.path.exists(dir):
        os.mkdir(dir)
        
class YoutubeDownloader:
    def __init__(self,download_dir:str) -> None:
        self.download_dir : str = download_dir        
        self.url : str = self.input_url()
        
    def run(self)-> None:
        # 화질
        resolutions : List[str] = ['1080p','720p','480p']
        
        # Youtube Instance
        yt : YouTube = YouTube(url=self.url,on_complete_callback=self.on_complete,on_progress_callback=self.on_progress)
            
        # Get Video Infos
        video_filters : List[list] = [yt.streams.filter(mime_type='video/mp4',res=f'{resolution}',progressive=True) for resolution in resolutions]
        
        # Get Video Filter
        filter = ''        
        for video_filter in video_filters:
            if len(video_filter) == 0:
                continue
            else:
                filter = video_filter
                break
        
        # Download
        video_filter.first().download(self.download_dir)
    
    def on_complete(self,stream,file_path)-> None:
        print(file_path)
    
    def on_progress(self,stream,chunk,bytes_remaining)-> None:
        print(100 - (bytes_remaining / stream.filesize * 100))
        
    def input_url(self)-> str:
        os.system('cls')
        while True:        
            url : str = input('Input URL\n:')
            if not url:
                os.system('cls')
                print('No URL')
                continue
            
            if len(url) < 15:
                os.system('cls')
                print("Invalid url")
                continue
            
            return url

def main()-> None:
    # Downloader Directory
    download_dir : str = r'C:\github\youtube-downloader\mypytube'
    
    # Create Directory
    create_download_dir(path=download_dir)
    
    # Create YoutubeDownloader
    youtube_downloader : YoutubeDownloader = YoutubeDownloader(download_dir=download_dir)
    
    # Execute run
    youtube_downloader.run()
    

if __name__ == '__main__':
    main()