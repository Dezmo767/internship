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
 
| PC  |Instruments  | PC  | Instruments  |   | |
|---|---|---|---|---|---|
| 0  |Acoustic Grand Piano |   |   |   | |
| 1  |   |   |   |   ||
| 2  |   |   |   |   ||
| 3  |   |   |   |   ||
| 4 |   |   |   |   ||
| 5  |   |   |   |   ||
| 6  |   |   |   |   ||
| 7  |   |   |   |   ||
| 8  |   |   |   |   ||
| 9  |   |   |   |   ||
| 10  |   |   |   |   ||
| 11  |   |   |   |   ||
| 12  |   |   |   |   ||
| 13  |   |   |   |   ||
| 14  |   |   |   |   ||
| 15  |   |   |   |   ||
| 16  |   |   |   |   ||
| 17  |   |   |   |   ||
| 18  |   |   |   |   ||
| 19  |   |   |   |   ||
| 20  |   |   |   |   ||




PC | Instrument
--- | ---
|0 | Acoustic Grand Piano|
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
|68|Oboe|
|69|English Horn|
|70|Bassoon|
|71|Clarinet|
|72|Piccolo|
|73|Flute|
|74|Recorder|
|75|Pan Flute|
|76|Blow Bottle|
|77|Shakuhachi|
|78|Wistle|
|79|Ocarina|
|80|Lead 1 (square)|
|81|Lead 2 (sawtooth)|
|82|Lead 3 (calliope)|
|83|Lead 4 (chiff)|
|84|Lead 5 (charang)|
|85|Lead 6 (voice)|
|86|Lead 7 (fifths)|
|87|Lead 8 (bass + lead)|
|88|Pad 1 (new age)|
|89|Pad 2 (warm)|
|90|Pad 3 (polysynth)|
|91|Pad 4 (choir)|
|92|Pad 5 (bowed)|
|93|Pad 6 (metallic)|
|94|Pad 7 (halo)|
|95|Pad 8 (sweep)|
|96|FX 1 (rain)|
|97|FX 2 (soundtrack)|
|98|FX 3 (crystal)|
|99|FX 4 (atmosphere)|
|100|FX 5 (brigthness)|
|101|FX 6 (golblins)|
|102|FX 7 (echoes)|
|103|FX 8 (sci-fi)|
|104|Sitar|
|105|Banjo|
|106|Shamisen|
|107|Koto|
|108|Kalimba|
|109|Bag Pipe|
|110|Fiddle|
|111|Shanai|
|112|Tinkle Bell|
|113|Agogo|
|114|Steel Drums|
|115|Woodblock|
|116|Taiko Drum|
|117|Melodic Tom|
|118|Synth Drum|
|119|Reverse Cymbal|
|120| Guitar Fret Noise|
|121|Breath Noise|
|122|Seashore|
|123|Bird Tweet|
|124|Telephone Ring|
|125|Helicopter|
|126|Applause|
|127|Gunshot|







