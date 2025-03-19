def fuse_content(subtitles, audio_text, image_captions):
    """融合多模态描述"""
    all_text = []
    if subtitles:
        all_text.extend(subtitles)
    if audio_text:
        all_text.append(audio_text)
    if image_captions:
        all_text.extend(image_captions)
    # 简单去重
    return ' '.join(list(set(all_text)))