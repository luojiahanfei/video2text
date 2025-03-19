from .subtitles import detect_subtitles, extract_subtitles
from .audio import extract_audio_text
from .image import sample_frames, generate_captions
from .fusion import fuse_content
import os

def process_video(video_path, output_file="output.txt"):
    """主处理流程"""
    # 字幕检测与处理
    if detect_subtitles(video_path):
        subtitles = extract_subtitles(video_path, "subtitles.txt")
        audio_text = ""
        print("字幕已提取")
    else:
        subtitles = []
        audio_text = extract_audio_text(video_path, "audio_text.txt")
        print("音频已转换")

    # 视频帧采样
    frame_dir = "sampled_frames"
    sample_frames(video_path, frame_dir)

    # 图像描述生成
    image_captions = generate_captions(frame_dir)

    # 融合描述
    final_text = fuse_content(subtitles, audio_text, image_captions)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_text)
    print(f"结果已保存至{output_file}")
