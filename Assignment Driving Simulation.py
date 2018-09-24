
t = int(input("Insert Time: "))
a = int(input("Insert Acceleration: "))
d = int(input("Insert Distance: "))
T = 0
A = 0
V = 0
D = 0

print("(The * indicates every 10m)")
while T <= t:
    v = int(V + a * T)
    D = int((t*(v+V))/2)
    print("Duration:" ,T, "Distance:","*" * (D//10))
    T = T + 1

if v> 60:
    v = int(V + a * T)
    V = "The person went over the speed limit."
    print(V)
    print("Max speed was" ,v, "m/s")
else:
    print("The person did not go over the speed limit.")
    print("Max speed was " ,v, "m/s")

if D >= d:
    print("The person reached the destination. ")
    print("Reached",D, "m")
else:
    print("The person did not reach the destination. ")
    print("Reached",D,"m")






