#!/usr/bin/env python

# Parses the text output of tcpdump (with no -v) from stdin, makes music

import argparse
import re
import sys
from datetime import datetime

import midi


MIN_SPACING = 20 	# will change the difference between now and the last event.
MIN_LENGTH = 25		# to determinate the note length based on the packet length.
MAX_OCTAVE = 100	# means to set an Maximal Octave hight when the script say the Octave is 101 then it get reset to 100.

# midi.type is the synchronisation of the Music, 0 = midi Standart (ansynchron all in one track), 1 = synchron (Diffrent Tracks but all synchron), 2 = ansynchron ( Diffrent Tracks but ansynchron)

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
# To add track you can copy the first track (track = midi.Track() pattern.append(track)) an change the number behind.
    pattern = midi.Pattern()
    ###########################
    track = midi.Track()
    pattern.append(track)
    ###########################
    track2 = midi.Track()
    pattern.append(track2)
    track3 = midi.Track()
    pattern.append(track3)
    track4 = midi.Track()
    pattern.append(track4)
    track5 = midi.Track()
    pattern.append(track5)
    track6 = midi.Track()
    pattern.append(track6)
    track7 = midi.Track()
    pattern.append(track7)
    """track8 = midi.Track()
    pattern.append(track8)
    track9 = midi.Track()
    pattern.append(track9)
    track10 = midi.Track()
    pattern.append(track10)
    track11 = midi.Track()
    pattern.append(track11)
    track12 = midi.Track()
    pattern.append(track12)
    track13 = midi.Track()
    pattern.append(track13)
    track14 = midi.Track()
    pattern.append(track14)
    track15 = midi.Track()
    pattern.append(track15)"""


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
            note = midi.E_3 # Modifire midi.C_3 to midi.E_3
            flags = data.get('flags', '')
            if flags: # You can change the note D C G F how do you want.
                if 'S' in flags:
                    note = midi.D_5
                elif '.' in flags:
                    note = midi.C_5
                elif 'F' in flags:
                    note = midi.G_5
                elif 'R' in flags:
                    note = midi.F_5
		
            # Determine the octave based on the src and dst IPs
            octave = hash((data['src'], data['dst'])) % 6 + 2
            note = note + octave * 5

	    if note > MAX_OCTAVE:
		note  = MAX_OCTAVE

            # Finally, append the note to the track, Velocity is between 0 and 127 also just copy the first 3 lines to add an track don't forget to change the number behind track.
            track.append(midi.NoteOnEvent(tick=800, velocity=127, pitch=50))
            track.append(midi.NoteOffEvent(tick=800, pitch=50))
            track.append(midi.ProgramChangeEvent(data=[115]))
            
            track2.append(midi.NoteOnEvent(tick=200, velocity=127, pitch=midi.C_3))
            track2.append(midi.NoteOffEvent(tick=200, pitch=midi.C_3))
            track2.append(midi.ProgramChangeEvent(data=[120]))
            
            track3.append(midi.NoteOnEvent(tick=400, velocity=50, pitch=note))
            track3.append(midi.NoteOffEvent(tick=400, pitch=note))
            track3.append(midi.ProgramChangeEvent(data=[0]))
            
            track4.append(midi.NoteOnEvent(tick=200, velocity=50, pitch=note))
            track4.append(midi.NoteOffEvent(tick=400, pitch=note))
            track4.append(midi.ProgramChangeEvent(data=[27]))
            
            track5.append(midi.NoteOnEvent(tick=400, velocity=100, pitch=note))
            track5.append(midi.NoteOffEvent(tick=800, pitch=note))
            track5.append(midi.ProgramChangeEvent(data=[53]))

	    track6.append(midi.NoteOnEvent(tick=200, velocity=50, pitch=note))
            track6.append(midi.NoteOffEvent(tick=400, pitch=note))
	    track6.append(midi.ProgramChangeEvent(data=[32]))

	    track7.append(midi.NoteOnEvent(tick=0, velocity=75, pitch=note))
            track7.append(midi.NoteOffEvent(tick=100, pitch=note))
	    track7.append(midi.ProgramChangeEvent(data=[72]))

	     #track8.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
             #track8.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track8.append(midi.ProgramChangeEvent(data=[52]))

	     #track9.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
	     #track9.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track9.append(midi.ProgramChangeEvent(data=[52]))

	     #track10.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
             #track10.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track10.append(midi.ProgramChangeEvent(data=[52]))

	     #track11.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
             #track11.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track11.append(midi.ProgramChangeEvent(data=[52]))

	     #track12.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
             #track12.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track12.append(midi.ProgramChangeEvent(data=[52]))

	     #track13.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
             #track13.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track13.append(midi.ProgramChangeEvent(data=[52]))

	     #track14.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
             #track14.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track14.append(midi.ProgramChangeEvent(data=[52]))

	     #track15.append(midi.NoteOnEvent(tick=0, velocity=100, pitch=note))
             #track15.append(midi.NoteOffEvent(tick=500, pitch=note))
	     #track15.append(midi.ProgramChangeEvent(data=[52]))

        line = sys.stdin.readline()

    # Dump MIDI track to stdout add the track.append(midi.EndOfTrackEvent(tick=1)) and change the number behind the track to add a track
    track.append(midi.EndOfTrackEvent(tick=1))
    track2.append(midi.EndOfTrackEvent(tick=1))
    track3.append(midi.EndOfTrackEvent(tick=1))
    track4.append(midi.EndOfTrackEvent(tick=1))
    track5.append(midi.EndOfTrackEvent(tick=1))
    track6.append(midi.EndOfTrackEvent(tick=1))
    track7.append(midi.EndOfTrackEvent(tick=1))
    # track8.append(midi.EndOfTrackEvent(tick=1))
    # track9.append(midi.EndOfTrackEvent(tick=1))
    # track10.append(midi.EndOfTrackEvent(tick=1))
    # track11.append(midi.EndOfTrackEvent(tick=1))
    # track12.append(midi.EndOfTrackEvent(tick=1))
    # track13.append(midi.EndOfTrackEvent(tick=1))
    # track14.append(midi.EndOfTrackEvent(tick=1))
    # track15.append(midi.EndOfTrackEvent(tick=1))
    midi.write_midifile(output_file, pattern)
    

    return 0


if __name__ == '__main__':
    exit(main())
