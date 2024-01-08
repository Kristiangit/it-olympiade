N = int(input())
for i in range(N):
    r1x1, r1y1, r1x2, r1y2 = map(int, input().split())
    r2x1, r2y1, r2x2, r2y2 = map(int, input().split())
    o1 = 2 * abs(r1x1 - r1x2) + 2 * abs(r1y1 - r1y2)
    o2 = 2 * abs(r2x1 - r2x2) + 2 * abs(r2y1 - r2y2)
    print(max(o1, o2))