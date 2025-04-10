for num in range (1000, 2001):
    import time
    if num % 11 == 5:
        print(f'O numero é {num}.')
        time.sleep(1)

        numero = 1000
        while numero <=2000:
            if numero % 11 == 5:
                print (f'O numero é {numero}.')
