import cv2
import pytesseract
from config import TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def detect_subtitles(video_path, sample_interval=10):
    """检测视频是否存在硬字幕"""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * sample_interval)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    text_count = 0

    for i in range(0, total_frames, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            break
        # 图像预处理
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        # OCR识别
        text = pytesseract.image_to_string(thresh)
        if text.strip():
            text_count += 1
    cap.release()
    return text_count >= 3  # 至少检测到3个文字帧视为有字幕
def extract_subtitles(video_path, output_file, sample_interval=2):
    """提取视频中的字幕"""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * sample_interval)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    extracted_text = []

    for i in range(0, total_frames, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(thresh, lang='chi_sim+eng')  # 中英文识别
        if text.strip():
            extracted_text.append(text.strip())
    cap.release()
    # 去重并保存
    unique_text = list(set(extracted_text))
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_text))
    return unique_text