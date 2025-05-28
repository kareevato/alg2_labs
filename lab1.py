def selection_sort(arr, a="a"):
    n = len(arr)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if (a == "a" and arr[j] < arr[target_idx]) or (a == "d" and arr[j] > arr[target_idx]):
                target_idx = j
        arr[i], arr[target_idx] = arr[target_idx], arr[i]
    return arr


def find_kth_element(arr, pos, a="a"):
    if not arr or pos < 1 or pos > len(arr):
        raise ValueError("Invalid input: pos must be between 1 and the length of the array.")

    sorted_arr = selection_sort(arr.copy(), a)
    kth_element = sorted_arr[pos - 1]
    index = arr.index(kth_element)

    return kth_element, index


def find_kth_both(arr, k, m):
    result_asc = find_kth_element(arr, k, "a")
    result_desc = find_kth_element(arr, m, "d")

    return {
        "asc": result_asc,
        "desc": result_desc
    }


if __name__ == "__main__":
    array = [15, 7, 22, 9, 30, 18]
    k = 2
    m = 3
    results = find_kth_both(array, k, m)
    print(f"{k}-й найменший елемент: {results['asc'][0]}, його позиція: {results['asc'][1]}")
    print(f"{m}-й найбільший елемент: {results['desc'][0]}, його позиція: {results['desc'][1]}")
