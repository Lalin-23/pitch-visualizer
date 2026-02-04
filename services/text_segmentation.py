def segment_text(text):
    sentences = text.split(".")
    return [s.strip() for s in sentences if len(s.strip()) > 5]
