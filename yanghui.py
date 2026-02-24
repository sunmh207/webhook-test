def yanghui(n):
    """生成杨辉三角"""
    triangle = []
    for i in range(n):
        # 每行首尾元素为1
        row = [1] * (i + 1)
        # 计算中间元素：当前位置 = 上一行相邻两数之和
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def print_yanghui(n):
    """打印杨辉三角"""
    tri = yanghui(n)
    # 计算最后一行宽度用于居中
    width = len(' '.join(map(str, tri[-1])))
    for row in tri:
        print(' '.join(map(str, row)).center(width))

if __name__ == "__main__":
    n = int(input("输入行数: "))
    print_yanghui(n)
