octave_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
octave_flat =  ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

class Scale(object):
    def __init__(self, start, name, intervals=""):
        if len(start) > 1:
            self.start = start[0].upper() + start[1]
            oct_type = start[1]
        else:
            self.start = start[0].upper()
            oct_type = "?"
        self.name = start.upper() + " " + name
        self.intervals = intervals
        self.pitches = []
        if intervals == "":
            #why? Why??? WHY??????
            if self.start[0] == 'F':
                octave = octave_flat
            else:
                octave = octave_sharp
            idx = octave.index(self.start)
            self.pitches = octave[idx:] + octave[:idx]
        else:
            if oct_type == "b":
                octave = octave_flat
            elif oct_type == "#":
                octave = octave_sharp
            else:
                octave = octave_sharp
            #why? Why??? WHY??????
            if start == 'g' or start == 'd':
                octave = octave_flat
            idx = octave.index(self.start)
            self.pitches.append(octave[idx])
            for ch in self.intervals[:-1]:
                if ch=='M':
                    idx_dx = 2
                elif ch=='m':
                    idx_dx = 1
                elif ch=='A':
                    idx_dx = 3
                else:
                    raise ValueError
                idx += idx_dx
                if idx >= len(octave):
                    idx = idx - len(octave)
                self.pitches.append(octave[idx])



