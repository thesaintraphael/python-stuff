import threading
from typing import List, Tuple, Union


class EmailThread(threading.Thread):
    def __init__(
        self, subject: str, content: str, receivers: Union[Tuple, List]
    ) -> None:
        self.subject = subject
        self.content = content
        self.receivers = receivers

        threading.Thread.__init__(self)

    def send(self):
        """Imaginary :D email sending function"""

    def run(self) -> None:
        self.send()
