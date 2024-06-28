# V미터 막대 올라감 -> A미터 내려가고 B미터 미끄러짐
import sys
r=range;input=sys.stdin.readline
A,B,V=map(int,input().split())
day=(V-B)/(A-B)
if day==int(day):
    print(int(day))
else:
    print(int(day)+1)