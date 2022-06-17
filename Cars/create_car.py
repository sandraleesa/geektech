class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def start_engine(self):
        print(f'Engine of {self.name} started!')

    def stop_engine(self):
        print(f'Engine of {self.name} stoped!')
