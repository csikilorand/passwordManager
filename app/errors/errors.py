class DataBaseExceptions(Exception):
    '''Base class for other type of exceptions'''    
    def __init__(self, message="Database error occured", context=None):
        self.message = message
        self.context = context
        super().__init__(self.message)


class NoDataAvailableException(DataBaseExceptions):
    pass

