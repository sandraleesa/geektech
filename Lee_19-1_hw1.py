class BMV:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color


    def start_engine(self):
        print(f"""
        {self.title} {self.model} engine started!
        """)


    def stop_engine(self):
        print(f"""
        {self.title} {self.model} engine stoped!
        """)


    def info(self):
        print(f"""
    Title: {self.title}
    Model: {self.model}
    Weight: {self.weight}
    HP: {self.hp}
    NM: {self.nm}
    Max Speed: {self.max_speed}
    Color: {self.color}
    """)


class Mercedes:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color


    def start_engine(self):
        print(f"""
        {self.title} {self.model} engine started!
        """)


    def stop_engine(self):
        print(f"""
        {self.title} {self.model} engine stoped!
        """)


    def info(self):
        print(f"""
    Title: {self.title}
    Model: {self.model}
    Weight: {self.weight}
    HP: {self.hp}
    NM: {self.nm}
    Max Speed: {self.max_speed}
    Color: {self.color}
    """)
