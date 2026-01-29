def merge_the_tools(string, k):
    result = []

    for i in range(0, len(string), k):
        substring = string[i:i+k]
        res = ""
        for ch in substring:
            if ch not in res:
                res += ch
        result.append(res)

    return result
