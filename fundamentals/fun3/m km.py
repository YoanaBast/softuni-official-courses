# 2. Convert Meters to Kilometers
#
# You will be given an integer that represents a distance in meters.
# Write a program that converts meters to kilometers formatted to the second decimal point.
meter = int(input())
km = meter / 1000
print(f'{km:.2f}')