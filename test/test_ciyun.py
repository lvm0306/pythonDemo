
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image

from util.CiyunUtil import CiyunHelper,CiyunHelperBg

if __name__=='__main__':
    # cu=CiyunHelper('mysql.txt','lovesosoi.png',1000,1000,200)
    # cu.createImage()
    chb=CiyunHelperBg('mysql.txt','lovesosoi.png',1000,1000,200,'alice_mask.png')
    chb.createImage()
