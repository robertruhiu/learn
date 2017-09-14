class clock:
    def __init__(self,frame,color):
        self.frame=frame
        self.color=color

    def get_state(self):
        print("The clock frame is {} and the color is {} ".format(self.frame,self.color))
upstair_clock= clock("circle","blue")
upstair_clock.get_state()


