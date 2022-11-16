import glob
import pretty_midi
import pandas as pd


def get_hanon_dataset_meta() -> pd.DataFrame:
    hanon_directories = glob.glob("./tmp/hanon/*")

    hanon_records = []
    for hanon_dir in hanon_directories:
        paths = glob.glob(hanon_dir + "/*")
        label = hanon_dir.split("/")[-1]
        for path in paths:
            record = {
                "label": label,
                "path": path,
            }
            hanon_records.append(record)

    df = pd.DataFrame(hanon_records)
    return df


def load_midi(path: str) -> pd.DataFrame:
    midi_data = pretty_midi.PrettyMIDI(path)

    instrument = midi_data.instruments[0]
    records = []
    note_number = 0
    for note in instrument.notes:
        record = {
            "start": note.start,
            "end": note.end,
            "pitch": note.pitch,
            "velocity": note.velocity,
        }
        records.append(record)
        note_number += 1

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    hanon_dataset = get_hanon_dataset_meta()
    sample_record = hanon_dataset.sample().iloc[0]
    midi = load_midi(sample_record.path)
    print("Record class:", sample_record.label)
    print("Number of notes:", midi.shape[0])
