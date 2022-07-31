"https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=false"

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB=int(input())
BC=int(input())

CA=math.hypot(AB,BC)
MC=CA/2
BCA=math.asin(1*AB/CA)
BM=math.sqrt((BC**2+MC**2)-(2*BC*MC*math.cos(BCA)))
MBC=math.asin(math.sin(BCA)*MC/BM)

print(int(round(math.degrees(MBC),0)),'\u00B0',sep='')