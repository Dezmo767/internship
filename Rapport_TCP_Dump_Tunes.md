# Report of TCP Dump Tunes

## Introduction

This report is about a Python Script called TCP_Dump_Tunes.py, the creator is ```https://github.com/nickpegg/tcpdump-tunes```.
I have just modifiert the Scrip and add some New Instruments and also modifiert the Max pitch to 85 and synchronised.
The Script Transform data traffic into "Random" generated Music one example you can find is the link ```https://github.com/Dezmo767/internship/``` with the file name ```test_just-wow``` it is an midi file type.

### What does the scirpt do?
The script TCP Dump tunes interprets some IP packets captured using TCPDump Unix Tool and generate a MIDI audio file out of it. 

### What is TCPDumpTool

A Python script that was createdd by **Nickpegg** and hosted ```https://github.com/nickpegg/tcpdump-tunes```. It was created on Oct 7, 2014 and last modified on Oct 11, 2014. 

## Installation Ubuntu/Linux Version 14.04 LTS

+ install Python with the command ```sudo apt-get install python3```
+ install Python pip with the command ```sudo apt-get install python-pip``` and ```sudo apt-get install python3-pip```
+ install python midi with the command ```sudo pip install midi ``` and ```sudo pip install python-midi```

+ Clone my github directory with the command ```git clone https://github.com/Dezmo767/internship.git``` then you can start.

## Running the script
+ Go to repo

Type ```sudo tcpdump -i any -n -c 1000 | ~/internship/Midi_Tunes/TCP_Dump_Intern.py -f test_just-wow```

reminder:

Command            | Effect
--- | ---
sudo               | launch command as root
tcpdump            | launch tcpdump application
-i any             | tcpdump option to use all network interfaces
-n                 | tcpdump option to not convert addresses (i.e., host addresses, port numbers, etc.) to names
-c 1000            | tcpdump option to exit after receiving 1000 packets
pipe (\|)          | link commands
~                  | is your Home directory
-f                 | write the file
test_just-wow      | your File name
TCP_Dump_Intern.py | the "Music" Script



## Edit the Script
 + Volicity is the Volume of the instruments between 0 and 127
 + Ticks are the speed of Playing an instrument
 + **List of the Midi Instruments**
 
| PC  |Instruments            | PC  |Instruments                | PC  |Instruments           | PC  |Instruments       |
|---|---|---|---|---|---|---|---|
| 0  |Acoustic Grand Piano    | 33  |Electric Bass (finger)     | 66  |Tenor Sax             | 99  |FX 4 (atmosphere) |
| 1  |Bright Acoustic Piano   | 34  |Electric Bass (pick)       | 67  |Baritone Sax          | 100 |FX 5 (brigthness) |
| 2  |Electric Grand Piano    | 35  |Fretless Bass              | 68  |Oboe                  | 101 |FX 6 (golblins)   |
| 3  |Honky-tonk Piano        | 36  |Slap Bass 1                | 69  |English Horn          | 102 |FX 7 (echoes)     |
| 4  |Electric Piano 1        | 37  |Slap Bass 2                | 70  |Bassoon               | 103 |FX 8 (sci-fi)     |
| 5  |Electric Piano 2        | 38  |Synth Bass 1               | 71  |Clarinet              | 104|Sitar              |
| 6  |Harpsichord             | 39  |Synth Bass 2               | 72  |Piccolo               | 105|Banjo              |
| 7  |Clavi                   | 40  |Violin                     | 73  |Flute                 | 106|Shamisen           |
| 8  |Celesta                 | 41  |Viola                      | 74  |Recorder              | 107|Koto               |
| 9  |Glockenspiel            | 42  |Cello                      | 75  |Pan Flute             | 108|Kalimba            |
| 10 |Music Box               | 43  |Contrabass                 | 76  |Blow Bottle           | 109|Bag Pipe           |
| 11 |Vibraphone              | 44  |Tremolo Strings            | 77  |Shakuhachi            | 110|Fiddle             |
| 12 |Marimba                 | 45  |Pizzicato Strings          | 78  |Wistle                | 111|Shanai             |
| 13 |Xylophone               | 46  |Orchestral Harp            | 79  |Ocarina               | 112|Tinkle Bell        |
| 14 |Tubular Bells           | 47  |Timpani                    | 80  |Lead 1 (square)       | 113|Agogo              |
| 15 |Dulcimer                | 48  |String Ensemble 1          | 81  |Lead 2 (sawtooth)     | 114|Steel Drums        |
| 16 |Drawbar Organ           | 49  |String Ensemble 2          | 82  |Lead 3 (calliope)     | 115|Woodblock          |
| 17 |Percussiv Organ         | 50  |SynthString 1              | 83  |Lead 4 (chiff)        | 116|Taiko Drum         |
| 18 |Rock Organ              | 51  |SynthString 2              | 84  |Lead 5 (charage)      | 117|Melodic Tom        |
| 19 |Church Organ            | 52  |Choir Aahs                 | 85  |Lead 6 (voice)        | 118| Synth Drum        |
| 20 |Reed Organ              | 53  |Voice Oohs                 | 86  |Lead 7 (fifths)       | 119|Reverse Cymbal     |
| 21 |Accordion               | 54  |Synth Voice                | 87  |Lead 8 (bass + lead)  | 120|Guitar Fret Noise  |
| 22 |Harmonica               | 55  |Orchestra Hit              | 88  |Pad 1 (new age)       | 121|Breath Noise       |
| 23 |Tango Accordion         | 56  |Trumpet                    | 89  |Pad 2 (warm)          | 122|Seashore           |
| 24 |Acoustic Guitar (nylon) | 57  |Trombone                   | 90  |Pad 3 (polysyth)      | 123|Bird Tweet         |
| 25 |Acoustic Guitar (steel) | 58  |Tuba                       | 91  |Pad 4 (choir)         | 124|Telephone Ring     |
| 26 |Electric Guitar (jazz)  | 59  |Muted Trumpet              | 92  |Pad 5 (bowed)         | 125|Helicopter         |
| 27 |Electric Guitar (clean) | 60  |French Horn                | 93  |Pad 6 (metallic)      | 126|Applause           |
| 28 |Electric Guitar (muted) | 61  |Brass Section              | 94  |Pad 7 (halo)          | 127|Gunshot            |
| 29 |Overdriven Guitar       | 62  |Synth Brass 1              | 95  |Pad 8 (sweep)         |||
| 30 |Disortion Guitar        | 63  |Synth Brass 2              | 96  |FX 1 (rain)           |||
| 31 |Guitar harmonics        | 64  |Soprano Sax                | 97  |FX 2 (soundtrack)     |||
| 32 |Acoustic Bass           | 65  |Alto Sax                   | 98  |FX 3 (crystal)        |||

+ Change an Instrument
> <p>It's on line 93 - 95</p>
```track.append(midi.NoteOnEvent(tick=400, velocity=50, pitch=note))```<br>
```track.append(midi.NoteOffEvent(tick=250, pitch=note))```<br>
```track.append(midi.ProgramChangeEvent(data=[0]))```<br>
Change Data=[**0**] to one of the Numbers in the Table of Instruments
