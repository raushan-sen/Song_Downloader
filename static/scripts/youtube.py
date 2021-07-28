
# pip install youtube_dl
# pip install pafy
# pip install pytube

import pafy
import math
import random
from pytube import YouTube
from Dlr.settings import *

def youtube(url,idx):
    
    if idx==None:
        a=songbitrates(url)
        down=random.choice(a["download_bits"])["bitid"]
    else:
        down=idx        
    try:
        song = pafy.new(url)
        filename=f"dlr-songs-{song.title.split('-')[0].replace(' ','-')}.mp3"
        song.audiostreams[int(down)].download(filepath=os.path.join(BASE_DIR,'static/songs/')+filename)
        
        f=f"/static/songs/{filename}"
        file=f
    except:
        file=None
    return file


def songbitrates(url):
    try:
        song = pafy.new(url)
        streamss=song.audiostreams

        bitrates=[]
        for idx, bit in enumerate(streamss):
            bitrates.append(str(idx)+','+str(math.ceil(float(bit.bitrate.replace('k',''))))+'kbps Song')

        random_bitrates=random.sample(bitrates,k=3)

        json_for_file={"download_bits":[{
                "bitid":random_bitrates[0].split(',')[0],
                "bitrate":random_bitrates[0].split(',')[1],
            },{
                "bitid":random_bitrates[1].split(',')[0],
                "bitrate":random_bitrates[1].split(',')[1],
            },{
                "bitid":random_bitrates[2].split(',')[0],
                "bitrate":random_bitrates[2].split(',')[1],
            }]
        }
    except:
        json_for_file=None
    return json_for_file


def youtubpy(url):
    v=YouTube(url).streams.filter(only_audio=True)
    # v=YouTube(url).streams.get_by_itag(itag)

# print(youtubpy('https://www.youtube.com/watch?v=lX3vT_Gm_HE'))

# print('sucesss------------------------------------')

def lyrics(url):
    import requests
    from bs4 import BeautifulSoup
    a=requests.get('https://www.lyrics.com/sublyric/77651/Arijit+Singh/KHAIRIYAT+Song+Lyrics')

    soup = BeautifulSoup(a.text, 'html.parser')
    
    return soup.find_all(id="lyric-body-text")[0].text