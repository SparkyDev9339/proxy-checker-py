import requests

def check_proxy(proxy):
    try:
        response = requests.get("https://www.example.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Рабочий прокси: {proxy}")
    except:
        pass

def scan_proxies(file_path):
    with open(file_path, "r") as file:
        proxy_list = file.read().splitlines()
        for proxy in proxy_list:
            check_proxy(proxy)

def main():
    file_path = "proxy_list.txt"  # Укажите путь к вашему файлу с прокси
    scan_proxies(file_path)

if __name__ == "__main__":
    main()
