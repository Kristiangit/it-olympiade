N = int(input())
for i in range(N):
    r1x1, r1y1, r1x2, r1y2 = map(int, input().split())
    r2x1, r2y1, r2x2, r2y2 = map(int, input().split())
    fullO = 2 * abs(r1x1 - r1x2) + 2 * abs(r1y1 - r1y2) + 2 * abs(r2x1 - r2x2) + 2 * abs(r2y1 - r2y2)

    fullO -= 2 * abs(max(r1x1, r2x1) - min(r1x2, r2x2)) + 2 * abs(max(r1y1, r2y1) - min(r1y2, r2y2))
    print(fullO)

"""
1
2 4 7 8
6 5 9 11
"""
"""
1
4 4 10 6
6 2 8 8
"""