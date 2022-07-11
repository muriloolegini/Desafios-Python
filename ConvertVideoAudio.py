import moviepy.editor

# Carrega arquivo do video #
video = moviepy.editor.VideoFileClip('Faint.mp4')

# Extrai apenas audio do video #
audio_data = video.audio

# Salva o arquivo de audio extraído de video #
audio_data.write_audiofile('Faint.mp3')