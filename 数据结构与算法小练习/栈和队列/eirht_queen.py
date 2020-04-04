"""
实现八皇后问题
"""
import copy

count = 0  # 解法个数


def not_danger(row: int, column: int, chess: list):
    """
    判断给定棋盘的位置是否危险
    即判断该位置的行，列，两条斜线上是否有皇后
    由于同一行的位置会被清零，列方向也可以判定给定的位置上是否已有皇后（保证不同的解法），
    所以只需判断列和斜线方向即可
    :param row: 给定行
    :param column: 给定列
    :param chess: 给定棋盘
    :return: True: 不危险，False：危险
    """
    flag1 = False  # 列
    flag2 = False  # 左上角
    flag3 = False  # 右下角
    flag4 = False  # 左下角
    flag5 = False  # 右上角
    # 判断列方向
    for i in range(8):
        if chess[i][column] == 1:
            flag1 = True
            break
    # 判断左上角
    i = row - 1
    j = column - 1
    while i >= 0 and j >= 0:
        if chess[i][j] == 1:
            flag2 = True
            break
        i -= 1
        j -= 1
    # 判断右下角
    i = row + 1
    j = column + 1
    while i < 8 and j < 8:
        if chess[i][j] == 1:
            flag3 = True
            break
        i += 1
        j += 1
    # 判断左下角
    i = row + 1
    j = column - 1
    while i < 8 and j >= 0:
        if chess[i][j] == 1:
            flag4 = True
            break
        i += 1
        j -= 1
    # 判断右上角
    i = row - 1
    j = column + 1
    while i >= 0 and j < 8:
        if chess[i][j] == 1:
            flag5 = True
            break
        i -= 1
        j += 1
    if flag1 or flag2 or flag3 or flag4 or flag5:
        return False
    return True


def eight_queen(row: int, columns: int, chess: list):
    """
    使用递归算法实现八皇后问题
    确定每行的安全位置
    :param row:初始行
    :param colums:列数
    :param chess:初始棋盘
    :return:
    """
    global count
    temp_chess = copy.deepcopy(chess)
    if row == 8:
        count += 1
        # 该种解法已经实现，每行都有安置了皇后
        print("第{}种解法".format(count))
        for i in range(8):
            for j in range(8):
                print(temp_chess[i][j], end=" ")
            print()

    else:
        # 查找该行中的安全位置安置皇后
        for k in range(columns):
            if not_danger(row, k, temp_chess):
                # 如果位置安全，则将改行内容全改为0（将原有皇后清除）
                for c in range(columns):
                    temp_chess[row][c] = 0
                # 再将该位置设置为1,放置皇后
                temp_chess[row][k] = 1
                # 该行皇后位置已经确定,前往下一行
                eight_queen(row + 1, columns, temp_chess)


if __name__ == '__main__':
    # 初始化棋盘，为空棋盘
    chess = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(0)
        chess.append(row)
    row = 0
    columns = 8
    # 从第0行开始排查，每行给出一个安全位置
    eight_queen(row, columns, chess)
