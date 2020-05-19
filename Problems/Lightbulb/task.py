class Lightbulb:
    def __init__(self):
        self.state = "off"

    def change_state(self):
        self.state = "off" if self.state == "on" else "on"
        print(f"Turning the light {self.state}")
