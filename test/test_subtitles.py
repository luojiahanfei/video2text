import pytest
import os
from src.subtitles import detect_subtitles, extract_subtitles

def test_subtitle_detection():
    # 准备测试视频（带字幕和无字幕各一个）
    assert detect_subtitles("test/test_data/with_subtitle.mp4") is True
    assert detect_subtitles("test/test_data/no_subtitle.mp4") is False

def test_subtitle_extraction():
    result = extract_subtitles("test/test_data/with_subtitle.mp4", "test_sub.txt")
    assert len(result) > 0
    assert os.path.exists("test_sub.txt")

# import cv2
# print(cv2.VideoCapture().open('test_video.mp4'))  # 应返回True