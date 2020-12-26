class Laptop:
    def __init__(self):
        text_file = Data("Content of text file")
        image = Data("Content of image")
        app = Data("Content of app")
        self.dataset = [text_file, image, app]

    def show_data(self):
        print(self.dataset)
        for data in self.dataset:
            print(data.content)


class Data:
    def __init__(self, content):
        self.content = content


mac = Laptop()
mac.show_data()
