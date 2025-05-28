def read_input(filename):
    f = open(filename, "r")
    n = int(f.readline())
    words = []
    for _ in range(n):
        line = f.readline()
        word = ""
        for ch in line:
            if ch != '\n' and ch != '\r':
                word += ch
        words.append(word)
    f.close()
    return words

def write_output(filename, result):
    f = open(filename, "w")
    f.write(str(result))
    f.write("\n")
    f.close()

def manual_sort_by_length(words):
    for i in range(len(words)):
        min_index = i
        for j in range(i+1, len(words)):
            if len(words[j]) < len(words[min_index]):
                min_index = j
        temp = words[i]
        words[i] = words[min_index]
        words[min_index] = temp
    return words

def longest_chain(words):
    dp = []  
    max_chain = 1

    for word in words:
        current_length = 1
        for i in range(len(word)):
            prev = ""
            for j in range(len(word)):
                if i != j:
                    prev += word[j]
            for pair in dp:
                if pair[0] == prev:
                    if pair[1] + 1 > current_length:
                        current_length = pair[1] + 1
        dp.append((word, current_length))
        if current_length > max_chain:
            max_chain = current_length

    return max_chain

if __name__ == "__main__":
    words = read_input("wchain.in")
    words = manual_sort_by_length(words)
    result = longest_chain(words)
    write_output("wchain.out", result)
