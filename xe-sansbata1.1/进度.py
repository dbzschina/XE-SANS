import sys

# 打印，不换行
def print_nl(text):
    sys.stdout.write(text)
    sys.stdout.flush()

# 删除当前行末尾n个字符，默认删1个，增加防负数保护
def erase_back(n=1):
    if n <= 0:
        return
    sys.stdout.write("\b"*n + " "*n + "\b"*n)
    sys.stdout.flush()

# 专门用来换行（单独调用）
def new_line():
    sys.stdout.write("\n")
    sys.stdout.flush()

# 【函数1：输出进度条】固定100格，参数：百分比、提示文字
def draw_bar(percent_val, msg):
    BOX1_COUNT = 100
    filled = int(BOX1_COUNT * percent_val / 100)
    bar_text = "[" + "#"*filled + "-"*(BOX1_COUNT-filled) + f"] {percent_val:.0f}%，{msg}"
    print_nl(bar_text)
    return len(bar_text) # 返回本次输出字符串长度，给删除函数用

# 【函数2：删除进度条】参数n：上一次输出一共多少字符
def erase_bar(n):
    erase_back(n)

# ============ 使用示例 ============
"""
l = draw_bar(1, "正在加载SYS和策略1")
import time
null = None
time.sleep(0.5)
erase_bar(l)
l = draw_bar(2, "正在加载SYS和策略1")
time.sleep(1)
erase_bar(l)
l = draw_bar(3, "正在读取配置")
sb_SB = 0
time.sleep(0.5)
erase_bar(l)
l = draw_bar(4, "正在读取配置")
time.sleep(0.5)
erase_bar(l)
l = draw_bar(5, "正在读取配置")
time.sleep(0.5)
erase_bar(l)
l = draw_bar(6, "正在保存")
time.sleep(0.5)
erase_bar(l)
l = draw_bar(7, "正在加载配置")
time.sleep(1)
erase_bar(l)
l = draw_bar(8, "正在加载配置")
time.sleep(0.1)
erase_bar(l)
l = draw_bar(9, "正在加载配置")
time.sleep(0.1)
erase_bar(l)
l = draw_bar(10, "正在加载配置")
time.sleep(0.1)
erase_bar(l)
l = draw_bar(11, "正在加载配置")
time.sleep(0.1)
erase_bar(l)
l = draw_bar(12, "正在加载配置")
time.sleep(5)
erase_bar(l)
l = draw_bar(37, "正在加载配置")
time.sleep(2)
erase_bar(l)
l = draw_bar(38, "正在保存")
time.sleep(1)
erase_bar(l)
sb_SB = 39
while True:
    if sb_SB == 95:
        break
    else:
        l = draw_bar(sb_SB, "正在加载配置")
        time.sleep(0.3)
        erase_bar(l)
        sb_SB = sb_SB + 1

l = draw_bar(96, "正在保存配置")
time.sleep(4)
erase_bar(l)
l = draw_bar(97, "正在准备")
time.sleep(1)
erase_bar(l)
l = draw_bar(98, "正在准备")
time.sleep(1)
erase_bar(l)
l = draw_bar(99, "正在准备")
time.sleep(2)
erase_bar(l)
l = draw_bar(100, "完成！")
time.sleep(1)
new_line()
"""