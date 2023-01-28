not_implemented_error_msg = "This method has not been implemented."


# TODO = you can also convert this class into abstract class and define models as abstract method

class SampleDataException(Exception):
    def __init__(self,message,errors = " "):
        print("message coming from our custom Exception class.")
        super().__init__(message)
        self.errors=errors


class ResourceBase(object):
    """
    base class representing required methods to be implemented by all resource classes.
    """

    #TODO - add all reources in this list
    resources = ["planets","spaceships","people","vehicles"]

    def __init__(self):
        self.home_url = "https://swapi.dev/"

    def get_count(self):
        raise NotImplementedError (not_implemented_error_msg)

    def get_resource_url(self,resource):
        raise NotImplementedError (not_implemented_error_msg)

    def get_sample_data(self):
        raise SampleDataException (not_implemented_error_msg)