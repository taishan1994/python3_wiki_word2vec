from pypinyin import pinyin, lazy_pinyin, Style

style = Style.TONE3
line = lazy_pinyin('我爱北京天安门 娃哈哈 style 你好123', style=style)
tmp = []
for i in line:
    if not i.isalpha() and not i.isdigit():
        tmp.append(i)
print(tmp)
