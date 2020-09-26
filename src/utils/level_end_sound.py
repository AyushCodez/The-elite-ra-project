import simpleaudio as sa
def play( ):
    filename = 'assets/audio/effects/level_end.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

