from datetime import date, timedelta


inp1 = list(map(int, input().split()))
inp2 = int(input())

x = date(*inp1)
y = timedelta(inp2)
result = x + y

print(result.year, result.month, result.day)
