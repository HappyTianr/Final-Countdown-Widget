import time

def timer(minutes):
    print('开始计时')
    seconds = minutes * 60
    while True:
        print(f"Time remaining: {seconds // 60:02d}:{seconds % 60:02d}")
        time.sleep(1)
        seconds -= 1
        if seconds == 0:
            print('Time remaining: 00:00')
            new = input('q：退出，e：重来：')
            if new == 'e':
                seconds = minutes * 60
                continue
            if new == 'q':
                break

timer(1)  # 倒计时时间