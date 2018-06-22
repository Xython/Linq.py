class Generator:
    """
    >>> stream = Generator(lambda x: x+1,  0)
    >>> a, b, c = map(lambda _: next(stream), [None, None, None])
    >>> assert [a, b, c] == [1, 2, 3]
    """
    def __init__(self, rule, start_elem):
        self.rule = rule
        self.start_elem = start_elem

    def __iter__(self):
        now = self.start_elem
        rule = self.rule
        while True:
            try:
                yield now
                now = rule(now)
            except StopIteration:
                break


class ScanGenerator:
    """
    >>> stream = ScanGenerator(lambda a, b: a + b, [1, 2, 3], 0)
    >>> assert list(stream) == [1, 3, 6]
    """
    def __init__(self, rule, seq, start_elem):
        self.rule = rule
        self.seq = seq
        self.start_elem = start_elem

    def __iter__(self):
        last = self.start_elem
        rule = self.rule
        for now in self.seq:
            acc = rule(last, now)
            yield acc
            last = acc
