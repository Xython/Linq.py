class Generator:
    def __init__(self, rule, start_elem):
        self.rule = rule
        self.start_elem = start_elem

    def __iter__(self):
        now = self.start_elem
        while True:
            try:
                yield now
                now = self.rule(now)
            except StopIteration:
                break