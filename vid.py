from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input('digite um link: ')
path = input('digite uma pasta: ')
yt = YouTube(link)

print('baixando...')
ys = yt.streams.filter(only_audio=True).first().download(path)
print('download completo')

print('convertendo arquivos...')
for file in os.listdir(path):
    if re.search('Mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(Mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(Mp4_path)
print('sucesso')