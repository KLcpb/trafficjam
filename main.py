import random
import matplotlib.pyplot as plt

dt = 0.01

#TODO constrain the max speed of a car
#TODO jam force rate

class car():
    def __init__(self):
        self.d0 = random.randint(2,7)
        self.reaction_time = random.randint(2,5)/10
        self.v = random.randint(5,35)
        self.alpha = 0.05 #TODO check
        self.beta = 0.25
        self.x = random.randint(0,1000)
        self.road = random.randint(0,3)
    def getDistance(self,other):
        return other.x - self.x
    def getRelativeSpeed(self,other):
        return self.v - other.v
    def process(self,other):
        if other == None:
            self.x += dt * self.v
        else:
            if self.getDistance(other) < self.d0/2: # anti collision
                self.v = other.v
            else:
                self.v +=  dt* ((self.alpha*(self.getDistance(other) - self.d0)) + self.beta*(other.v - self.v))
                self.x += self.v*dt
    def getX(self):
        return self.x

'''carA = car(0,20)
carB = car(100,60)
la = []
lb = []
for i in range(int(20/dt)):
    la.append(carA.getX())
    lb.append(carB.getX())
    carA.process(carB)
    carB.process(None)
plt.plot(la)
plt.plot(lb)
plt.show()'''

#description: when one car slows down, it sufficiently influence the average speed
N = 10
cars = [[] for i in range(N)]
for j in range(N):
    for i in range(10): #10 cars
       cars[j].append(car())

for j in range(N):
    cars[j].sort(key=lambda c: c.x,reverse=True) #cars are sorted and placed in 3 lines

data= [[] for i in range(N)]
avg_speeds = []
for k in range(int(60/dt)):

    for i in range(N):
        if i == 0:
            cars[0][i].process(None)
        else:
            cars[0][i].process(cars[0][i-1])
        data[i].append(cars[0][i].getX())
    if k == int(20/dt):
        for i in range(1,N,10):
            cars[0][i].v = 0

    speeds = []
    for i in range(N):
        speeds.append(cars[0][i].v)
    avg_speed = sum(speeds)/len(speeds)
    avg_speeds.append(avg_speed)
    speeds = []

for i in range(N):
    plt.plot(data[i])
plt.show()
plt.plot(avg_speeds)
plt.show()
'''carA = car(0,150)
carB = car(30,30)
la = []
lb = []
for i in range(int(10//dt)):
    carB.process(None)
    carA.process(carB)

    # carA.process(carB)
    lb.append(carA.getX())
    la.append(carB.getX())

    print(carB.getX())

plt.plot(la)
plt.plot(lb)
plt.show()'''