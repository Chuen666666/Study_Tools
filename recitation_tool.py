from os import name, system
from random import shuffle

qa, wrong = {}, []

def test(q: str, a: str) -> None:
    amount = int(input(f'請問有多少個 {q} 要背：'))

    for i in range(1, amount+1):
        que = input(f'請輸入第 {i} 個 {q}：').lower()
        ans = input(f'請輸入其 {a}：').lower()
        qa[que] = ans

    items = list(qa.items())
    shuffle(items)

    input('測驗即將開始\n按下 "Enter" 以繼續...')
    system('cls' if name == 'nt' else 'clear')

    for k, v in items:
        user_ans = input(f'請輸入 "{v}" 的 {q}：').lower()

        if user_ans == k:
            print('恭喜答對！')
        else:
            print(f'可惜答錯 正確答案應該是 "{k}"')
            wrong.extend([v, k, user_ans])

    input('測驗完成！將公布成績！\n按下 "Enter" 以繼續...')
    system('cls' if name == 'nt' else 'clear')

    if not wrong:
        print('\n恭喜全對！')
    else:
        print(f'\n可惜錯了{len(wrong) // 3}題：')
        for j in range(0, len(wrong), 3):
            print(f'題目：{wrong[j]} | 答案：{wrong[j+1]} | 作答：{wrong[j+2]}')

    print('請再接再厲！')

def main() -> None:
    match input('請問你要背什麼 (A)英文單字 (B)國文註釋\n:').upper():
        case'A':
            test('英文單字', '中文')
        case 'B':
            test('詞語', '註釋')
        case _:
            print('滾')
            return

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'發生 {type(e).__name__} 錯誤\n錯誤訊息：{e}')