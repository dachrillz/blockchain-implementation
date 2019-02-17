from abc import ABCMeta, abstractmethod


class IIO:
    '''
    This class provides an interface to IO
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def create_transaction(self):
        raise NotImplementedError
