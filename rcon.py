import time

import mcrcon
import random

al = 20  # 排序数组范围
# 设置RCON
rcon_host = "your host"
rcon_pwd = "your password"
rcon_port = "your rcon port"
height = 80
block1 = "diamond_block"
block2 = "air"
x_offset = 128
y_offset = 128
clrange = 40
block1d = {
    1: "diamond_block",
    2: "gold_block"
}

s = 0

rcon = mcrcon.MCRcon(rcon_host, rcon_pwd, rcon_port)
rcon.connect()


def place(x, y, block):
    rcon.command(f"setblock {x + x_offset} {height} {y + y_offset} {block}")


def clear():
    rcon.command(
        f"fill {x_offset - clrange} {height} {y_offset - clrange} {x_offset + clrange} {height} {y_offset + clrange} air")


def sba(arr):
    global s
    amax = max(arr)
    length = len(arr)
    for i in range(amax, 0, -1):
        for j in range(0, length, 1):
            if arr[j] > i - 1:
                place(i, j, block1d[s % 2 + 1])
            else:
                place(i, j, "air")
    s += 1


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            sba(arr)


clear()

arr = []
for i in range(al):
    arr.append(i)
sba(arr)
time.sleep(1)
for i in range(al):
    arr[i] = random.randint(0, al - 1) + 1
sba(arr)
time.sleep(1)
bubbleSort(arr)
rcon.command("tellraw @a {\"text\":\"Done!\"}")
