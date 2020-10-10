class NoKeysFoundException(Exception):
    def __init__(self):
        super(NoKeysFoundException, self).__init__(
            f"No TEKs found on exposure keys export file.")
