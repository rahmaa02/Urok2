class Cars:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f' {self.name}    поехала ')

    def stop(self):
        print(f'{self.name}     остановилась ')

    def turn(self, direction):
        print(f'{self.name}     повернула {direction} ')


class TownCar(Cars):
    pass

class SportCar(Cars):
    pass

class WorkCar(Cars):
    pass

class PoliceCar(Cars):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

TownCarr=TownCar(100,'green','Town')
SportCarr=SportCar(100, 'black', 'Sport')
WorkCarr=WorkCar(111, 'black', 'Work')
PoliceCarr=PoliceCar(123, 'blue', 'Police')

TownCarr.go()
SportCarr.stop()
WorkCarr.turn('left')
PoliceCarr.go()