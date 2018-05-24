
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image
d = path.dirname(__file__)


text = open(path.join(d, 'constitution.txt')).read()


f = open(path.join(d, 'constitution.txt')).read()
wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(f)
#生成图片
# wordcloud.to_file('test.png')


#图片做背景

#读入背景图片
abel_mask = np.array(Image.open("alice_mask.png"))

#读取要生成词云的文件
text_from_file_with_apath = open('mysql.txt').read()

#通过jieba分词进行分词并通过空格分隔
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
#my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
my_wordcloud = WordCloud(
            background_color='white',    # 设置背景颜色
            # mask = abel_mask,        # 设置背景图片
            max_words = 1000,            # 设置最大现实的字数
            stopwords = STOPWORDS,        # 设置停用词
            width=1000,
            height=1000,
            font_path='/Users/lovesosoi/Documents/font_style/syst.otf',
            max_font_size = 250,            # 设置字体最大值
            random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                scale=.5
                ).generate(wl_space_split)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(abel_mask)
#my_wordcloud.recolor(color_func=image_colors)

# # 以下代码显示图片
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()
my_wordcloud.to_file('mysql.png')