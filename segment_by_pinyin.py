#!/usr/bin/env python
# -*- coding: utf-8  -*-
#逐行读取文件数据进行jieba分词
from pypinyin import pinyin, lazy_pinyin, Style
import codecs,sys


if __name__ == '__main__':
    f = codecs.open('wiki.zh.simp.txt', 'r', encoding='utf8')
    target = codecs.open('wiki.zh.simp.seg.pinyin.txt', 'w', encoding='utf8')
    print('open files.')

    lineNum = 1
    line = f.readline()
    style = Style.TONE3
    while line:
        print('---processing ',lineNum,' article---')
        line = lazy_pinyin(line, style=style)
        tmp = []
        for i in line:
            if not ' ' in i: # 去除掉一连串英文，一般都包含空格
                tmp.append(i)
        line_seg = " ".join(tmp)
        target.writelines(line_seg)
        lineNum = lineNum + 1
        line = f.readline()

    print('well done.')
    f.close()
    target.close()
