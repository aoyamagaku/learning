class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def complete(self):
        self.done = True

    def __str__(self):
        if self.done:
            mark = '[x]'
        else:
            mark = '[ ]'
        return f'{mark} {self.title}'