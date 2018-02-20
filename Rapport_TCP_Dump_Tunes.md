# Report of TCP Dump Tunes

## Introduction

This report is about a Python Script called TCP_Dump_Tunes.py, the creator is ```https://github.com/nickpegg/tcpdump-tunes```.
I have just modifiert the Scrip and add some New Instruments.
The Script Transform data traffic into "Random" generated Music one example you can find is the link ```https://github.com/Dezmo767/internship/``` with the file name ```test_just-wow``` it is an midi file type.

### What does the scirpt do?
The script TCP Dump tunes interprets some IP packets captured using TCPDump Unix Tool and generaes a MIDI audio file out of it. 

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

Command | Effect
--- | ---
sudo | launch command as root
tcpdump | launch tcpdump application
-i any | tcpdump option to use all network interfaces
-n | tcpdump option to not convert addresses (i.e., host addresses, port numbers, etc.) to names
-c 1000 | tcpdump option to exit after receiving 1000 packets
pipe (\|) | link commands

## Edit the Script
 + Volicity is the Volume of the instruments between 0 and 127
 + Ticks are the speed of Playing an instrument
 + **List of the Midi Instruments**
 
PC | Instrument
--- | ---
| 0| Acoustic Grand Piano|
|1 | Bright Acoustic Piano|
|2 | Electric Grand Piano|
|3 | Honky-tonk Piano|
|4 |Electric Piano 1|
|5 |	Electric Piano 2|
|6 |Harpsichord|
|7 |Clavi|
|8 |Celesta|
|9 |Glockenspiel|
|10 |Music Box|
|11 |Vibraphone|
|12 |Marimba|
|13 |Xylophone|
|14 |Tubular Bells|
|15 |Dulcimer|
|16 |Drawbar Organ|
|17 |Percussive Organ|
|18 |Rock Organ|
|19 |Church Organ|
|20 |Reed Organ|
|21|Accordion|
|22|Harmonica|
|23|Tango Accordion|
|24|Acoustic Guitar (nylon)|
|25|Acoustic Guitar (steel)|
|26|Electric Guitar (jazz)|
|27|Electric Guitar (clean)|
|28|Electric Guitar (muted)|
|29|Overdriven Guitar|
|30|Distortion Guitar|
|31|Guitar harmonics|
|32|Acoustic Bass|
|33|Electric Bass (finger)|
|34|Electric Bass (pick)|
|35|Fretless Bass|
|36|Slap Bass 1|
|37|Slap Bass 2|
|38|Synth Bass 1|
|39|Synth Bass 2|
|40|Violin|
|41|Viola|
|42|Cello|
|43|Contrabass|
|44|Tremolo Strings|
|45|Pizzicato Strings|
|46|Orchestral Harp|
|47|Timpani|
|48|String Ensemble 1|
|49|String Ensemble 2|
|50|SynthString 1|
|51|SynthStrings 2|
|52|Choir Aahs|
|53|Voice Oohs|
|54|Synth Voice|
|55|Orchestra Hit|
|56|Trumpet|
|57|Trumpet|
|58|Tuba|
|59|Muted Trumpet|
|60|French Horn|
|61|Brass Section|
|62|SynthBrass 1|
|63|SynthBrass 2|
|64|Soprano Sax|
|65|Alto Sax|
|66|Tenor Sax|
|67|Baritone Sax|
