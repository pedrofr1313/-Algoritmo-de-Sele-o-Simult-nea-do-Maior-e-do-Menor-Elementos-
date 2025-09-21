def maxmin_select(arr, left, right):
    # Caso base: apenas um elemento
    if left == right:
        return arr[left], arr[left]
    
    # Caso base: dois elementos
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    # Dividir o problema
    mid = (left + right) // 2
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)

    # Combinar os resultados
    return min(min1, min2), max(max1, max2)


if __name__ == "__main__":
    lista = [6, 2, 9, 4, 1, 5, 8, 3, 6]
    menor, maior = maxmin_select(lista, 0, len(lista) - 1)
    print(f"Lista: {lista}")
    print(f"Menor elemento: {menor}")
    print(f"Maior elemento: {maior}")
