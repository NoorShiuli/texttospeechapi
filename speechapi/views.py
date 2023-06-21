from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from gtts import gTTS

# Create your views here.

def text_to_speech_view(request):
    text = request.GET.get('text', '')

    if text:
        tts = gTTS(text)
        audio_file = f'audio/default.mp3'
        tts.save(audio_file)
        return FileResponse(open(audio_file, 'rb'), content_type='audio/mpeg')
    else:
        err_audio_file = f'audio/error/error.mp3'
        return FileResponse(open(err_audio_file, 'rb'), content_type='audio/mpeg')
