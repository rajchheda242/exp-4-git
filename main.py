def add(a, b):
    pass
from add import add
from sub import sub
from mul import mul

def main():
    print("add:", add(2, 3))
    print("sub:", sub(5, 2))
    print("mul:", mul(3, 4))


if __name__ == "__main__":
    main()


