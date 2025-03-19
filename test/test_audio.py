from src.audio import extract_audio_text

def test_audio_extraction():
    text = extract_audio_text("test/test_data/sample_audio.mp4")
    assert len(text) > 10  # 验证返回合理长度文本
    assert "失败" not in text  # 验证没有错误信息

# import pyaudio
# p = pyaudio.PyAudio()
# print(p.get_device_count())  # 应输出>0
#
# import pytesseract
# print(pytesseract.image_to_string('test_image.png'))  # 应有文字输出