import cv2
import os
from PIL import Image
from transformers import pipeline

def sample_frames(video_path, output_dir,sample_interval=10):
    """采样视频帧"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * sample_interval)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0

    for i in range(0, total_frames, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1
    cap.release()
    return frame_count
def generate_captions(image_dir):
    """生成图像描述"""
    captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    captions = []
    for img_file in os.listdir(image_dir):
        if img_file.lower().endswith(('png', 'jpg', 'jpeg')):
            image_path = os.path.join(image_dir, img_file)
            image = Image.open(image_path)
            result = captioner(image)
            captions.append(result[0]['generated_text'])
    return captions