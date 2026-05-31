def yanghui(n):
    """生成n行杨辉三角"""
    triangle = []  # 存储整个杨辉三角的二维列表
    for i in range(n):  # 遍历每一行
        row = [1] * (i + 1)  # 初始化当前行，首尾元素为1
        for j in range(1, i):  # 计算中间元素（不包含首尾）
            # 每个中间元素等于上一行相邻两元素之和
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)  # 将当前行添加到三角中
    return triangle

def print_yanghui(n):
    """打印n行杨辉三角"""
    tri = yanghui(n)  # 生成杨辉三角数据
    width = len(' '.join(map(str, tri[-1])))  # 计算最后一行字符串宽度，用于居中
    for row in tri:  # 遍历每一行
        print(' '.join(map(str, row)).center(width))  # 转换为字符串并居中打印

if __name__ == "__main__":
    n = int(input("输入行数: "))
    print_yanghui(n)
    print('end')
