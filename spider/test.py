def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('cuowu')
    else:
        while(n-2) > 0:
            print(n3)
            n3 = n2+n1
            n1 = n2
            n2 = n3
            n -= 1




def main():
    fab(10)


main()
