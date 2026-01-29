def word_order(words):
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    return count
