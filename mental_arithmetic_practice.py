# 運算部分由淳編寫，兩點式部分由球爸程式改編

from math import gcd
from random import sample
from time import sleep


def operations() -> None:
    print('接下來請直接輸入答案')
    sleep(1)
    print('程式將一直執行下去，若想停止請按下 "Ctrl+C"')
    sleep(1)
    print('答對得 1 分，答錯倒扣 1 分，無時間限制')
    sleep(1)

    content_choice = input('請選擇訓練內容 (A)加法 (B)減法 (C)乘法 (D)指數\n:').upper()
    score = 0
    limit = int(input('請輸入數值範圍：'))

    while True:
        num1, num2 = sample(range(1, limit), 2)

        match content_choice:
            case 'A':
                symbol, ans = '+', num1 + num2
            case 'B':
                symbol, ans = '-', num1 - num2
            case 'C':
                symbol, ans = '*', num1 * num2
            case 'D':
                symbol, ans = '^', num1**num2
            case _:
                print('無效的選擇，請重新啟動')
                break

        try:
            user_input = int(input(f'{num1} {symbol} {num2} = '))
        except ValueError:
            print('請輸入數字！')
            continue

        if user_input == ans:
            score += 1
            print(f'恭喜答對了，你獲得了 1 分\n你目前有 {score} 分')
        else:
            score -= 1
            print(f'可惜答錯了，你失去了 1 分，正確答案為：{ans}\n你目前有 {score} 分')

        sleep(1)


def two_point_form() -> int | tuple[int]:
    t = int(input('請問一題要幾秒（建議從 7 秒開始練習）：'))
    m = int(input('數值範圍（建議 "7", 得到 -7~7 的整數）：'))

    print('接下來無需輸入，在心裡求得答案後，再看顯示出的答案是否如預期即可')
    sleep(1)

    while True:
        x1, y1, x2, y2 = sample(range(-m, m + 1), 4)
        if x1 == x2 and x2 == y2:
            continue

        sleep(1)
        print(f'({x1},{y1}), ({x2},{y2})，求過兩點的方程式')

        d = [abs(x1 - x2), abs(y1 - y2)]
        g = gcd(*d)
        d = [d[0] // g, d[1] // g]
        c = d[1] * x1 - d[0] * y1

        sleep(t)
        if d[0] == 0 or d[1] == 0:
            print(f'x = {x1}' if d[0] == 0 else f'y = {y1}')
        else:
            print(
                f'{d[1] if d[1] != 1 else ""}x {"-" if d[0] > 0 else "+"} {abs(d[0]) if abs(d[0]) != 1 else ""}y = {c}'
            )
        sleep(1)


def main() -> None:
    match input('請問你要練習什麼 (A)基本運算/次方運算 (B)兩點式練習\n:').upper():
        case 'A':
            operations()
        case 'B':
            two_point_form()
        case _:
            print('你是來亂的嗎？')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'發生 {type(e).__name__} 錯誤\n錯誤訊息：{e}')
