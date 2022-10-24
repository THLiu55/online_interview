import threading
import wave

import pyaudio
from PIL import ImageGrab
import cv2
import numpy as np
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip


class Record:
    def __init__(self, name):
        self.recording = True
        self.audio_filename = "audio_for_covering.mp3"
        self.video_record_filename = "video_for_covering.avi"
        self.name = name
        self.t1 = threading.Thread(target=self.record_audio)
        self.t2 = threading.Thread(target=self.video_record)

    def record_audio(self):
        record_audio = pyaudio.PyAudio()
        stream = record_audio.open(format=pyaudio.paInt16, channels=2, rate=48000, input=True, frames_per_buffer=124)
        wave_file = wave.open(self.audio_filename, 'wb')
        wave_file.setnchannels(2)
        wave_file.setsampwidth(record_audio.get_sample_size(pyaudio.paInt16))
        wave_file.setframerate(48000)

        while self.recording:
            data = stream.read(128, exception_on_overflow=False)
            wave_file.writeframes(data)
        wave_file.close()
        stream.stop_stream()
        stream.close()
        record_audio.terminate()

    def video_record(self):
        screen = ImageGrab.grab()
        video = cv2.VideoWriter(self.video_record_filename, cv2.VideoWriter_fourcc(*'XVID'), 20, screen.size)
        while self.recording:
            screen = ImageGrab.grab()
            # noinspection PyTypeChecker
            screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
            video.write(screen)
        video.release()

    def run(self):

        for t in [self.t1, self.t2]:
            t.start()

    def stop(self):
        self.recording=False
        audio = AudioFileClip(self.audio_filename)
        video = VideoFileClip(self.video_record_filename)
        total_video = video.set_audio(audio)
        total_video.write_videofile(self.name, codec="libx264", fps=25)
        audio.close()
        video.close()

        for t in [self.t1, self.t2]:
            t.join()


record = Record("screen_record_test.mp4")
