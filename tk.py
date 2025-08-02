import sys
import os
import requests
import time
import random
from pystyle import Colorate, Colors, Write, Center

__Credit__ = 'TKhanh 🌟'

# Define a minimal set of confirmed gradients to avoid AttributeError
GRADIENTS = [
    Colors.red_to_yellow,
    Colors.blue_to_green,
    Colors.green_to_yellow,
    Colors.purple_to_red,
    Colors.cyan_to_green
]

def banner(gradient):
    banner_text = '''
     _____ _  _______ _          _ _       
    |_   _| |/ /_   _| |__   ___| | | ___  
      | | | ' /  | | | '_ \\ / __| | |/ _ \\ 
      | | | . \\  | | | | | | (__| | | (_) |
      |_| |_| \\_\\ |_| |_| |_| \\___|_|_|\\___|
   ╔════════════════════════════════════════╗
   ║ 🔥 Fb: https://fb.com/your-profile 🔥 ║
   ║ ✨ Version 1.0 - TKhanh 🌟 ✨        ║
   ╚════════════════════════════════════════╝
    '''
    print(Center.XCenter(Colorate.Vertical(gradient, banner_text, 1)))

def clear():
    os.system('cls' if sys.platform.startswith('win') else 'clear')

def load_tokens(file_list):
    tokens = []
    for file_name in file_list:
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                tokens.extend(line.strip() for line in lines if line.strip())
        except FileNotFoundError:
            print(Center.XCenter(f"\033[1;31mFile {file_name} không tồn tại!\033[0m"))
        except Exception as e:
            print(Center.XCenter(f"\033[1;31mLỗi khi đọc file {file_name}: {str(e)}\033[0m"))
    return tokens

def share(token, id_share):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US,en;q=0.9',
        'connection': 'keep-alive',
        'host': 'graph.facebook.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    try:
        url = f'https://graph.facebook.com/v15.0/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}'
        response = requests.post(url, headers=headers, timeout=10).json()
        return 'id' in response
    except Exception:
        return False

def main_share():
    clear()
    # Select random gradients for this run
    main_gradient = random.choice(GRADIENTS)
    success_gradient = random.choice(GRADIENTS)
    failure_gradient = random.choice(GRADIENTS)
    
    banner(main_gradient)
    Write.Print("🌈 Bắt Đầu Share Bot V1.0 - TKhanh 🌟 💥\n", main_gradient, interval=0.05)
    time.sleep(1.5)

    # Input token files with e/c options
    file_list = []
    while True:
        choice = input(Center.XCenter(
            "\033[1;31m[\033[1;37m+\033[1;31m] \033[1;37m=> \033[1m\033[38;5;208mNhập tên file chứa Tokens (e để tiếp tục chạy tool, c để nhập file khác): \033[1;93m"
        )).lower()
        if choice == 'e':
            if not file_list:
                print(Center.XCenter("\033[1;31m⚠ Chưa nhập file token nào!\033[0m"))
                continue
            break
        elif choice == 'c':
            print(Center.XCenter("\033[1;32mTiếp tục nhập file token khác.\033[0m"))
            continue
        else:
            file_list.append(choice)
    
    tokens = load_tokens(file_list)
    total_tokens = len(tokens)
    if total_tokens == 0:
        print(Center.XCenter("\033[1;31m⚠ Không có token hợp lệ nào trong các file!\033[0m"))
        return False

    id_share = input(Center.XCenter(
        "\033[1;31m[\033[1;37m+\033[1;31m] \033[1;37m=> \033[1m\033[38;5;208mNhập ID Cần Share: \033[1;93m"
    ))
    try:
        delay = int(input(Center.XCenter(
            "\033[1;31m[\033[1;37m+\033[1;31m] \033[1;37m=> \033[1m\033[38;5;208mNhập Delay Share (giây): \033[1;93m"
        )))
        total_shares = int(input(Center.XCenter(
            "\033[1;31m[\033[1;37m+\033[1;31m] \033[1;37m=> \033[1m\033[38;5;208mBao Nhiêu Share Thì Dừng: \033[1;93m"
        )))
    except ValueError:
        print(Center.XCenter("\033[1;31m⚠ Vui lòng nhập số hợp lệ cho delay và số share!\033[0m"))
        return False

    print(Center.XCenter(Colorate.Horizontal(main_gradient, f'═' * 60)))
    print(Center.XCenter(Colorate.Horizontal(main_gradient, f"🚀 Tổng số token: {total_tokens} 🚀")))

    # Process shares sequentially with simplified status UI
    stt = 0
    while stt < total_shares:
        token = tokens[stt % total_tokens]  # Cycle through tokens
        stt += 1
        Write.Print(f"⚡️ Đang share [{stt}/{total_shares}]... ", main_gradient, interval=0.02)
        success = share(token, id_share)
        status = "THÀNH CÔNG" if success else "THẤT BẠI"
        Write.Print(status + "\n", success_gradient if success else failure_gradient, interval=0.02)
        time.sleep(delay)
    
    print(Center.XCenter(Colorate.Horizontal(main_gradient, f'═' * 60)))
    Write.Print("🎉 Hoàn tất share! TKhanh 🌟 💥\n", main_gradient, interval=0.05)
    return True

if __name__ == "__main__":
    while True:
        try:
            success = main_share()
            if not success:
                continue
            choice = input(Center.XCenter(
                '\033[38;5;245m[\033[1;32mOPTIONS\033[38;5;245m] \033[1;32mNhấn [c] để chạy lại tool, [e] để dừng hoàn toàn: \033[1;93m'
            )).lower()
            if choice == 'c':
                continue
            else:  # Includes 'e' or any other input (e.g., Enter)
                print(Center.XCenter(
                    f'\033[38;5;245m[\033[1;32mOPTIONS\033[38;5;245m] \033[1;32mNhấn [c] để chạy lại tool, [e] để dừng hoàn toàn: \033[1;93m'
                ))
                print(Center.XCenter(
                    Colorate.Horizontal(random.choice(GRADIENTS), "🔥 Liên hệ: https://fb.com/your-profile 🔥")
                ))
                sys.exit()
        except KeyboardInterrupt:
            print(Center.XCenter(
                f'\033[38;5;245m[\033[38;5;9m!\033[38;5;245m] \033[38;5;9mĐã dừng tool! {__Credit__}\033[0m'
            ))
            print(Center.XCenter(
                Colorate.Horizontal(random.choice(GRADIENTS), "🔥 Liên hệ: https://fb.com/your-profile 🔥")
            ))
            sys.exit()
