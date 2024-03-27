from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def select_menu(self):
        pass

    @abstractmethod
    def display_main_menu(self):
        pass
