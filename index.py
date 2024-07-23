def find_page_and_line(K, N):
    df = (N - 1) // K + 1
    fh = (N - 1) % K + 1
    return df, fh
k, n = map(int, input().split())
k1, n1 = find_page_and_line(k, n)
print(k1, n1)