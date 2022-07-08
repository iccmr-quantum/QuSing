#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: S. Basak
Interdisciplinary Centre for Computer Music Research
University of Plymouth, UK
"""

from mido import MidiFile
import numpy as np
import collections

def convert_MIDI_to_code(filename):
    print('Input music:', filename)
    mid = MidiFile(filename+'.mid')

    messages = []
    msg_types = ['note_on', 'note_off']
    for i, track in enumerate(mid.tracks):
        for msg in track:
            if msg.type in msg_types:
                messages.append(msg)

    ticks_per_beat = mid.ticks_per_beat
    print('Ticks per beat:', ticks_per_beat, 'ticks')

    # quantization
    smallest_unit = int(ticks_per_beat/ 12)
    for m in messages:
        m.time = int(smallest_unit * round(m.time/smallest_unit))
    print('Notes quantized to: ', smallest_unit, 'ticks')

    # ensuring that all messages are in the sequence on off on off
    for i in range(len(messages)-1):
        if messages[i].type == messages[i+1].type == 'note_on':
            t1 = messages[i+1].time
            t2 = messages[i+2].time
            messages[i+1], messages[i+2] = messages[i+2], messages[i+1]
        
            messages[i+1].time = t1
            messages[i+2].time = t2
    
    # extracting pitch and duration information fromm messages
    all_pitches = []
    all_durations = []
    for i in range(len(messages)-1):
    
        m0 = messages[i]
        m1 = messages[i+1]
    
        if m0.type == 'note_on' and m1.type == 'note_off':
            if m0.time == 0:
                all_pitches.append(m0.note)
                all_durations.append(m1.time) # m1 is a note off
            else:
                # silence between notes
                all_pitches.append(0)
                all_durations.append(m0.time)
            
                # note after the silence
                all_pitches.append(m0.note)
                all_durations.append(m1.time)
            
    # Given
    pitch_bits = 5
    duration_bits = 4

    # counting the frequency of occurance of pitches
    counter_p = collections.Counter(all_pitches)
   
    # we only have 5 bits for pitch
    # Considering 2^5 = 32 pitch values
    unique_pitches = []
    if len(counter_p) > 2**pitch_bits:
        for p in counter_p.most_common(2**pitch_bits):
            unique_pitches.append(p[0])
    else:
        unique_pitches = list(counter_p.keys())

    # same for durations, only 4 bits
    counter_d = collections.Counter(all_durations)
    unique_durations = []
    if len(counter_d) > 2**duration_bits:
        for d in counter_d.most_common(2**duration_bits):
            unique_durations.append(d[0])
    else:
        unique_durations = list(counter_d.keys())

    # sorting for convenience while testing
    unique_pitches.sort()
    unique_durations.sort()

    # if pitch is not one of the most common pitches, find the nearest pitch from the unique_pitches list
    for i in range(len(all_pitches)):
        if all_pitches[i] not in unique_pitches:
            p = all_pitches[i]
            p = min(unique_pitches, key=lambda x:abs(x-p))
            all_pitches[i] = p

    for i in range(len(all_durations)):
        if all_durations not in unique_durations:
            d = all_durations[i]
            d = min(unique_durations, key=lambda x:abs(x-d))
            all_durations[i] = d

    # enoding scheme for pitches 
    pitch_encoding = []
    for i in range(len(unique_pitches)):
        pitch_encoding.append((unique_pitches[i], np.binary_repr(i, width = pitch_bits)))

    #filename1 = filename+'_pitenc.txt'
    #file = open(filename1, 'w')
    #for p in pitch_encoding:
    #    file.write(str(p)+'\n')

    # encoding scheme for durations
    duration_encoding = []
    for i in range(len(unique_durations)):
        duration_encoding.append((unique_durations[i], np.binary_repr(i, width = duration_bits)))

    #filename2 = filename+'_durenc.txt'
    #file = open(filename2, 'w')
    #for d in duration_encoding:
    #    file.write(str(d)+'\n')

    # using binary values pitches and durations
    encoded_pitches = []
    encoded_durations = []

    for p in all_pitches:
        for enc in pitch_encoding:
            if p == enc[0]:
                encoded_pitches.append(enc[1])
            
    for d in all_durations:
        for enc in duration_encoding:
            if d == enc[0]:
                encoded_durations.append(enc[1])

    # combining encoded output
    encoded_notes = []
    encoded_notes_for_file = []
    for i in range(len(encoded_durations)):
        #encoded_notes_for_file.append(encoded_pitches[i]+encoded_durations[i]+'\n')
        encoded_notes.append(encoded_pitches[i]+encoded_durations[i])

    # writing data to file
    #file = open(filename+'.txt', 'w')
    #file.writelines(encoded_notes_for_file)
    #file.close()

    return encoded_notes, pitch_encoding, duration_encoding