from queue import Lifoqueue
s = Lifoqueue(maxsize=3)
print(s.qsize())

s.puy('a')
s.put('b')
s.put('c')

print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())

print(s.empty())

