import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

def extract_audio_text(video_path):
    """提取并识别音频"""
    # 提取音频为临时文件
    audio = AudioSegment.from_file(video_path)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        audio.export(tmpfile.name, format="wav")
        audio_path = tmpfile.name

    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='zh-CN')
    except Exception as e:
        text = f"音频识别失败：{str(e)}"
    finally:
        os.remove(audio_path)

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    return text