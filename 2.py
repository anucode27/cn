def bitStuffing(N, arr):
    brr = [0 for _ in range(30)]
    j = 0
    i = 0

    while i < N:
        if arr[i] == 1:
            count = 1
            brr[j] = arr[i]
            k = i + 1

            while k < N and arr[k] == 1 and count < 5:
                j += 1
                brr[j] = arr[k]
                count += 1
                k += 1

            if count == 5:
                j += 1
                brr[j] = 0

            i = k
        else:
            brr[j] = arr[i]
            i += 1

        j += 1

    for i in range(j):
        print(brr[i], end="")


if __name__ == "__main__":
    N = 6
    arr = [1, 1, 1, 1, 1, 1]

    bitStuffing(N, arr)
