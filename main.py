import re


def main():
    text = input('Digite seu texto aqui: ')
    korean = re.findall(r"[\w가-힣]+", text)
    
    print(f'teste isso {korean}')


if __name__ == "__main__":
    main()

