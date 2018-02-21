#!/usr/bin/env python

# Parses the text output of tcpdump (with no -v) from stdin, makes music

import argparse
import re
import sys
from datetime import datetime

import midi


MIN_SPACING = 20
MIN_LENGTH = 25
MAX_OCTAVE = 100

# midi.type is the synchronisation of the Music, 0 = midi Standart, 1 = synchron, 2 = ansynchron 

midi.type = 1

def main():
    line_re = r"(?P<timestamp>\d{2}:\d{2}:\d{2}.\d{6}) IP (?P<src>\d+\.\d+\.\d+\.\d+)\.(?P<sport>\d+) > (?P<dst>\d+\.\d+\.\d+\.\d+)\.(?P<dport>\d+): (?:Flags \[(?P<flags>[SFPRUWE\.]+)\])?.+?length (?P<length>\d+)"

    arg_parser = argparse.ArgumentParser(description="MIDI from tcpdump")
    arg_parser.add_argument('-f',
                            help="Output file, omit or give - for stdout",
                            metavar='file',
                            default='-')
    args = arg_parser.parse_args()

    if args.f == '-':
        output_file = sys.stdout
    else:
        output_file = open(args.f, 'w')

    pattern = midi.Pattern()
    track = midi.Track()
    pattern.append(track)
    track2 = midi.Track()
    pattern.append(track2)
    track3 = midi.Track()
    pattern.append(track3)
    track4 = midi.Track()
    pattern.append(track4)
    track5 = midi.Track()
    pattern.append(track5)


    last_time = datetime.now()
    line = sys.stdin.readline()
    while line:
        match = re.match(line_re, line)
        if match:
            data = match.groupdict()

            # Get the difference between now and the last event
            now = datetime.strptime(data['timestamp'], '%H:%M:%S.%f')

            spacing = int((now - last_time).microseconds / 1000.0)
            last_time = now

            if spacing < MIN_SPACING:
                spacing = MIN_SPACING

            # Determine note length based on packet length
            pkt_length = int(data.get('length', 0))
            note_length = int(pow(pkt_length, 0.75))

            if note_length < MIN_LENGTH:
                note_length = MIN_LENGTH

            # determine the note to play based on TCP flags
            note = midi.C_3
            flags = data.get('flags', '')
            if flags:
                if 'S' in flags:
                    note = midi.D_3
                elif '.' in flags:
                    note = midi.C_3
                elif 'F' in flags:
                    note = midi.G_3
                elif 'R' in flags:
                    note = midi.F_3

            # Determine the octave based on the src and dst IPs
            octave = hash((data['src'], data['dst'])) % 6 + 2
            note = note + octave * 5

	    if note > MAX_OCTAVE:
		note  = MAX_OCTAVE

            # Finally, append the note to the track, Velocity is between 0 and 127
            track.append(midi.NoteOnEvent(tick=0, velocity=0, pitch=note))
            track.append(midi.NoteOffEvent(tick=350, pitch=note))
	    track.append(midi.ProgramChangeEvent(data=[4]))

	    track2.append(midi.NoteOnEvent(tick=0, velocity=90,pitch=note))
            track2.append(midi.NoteOffEvent(tick=150, pitch=note))
	    track2.append(midi.ProgramChangeEvent(data=[117]))
	    
	    track3.append(midi.NoteOnEvent(tick=0, velocity=60, pitch=note))
            track3.append(midi.NoteOffEvent(tick=500, pitch=note))
	    track3.append(midi.ProgramChangeEvent(data=[58]))

	     #track4.append(midi.NoteOnEvent(tick=0, velocity=127, pitch=note))
             #track4.append(midi.NoteOffEvent(tick=1000, pitch=note))
	     #track4.append(midi.ProgramChangeEvent(data=[52]))
	  
	     #track5.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
             #track5.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track5.append(midi.ProgramChangeEvent(data=[52]))

        line = sys.stdin.readline()

    # Dump MIDI track to stdout
    track.append(midi.EndOfTrackEvent(tick=1))
    track2.append(midi.EndOfTrackEvent(tick=1))
    track3.append(midi.EndOfTrackEvent(tick=1))
    # track4.append(midi.EndOfTrackEvent(tick=1))
    # track5.append(midi.EndOfTrackEvent(tick=1))
    midi.write_midifile(output_file, pattern)
    

    return 0


if __name__ == '__main__':
    exit(main())
