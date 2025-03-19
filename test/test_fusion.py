from src.fusion import fuse_content

def test_fusion():
    test_data = {
        "subtitles": ["字幕文本1", "字幕文本2"],
        "audio": "音频转写文本",
        "images": ["图像描述1", "图像描述2"]
    }
    result = fuse_content(**test_data)
    assert len(result.split()) >= 4
    assert "字幕文本1" in result