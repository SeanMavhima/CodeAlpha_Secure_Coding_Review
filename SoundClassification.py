import urllib
import urllib.request

audio_file_name = 'speech_16000_hz_mono.wav'
url = f'https://storage.googleapis.com/mediapipe-assets/{audio_file_name}'
urllib.request.urlretrieve(url, audio_file_name)

from IPython.display import Audio, display

file_name = '1091f54855b2803f0e9ce40596a5db10-mc.m4a'
display(Audio(file_name, autoplay=False))

import numpy as np

from mediapipe.tasks import python
from mediapipe.tasks.python.components import containers
from mediapipe.tasks.python import audio
from scipy.io import wavfile

# Customize and associate model for Classifier
base_options = python.BaseOptions(model_asset_path='yamnet.tflite')
options = audio.AudioClassifierOptions(
    base_options=base_options, max_results=4)

# Create classifier, segment audio clips, and classify
with audio.AudioClassifier.create_from_options(options) as classifier:
  sample_rate, wav_data = wavfile.read(audio_file_name)
  audio_clip = containers.AudioData.create_from_array(
      wav_data.astype(float) / np.iinfo(np.int16).max, sample_rate)
  classification_result_list = classifier.classify(audio_clip)

  assert(len(classification_result_list) == 5)

# Iterate through clips to display classifications
  for idx, timestamp in enumerate([0, 975, 1950, 2925]):
    classification_result = classification_result_list[idx]
    top_category = classification_result.classifications[0].categories[0]
    print(f'Timestamp {timestamp}: {top_category.category_name} ({top_category.score:.2f})')