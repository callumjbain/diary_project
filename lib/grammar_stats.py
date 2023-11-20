class GrammarStats:
    def __init__(self):
        self.percentage_list = []

    def check(self, text):
        if text[0].istitle():
            if text[-1] == ".":
                return True
            else:
                return False
        

    def percentage_good(self):

        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.

        pass

    """
    Count the number of times check() is passing. 
    Create list to store number
    List needs to append itself whenever run again. 
    Find total number of tests to get percentage or number.

    Number of True / number of Fail * 100

    """