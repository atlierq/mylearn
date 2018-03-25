import sys
import re
WORD_RE = re.compile(r'\w+')
index = {}
with open('a.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            # print(match.span())
            # print(match.start())
            word = match.group()
            # print(word)
            column_no = match.start()+1
            location = (line_no, column_no)
# # 这其实是一种很不好的实现，这样写只是为了证明论点
            occurrences = index.get(word, [])
            # print(occurrences)
            occurrences.append(location)
            # print(occurrences)
            index[word] = occurrences
            print(index)
# 以字母顺序打印出结果
# for word in sorted(index, key=str.upper):
#     print(word, index[word])