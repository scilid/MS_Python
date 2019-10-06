"""
    作者：一笑了之
    功能：对一组数据进行选择排序，使之最终按升序排列，用于演示VS Code和
          Pycharm的调试。
    版本：1.0
    日期：01/10/2019
"""
import numpy as np


def select(arr):
    # 各趟选择排序
    for i in range(0, len(arr)):
        # 初始化k,让k一开始指向每一趟的开始元素
        k = i
        # 每一趟排序的过程
        for j in range(i+1, len(arr)):
            # 如果j所指向的当前元素小于k所指向的元素，
            # 那么让K指向当前元素，相当于每趟找到一个最小值
            if arr[j] < arr[k]:
                k = j
        # 将k所指的每趟最小元素与每趟的开始元素交换位置
        arr[i], arr[k] = arr[k], arr[i]


def main():
    marry = np.random.randint(10, size=10)
    print(marry)
    select(marry)
    print(marry)


if __name__ == '__main__':
    main()
