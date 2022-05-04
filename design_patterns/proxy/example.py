class Image:
    def __init__(self, file_name) -> None:
        self._file_name = file_name

    def load_image_from_disk(self) -> None:
        print(f"Loading {self._file_name}")

    def display_image(self) -> None:
        print(f"Displaying {self._file_name}")


class Proxy:
    def __init__(self, subject) -> None:
        self._subject = subject
        self._proxystate = None


class ProxyImage(Proxy):
    def display_image(self) -> None:
        if self._proxystate is None:
            self._subject.load_image_from_disk()
            self._proxystate = 1

        print(f"Displaying {self._subject._file_name}")


proxy_image1 = ProxyImage(Image("1.jpg"))
proxy_image2 = ProxyImage(Image("2.jpg"))

proxy_image1.display_image()  # loading necessary
proxy_image1.display_image()  # loading unnecessary
proxy_image2.display_image()  # loading necessary
proxy_image2.display_image()  # loading unnecessary
proxy_image1.display_image()  # loading unnecessary
