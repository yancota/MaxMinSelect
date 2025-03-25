def max_min_select(numeros, primeiro, ultimo):
    if primeiro == ultimo:
        return arr[primeiro], arr[primeiro]
    
    if ultimo == primeiro + 1:
        if arr[primeiro] < arr[ultimo]:
            return arr[primeiro], arr[ultimo]
        else:
            return arr[ultimo], arr[primeiro]

    mid = (primeiro + ultimo) // 2
    min1, max1 = max_min_select(arr, primeiro, mid)
    min2, max2 = max_min_select(arr, mid + 1, ultimo)

    return min(min1, min2), max(max1, max2)

if __name__ == "__main__":
    arr = []
    print("Insira um número. Digite 'OK' para concluir.")

    while True:
        num = input("Digite um número: ")
        if num == "OK" or num == "Ok" or num == "ok":  
            break
        try:
            arr.append(int(num))
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    if arr:
        min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
        print(f"\nMenor elemento: {min_val}")
        print(f"Maior elemento: {max_val}")
    else:
        print("Nenhum número foi inserido.")
