import numpy as np
import jieba
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def draw_word_cloud(word):
    words = jieba.cut(word)
    wordstr = " ".join(words)
    sw = set(STOPWORDS)
    sw.add("ok")
    mask = np.array(Image.open('3.jpg'))
    wc = WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf', 
        background_color="white",
        mask=mask,
        max_words=500,
        max_font_size=24,
        stopwords=sw,
        scale=4,
        ).generate(wordstr)

    # 显示词云图
    plt.imshow(wc)
    plt.axis("on")
    plt.show()

    # 保存词云图
    wc.to_file('result.jpg')

if __name__ == "__main__":
    with open("cinderella.txt", "rb") as f:
        word = f.read()
        draw_word_cloud(word)