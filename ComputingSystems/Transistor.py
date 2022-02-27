class NTypeTransistor:
    # terminal connections
    drain = None
    source = None
    gate = None

    def __init__(self, drain, source, gate):
        self.drain = drain
        self.source - source
        self.gate = gate

    def set_drain(self, drain):
        self.drain = drain

    def set_source(self, source):
        self.source = source

    def set_gate(self, gate):
        self.gate = gate

    def set_power(self):
        if self.gate.has_voltage():
            self.drain.set_power(self.source.has_voltage())
        else:
            self.drain.set_power(False)


