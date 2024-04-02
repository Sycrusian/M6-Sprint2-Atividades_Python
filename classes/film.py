class Film:

    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration
        self.number_of_exhibitions = 0

    def __str__(self):
        return f'<Film: {self.title}>'

    def __len__(self):
        return self.duration
