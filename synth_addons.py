import re
from google.cloud import texttospeech


def mysplit(text, chunk=5000):
    text = re.sub(r'(\s)+', r'\1', text)

    result = []
    while text:
        if len(text) <= chunk:
            result.append(text)
            break
        
        found = False
        split_index = chunk
        while split_index > 0:
            if re.match(r'^(\.|\?|!)\s', text[split_index - 1:]) and \
                    not re.match(r'^\.\.\.\s', text[split_index - 3:]):
                found = True
                break
            split_index -= 1
        if not found:
            split_index = chunk
            while split_index > 0:
                if re.match(r'^\s', text[split_index - 1:]):
                    found = True
                    break
                split_index -= 1
        if split_index == 0:
            split_index = chunk
        rest = text[split_index:]
        rest = re.sub(r'^\s+', "", rest)
        result.append(text[:split_index])
        text = rest
    return result


def my_synthesize_speech(client, text, **kwargs):
    chunks = mysplit(text)
    return b"".join(client.synthesize_speech(input=texttospeech.SynthesisInput(text=chunk), **kwargs).audio_content for chunk in chunks)
