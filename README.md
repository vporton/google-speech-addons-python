# google-speech-addons-python
Addons to Google Text-to-Speech (bypass 5000 character limit!)

# The problem

Google has 5000 characters limit in its TTS (Text-to-Speech) synthetizer.

# The solution

For plain text, I wrote code that splits the text into fragments of maximum
5000 characters before passing it to Google.

It correctly handles ends of sentences (`.`, `?`, `!`) and doesn't consider
ellipsis (`...`) as end of sentence, because it may meet in the middle of a quote.

Moreover, if your sentence is longer than 5000 characters, this library does its
best to split between word boundaries.

# The API

`sentences_splitter(text, chunk=5000)`

Splits `text` into chunks, as described above, and returns an array of strings.

`synthesize_speech(client, text, **kwargs)`

Splits the text into fragments and passes it to Google Text-to-Speech synthetizer
and returns the audio bytes.

Note that in the current version of the library the returns audio bytes resulting
from simple concatenation of results returned from Google, what may be right or wrong
dependently on the Google output format choosen. Note that resulting `.mp3` files play
well (if we ask Google to return it in `.mp3` format).

# Example

```
import sys
from google.cloud import texttospeech
from speech.synth_addons import synthesize_speech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

with open(sys.argv[1]) as in_:
    text = in_.read()

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL, name="en-US-Wavenet-A"
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=1.0,
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
audio_content = synthesize_speech(client, text, voice=voice, audio_config=audio_config)

# The response's audio_content is binary.
with open(sys.argv[2], "wb") as out:
    out.write(audio_content)
```
