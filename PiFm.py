#!/usr/bin/python

import subprocess
import os
import wave
import ffmpeg


def play(path:str, freq = '', sample_rate = '', stereo = '', volume = '') :
   if os.path.isfile(path):
      subprocess.call(['./pifm', path, freq, sample_rate, stereo, volume])
   elif os.path.isdir(path):
      p = subprocess.Popen(['./pifm', '-', freq, sample_rate, stereo, volume], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
      process_files(path, p)
   else:
      raise FileNotFoundError()

def process_files(path:str, p:subprocess.Popen):
   for _, dirs, files in os.walk(path):
      for file in [audio_file for audio_file in files if os.path.splitext()[-1] == '.wav']:
         p.communicate(input=wave.open(file, 'rb'))
      for dir in dirs:
         process_files(dir, p)