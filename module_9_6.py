def all_variants(text):
    for len_s in range(len(text)):
        for index in range(len(text)-len_s):
            yield text[index:index+len_s+1]


a = all_variants("abc")
for i in a:
    print(i)
