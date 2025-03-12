# REPLACE BELOW WITH CHATGPT RESULT

# Defining the MIDI values for the chord progression from The Beatles' "Yellow Submarine" in G major
chords = [
    [55, 59, 62],  # G major chord (I)
    [59, 63, 67],  # C major chord (IV)
    [67, 71, 74],  # D major chord (V)
    [55, 59, 62]   # G major chord (I) (repeat)
]

# DON'T CHANGE ANYTHING BELOW THIS



import mido
from mido import MidiFile, MidiTrack, Message

# Assuming 480 ticks per beat
ticks_per_beat = 480

def create_midi_file(filename):
    midi_file = MidiFile(ticks_per_beat=ticks_per_beat)
    track = MidiTrack()
    midi_file.tracks.append(track)

    time = 0
    duration = ticks_per_beat * 4  # 4/4 whole note duration

    for chord in chords:
        for note in chord:
            track.append(Message('note_on', note=note, velocity=78, time=time))
        for i, note in enumerate(chord):
            if i == 0:
                track.append(Message('note_off', note=note, velocity=78, time=duration))
            else:
                track.append(Message('note_off', note=note, velocity=78, time=0))

        # Add a time delay before the next chord
        time += time

    # Save the MIDI file
    midi_file.save(filename)
    print(f"MIDI file '{filename}' generated successfully.")

if __name__ == "__main__":
    file_name = "output.mid"
    create_midi_file(file_name)