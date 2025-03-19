from src.image import sample_frames, generate_captions
import os
def test_frame_sampling():
    frame_count = sample_frames("test/test_data/sample_video.mp4", "test_frames")
    assert frame_count > 0
    assert len(os.listdir("test_frames")) == frame_count

def test_caption_generation():
    sample_frames("test/test_data/sample_video.mp4", "test_frames")
    captions = generate_captions("test_frames")
    assert len(captions) > 0
    assert isinstance(captions[0], str)