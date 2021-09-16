#!/usr/bin/env python
# -*- coding: utf-8  -*-
#测试训练好的模型

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')# 忽略警告
from gensim.models import KeyedVectors

if __name__ == '__main__':
    fdir = '/data02/gob/model_hub/wiki_zh_char_vec/'
    # model = KeyedVectors.load_word2vec_format(fdir+'wiki.zh.text.vector', binary=False, unicode_errors='ignore')
    model = KeyedVectors.load_word2vec_format(fdir+'wiki.zh.text.char.vector', binary=False)
    word = model.most_similar(u"丑")
    print('==============================')
    print('求丑的相似词：')
    for t in word:
        print(t[0],t[1])
    print('==============================')
    print('==============================')
    word = model.most_similar(u"龚")
    print('求龚的相似词：')
    for t in word:
        print(t[0],t[1])
    print('==============================')
    print('==============================')
    word = model.most_similar(u"美")
    print('求美的相似词：')
    for t in word:
        print(t[0],t[1])
    print('==============================')
    """
    print('==============================')
    print('皇上+国王=皇后+？')
    word = model.most_similar(positive=[u'皇上',u'国王'],negative=[u'皇后'])
    for t in word:
        print(t[0],t[1])
    print('==============================')
    print('==============================')
    print('找出“太后 妃子 贵人 贵妃 才人”不匹配的词语')
    print(model.doesnt_match(u'太后 妃子 贵人 贵妃 才人'.split()))
    print('==============================')
    print('==============================')
    print('找出“书籍和书本"的相似度')
    print(model.similarity(u'书籍',u'书本'))
    print('找出"逛街和书本"的相似度')
    print(model.similarity(u'逛街',u'书本'))
    """
