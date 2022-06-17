from create_car import Car


class Cars(Car):
    def __init__(self, name, model, engine):
        super(Cars, self).__init__()

    def get_car_info(self):
        print(f"""Name: {self.name},
                  Model: {self.model},
                  Engine: {self.engine}
              """)