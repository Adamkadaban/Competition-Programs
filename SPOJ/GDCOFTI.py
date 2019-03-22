def find_gcd(arr):
    if len(arr) <= 1:
        return arr
    else:
        for i in range(len(arr)-1):
            a = arr[i]
            b = arr[i+1]
            while b:
                a, b = b, a%b
            arr[i+1] = a
        return a
print(find_gcd([int(input()), int(input()), int(input())]))