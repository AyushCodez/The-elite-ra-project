# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Kartikey Pandey

import simpleaudio as sa
import constants as consts
import platform


def play():

    if platform.system() == "Windows":
        filename = fr'{consts.ROOT_PATH}\assets\audio\effects\level_end.wav'
    else:
        filename = f'{consts.ROOT_PATH}/assets/audio/effects/level_end.wav'

    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing
