n=int(input())
travel_time = int(input())
time_remianing= 240-travel_time
count = 0
for i in range(1,n+1):
    solve_time=i*5
    if solve_time < time_remianing and time_remianing > 0:
        count += 1
        time_remianing -= solve_time
    else:
        break
print(count)
