def naive_substring_search(haystack: str, needle: str) -> tuple[int, int]:
    comparisons = 0
    last_index = -1
    h_len = len(haystack)
    n_len = len(needle)

    if n_len == 0 or h_len == 0 or n_len > h_len:
        return -1, 0

    for i in range(h_len - n_len + 1):
        match = True
        for j in range(n_len):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            last_index = i + n_len - 1

    return last_index, comparisons


if __name__ == "__main__":
    haystack = input("Введіть текст (haystack): ")
    needle = input("Введіть підрядок для пошуку (needle): ")

    index, comparisons = naive_substring_search(haystack, needle)

    print(f"\nКінцевий індекс останнього входження: {index}")
    print(f"Кількість порівнянь символів: {comparisons}")
