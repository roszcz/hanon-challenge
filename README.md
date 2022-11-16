To get the MIDI data:

```sh
wget -O tmp/hanon.zip https://storage.googleapis.com/sacrebleu-development/hanon.zip
unzip tmp/hanon.zip -d tmp/
```

### Hanon classification challenge

Midi files are grouped in directory structure: `hanon/0x{NN}/{file_name}.mid`, where *NN* indicates the exercise number.
The goal is to develop an algorithm that can classify a short fragment of a midi record (couple of seconds or couple of notes)
as one of the *NN* Hanon exercises.

Basic code to load the data is included:

```sh
python main.py

Record class: 0x02
Number of notes: 226
```
