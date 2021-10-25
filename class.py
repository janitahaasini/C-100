class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.color=color
        self.company=company
        self.speedlimit=speedlimit
        self.model=model
    def start(self):
        print("started")
        print(self.color)
    def stop(self):
        print("stopped")
        print(self.model)
    def accelerate(self):
        print("accelarated")
        print(self.speedlimit)
def main():
    audi=Car("A6","Red","Audi","80")
    audi.start()
    audi.stop()
    audi.accelerate()

main()