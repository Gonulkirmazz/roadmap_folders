#################
# Exercise 4
# Rewrite your pay computation program (previus chapter) with time-and-a-half for overtime
# and create a function called computepay which takes two parameters (hours and rate).

def computepay(hour, rate):
    if hour > 0 and rate > 0:
        pay = (0.5 * float(rate) * hour)
        return (float(hour) * float(rate) + pay)


print(computepay(45, 10))
