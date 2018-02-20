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
|1. | Bright Acoustic Piano|
|2. | Electric Grand Piano|
|3. | Honky-tonk Piano|
|5. | Electric Piano 1|
|6. | Electric Piano 2|
|7. ||
|8. ||
|9. ||
|10. ||
|11. ||
|12. ||
|13. ||
|14. ||
|15. ||
|16. ||
|17. ||
|18. ||
|19 ||
|20 ||
21||
22||
23||
24||
25||
26||
27||
28||
29||
30||
31||
32||
33||
34||
35||
36||
37||
38||
39||
40||
41||
42||
43||
44||
45||
46||
47||
48||
49||
50||
51||
52||
53||
54||
55||
56||
57||
58||
59||
60||
61||
62||
63||
64||
65||
66||
67||
