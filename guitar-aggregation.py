class Guitar:
    def __init__(self, strings):
        self.strings = strings

    def play(self):
        print(f'Playing on guitar with {self.strings.string_tension} tension strings.')


class Strings:
    def __init__(self, string_tension):
        self.string_tension = string_tension


strings = Strings('high')
yamaha = Guitar(strings)
yamaha.play()

strings_tension = strings.string_tension
print(strings_tension)
