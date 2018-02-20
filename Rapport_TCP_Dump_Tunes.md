# Report of TCP Dump Tunes

## Introduction

This report is about a Python Script called TCP_Dump_Tunes.py, the creator is https://github.com/nickpegg/tcpdump-tunes.
I have just modifiert the Scrip and add some New Instruments.
The Script Transform data traffic into "Random" generated Music one example you can find is the link https://github.com/Dezmo767/internship/ with the file name test_just-wow it is an midi file type.

### What does the scirpt do?
The script TCP Dump tunes interprets some IP packets captured using TCPDump Unix Tool and generaes a MIDI audio file out of it. 

### What is TCPDumpTool

A Python script that was createdd by NAME and hosted GITHUB WEB ADDRESS. It was created on DATE and last modified on DATE. 

## Installation Ubuntu/Linux Version 14.04 LTS

+ install Python with the command ```sudo apt-get install python3```
+ install Python pip with the command ```sudo apt-get install python3-pip```
+ install python midi with the command ```sudo pip install git+https://github.com/vishnubob/python-midi@feature/python3```

+ Clone my github directory with the command ```git clone git@github.com:Dezmo767/internship.git``` then you can start.

## Running the script
+ Go to repo
+

<b><i> Tips: The best command is <u> sudo tcpdump -i any -n -c 1000 | ~/internship/Midi_Tunes/TCP_Dump_Intern.py -f test_just-wow </u></i></b>
