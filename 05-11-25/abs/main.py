from abc import abstractmethod,ABC

class Song(ABC):
    # @expr => decorators
    @abstractmethod
    def playSong():
        pass
    @abstractmethod
    def pauseSong():
        pass