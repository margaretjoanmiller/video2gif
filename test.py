from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']
ydl_opts = {'final_ext': 'mkv',
            'format': 'bv*[ext=mp4]+ba[ext=vorbis]/b[ext=mp4] / bv*+ba/b',
            'outtmpl': {'default': 'result/inter.mkv'},
            'postprocessors': [{'key': 'FFmpegVideoRemuxer', 'preferedformat': 'mkv'}]}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)


