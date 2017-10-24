def faktoriyel(n):
  if n<=1:
      return 1
  else:
      return n*faktoriyel(n-1)

def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print("YARDIMCI FONKSIYON")
if __name__ == "__main__":
    main