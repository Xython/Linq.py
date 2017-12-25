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


class ScanGenerator:
    def __init__(self, rule, seq, start_elem):
        self.rule = rule
        self.seq = seq
        self.start_elem = start_elem

    def __iter__(self):
        last = self.start_elem
        for now in self.seq:
            acc = self.rule(last, now)
            yield acc
            last = acc
