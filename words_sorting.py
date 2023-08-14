def words_sorting(*args):
    words_dict = {}

    for word in args:
        count = 0
        for ch in word:
            count += ord(ch)
        words_dict[word] = count


    all_values_sum = sum(words_dict.values())

    if all_values_sum % 2 == 0:
        return "\n".join([f"{k} - {v}" for k, v in sorted(words_dict.items(), key=lambda x: x[0])])
    else:
        return "\n".join([f"{k} - {v}" for k, v in sorted(words_dict.items(), key=lambda x: -x[1])])

