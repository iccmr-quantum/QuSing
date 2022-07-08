#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: S. Basak
Interdisciplinary Centre for Computer Music Research
University of Plymouth, UK
"""

from mido import Message, MidiFile, MidiTrack
import time

def convert_code_to_MIDI(tune_code, pitch_codes, dur_codes, sequence_length, backend, number_of_new_notes, shots):

    mid = MidiFile()

    # for a new midi track, 
    # the 'ticks_per_beat" parameter is set at 480 by default by the MIDO python package
    # the training midi tracks have the ticks_per_beat parameter set at 960
    # in order to change the length of the track, I have adjusted the durations 
    ticks_per_beat = mid.ticks_per_beat
    factor = ticks_per_beat/960

    print('ticks per beat:', ticks_per_beat)
    print('factor', factor)

    print(tune_code)

    # split 9 bit data into pitches and durations
    pitches_bin = []
    durations_bin = []
    for string in tune_code:
        #string = i.replace('\n', '')
        #string = i
        pitch = string[0:5]
        duration = string[5:]
        pitches_bin.append(pitch)
        durations_bin.append(duration)
        
    pitch_encoding = []
    for i in pitch_codes:
        i = (int(i[0]), i[1].strip(' ').strip("''"))
        pitch_encoding.append(i)
    
    duration_encoding = []
    for i in dur_codes:
        i = (int(i[0]), i[1].strip(' ').strip("''"))
        duration_encoding.append(i)
    
    # convert binary to decimal    
    pitches = []
    for p in pitches_bin:
        for dec in pitch_encoding:
            if p == dec[1]:
                pitches.append(dec[0])
        
    durations = []
    for d in durations_bin:
        for dec in duration_encoding:
            if d == dec[1]:
                durations.append(int(dec[0]*factor))

    # define midi track and add mesages
    track = MidiTrack()
    mid.tracks.append(track)

    for i in range(len(durations)):
        if pitches[i] == 0:
            # pitch = 0 = silence
            # silcence = note with zero velocity
            m_on = Message('note_on', channel = 0, note = pitches[i], velocity = 0, time = durations[i])
            m_off = Message('note_off', channel = 0, note = pitches[i], velocity = 0, time = 0)
        else:   
            m_on = Message('note_on', channel = 0, note = pitches[i], velocity = 100, time = 0)
            m_off = Message('note_off', channel = 0, note = pitches[i], velocity = 0, time = durations[i])
        track.append(m_on)
        track.append(m_off)
    
    mid.save('QuSing'  + "_" + str(sequence_length) + "n " + str(backend) + "_" + str(number_of_new_notes) + "notes " + str(shots) \
        + "shots " + "_" + str(time.time()) + '.mid')

