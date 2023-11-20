class GrammarStats:
    def __init__(self):
        self.history = []
        # self.percentage_true = 0
        # self.percentage_false = 0

    def check(self, text):
        if text[0].istitle():
            if text[-1] == ".":
                self.history.append(True)
                return True
            else:
                self.history.append(False)
                return False

    def percentage_good(self):
        return self.history.count(True) / len(self.history) * 100

    """
    Count the number of times check() is passing. 
    Create list to store number
    List needs to append itself whenever run again. 
    Find total number of tests to get percentage or number.

    Number of True / number of Fail * 100

    """


        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
