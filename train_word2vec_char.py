#!/usr/bin/env python
# -*- coding: utf-8  -*-
#使用gensim word2vec训练脚本获取词向量

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')# 忽略警告

import logging
import os.path
import sys
import multiprocessing
import os

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


if __name__ == '__main__':

    #print open('/Users/sy/Desktop/pyRoot/wiki_zh_vec/cmd.txt').readlines()
    #sys.exit()
    
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # inp为输入语料, outp1 为输出模型, outp2为原始c版本word2vec的vector格式的模型
    fdir = '/data02/gob/model_hub/wiki_zh_char_vec/'
    if not os.path.exists(fdir):
        os.mkdir(fdir)
    inp = 'wiki.zh.simp.seg.char.txt'
    outp1 = fdir + 'wiki.zh.text.char.model'
    outp2 = fdir + 'wiki.zh.text.char.vector'

    # 训练skip-gram模型
    model = Word2Vec(LineSentence(inp), vector_size=100, window=5, min_count=5,
                     workers=4, epochs=10)

    # 保存模型
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)

