def yanghui(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def print_yanghui(n):
    tri = yanghui(n)
    width = len(' '.join(map(str, tri[-1])))
    for row in tri:
        print(' '.join(map(str, row)).center(width))

if __name__ == "__main__":
    n = int(input("输入行数: "))
    print_yanghui(n)
