import subprocess
import eel
import os

# root_dir = os.path.abspath(os.path.dirname(__file__))

eel.init('templates')

@eel.expose
def demo():
    print("Hello")
@eel.expose
def openVLC(full_path, file_name):
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
    media_path = full_path+"\\"+file_name
    # parameter = r"--intf=dummy"
    streaming_options = r":sout=#transcode{acodec=mp3,ab=128}:http{mux=mp3,dst=:8080/}"
    subprocess.call([vlc_path, media_path, streaming_options])

if __name__== "__main__":
    eel.start('index.html', size=(1000, 600), port=10, root="templates")