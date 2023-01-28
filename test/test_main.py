from __init__ import YoutubeDownloader,create_download_dir
from typing import List
import os
import unittest

class YoutubeDownloaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.youtube_downloader : YoutubeDownloader = YoutubeDownloader(download_dir=r'C:\github\youtube-downloader\mypytube')
        
    def test_run(self):
        keyword : str = '그때 그 아인'
        self.youtube_downloader.run()
        
        dir_list : List[str] = os.listdir(r'C:\github\youtube-downloader\mypytube')
        check_dir : List[str] = [dir for dir in dir_list if '그때 그 아인' in dir]
        self.assertNotEqual(len(check_dir),0)
            
    def test_input_url(self):
        test_url : str = 'https://www.youtube.com/watch?v=xYvO_mYfOfk&list=TLPQMjgwMTIwMjOiyUhRwbDIhw&index=10'        
        self.assertEqual(test_url,self.youtube_downloader.url)
    
    def test_creeate_download_dir(self):
        test_path : str = r'C:\github\youtube-downloader\testDir'
        create_download_dir(path=test_path)        
        dir_check : bool = os.path.isdir('testDir')
        self.assertTrue(dir_check)
        
    def tearDown(self):
        try:
            os.rmdir(r'C:\github\youtube-downloader\testDir')
        except:
            pass
    
if __name__ == '__main__':
    unittest.main()