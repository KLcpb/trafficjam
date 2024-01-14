from main import car
import matplotlib.pyplot as plt

dt = 0.01
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