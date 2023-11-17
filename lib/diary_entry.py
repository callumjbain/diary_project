class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        

    def format(self):
        return f"{self.title}: {self.contents}"
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        

    def count_words(self):
        return len(self.contents.split())
        # Returns:
        #   int: the number of words in the diary entry
        

    def reading_time(self, wpm):
        self.wpm = wpm
        return len(self.contents.split()) / wpm
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        

    def reading_chunk(self, wpm, minutes):
        self.wpm = wpm
        self.minutes = minutes

        num_of_words = minutes * wpm
        return self.contents[:num_of_words]

        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        