import re

def chunk_text(text, chunk_size=500, overlap=100):

    sentences = re.split(r'(?<=[.!?]) +', text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def clean_chunks(chunks):
    filtered = []

    for chunk in chunks:
        if len(chunk.strip()) < 50:
            continue
        if "@" in chunk:
            continue
        if "ISSN" in chunk:
            continue
        if "http" in chunk:
            continue

        filtered.append(chunk)

    return filtered