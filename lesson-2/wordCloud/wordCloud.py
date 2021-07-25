from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

# 读取文本内容
current_directory = Path.cwd()
text = Path.open(current_directory/"4.txt", encoding='utf-8').read()

### 参数配置 ###
# 增加词云轮廓模板
cinderella_mask = np.array(Image.open(current_directory/"4.png"))

# 创建词云实例对象，并配置参数（stopwords禁用词参数，mask设置轮廓模板）
wordcloud = WordCloud(background_color = 'black', mask = cinderella_mask, 
                      mix_words=40, max_words = 1000, width = 600, height = 500, prefer_horizontal = 1.0, stopwords = STOPWORDS, min_font_size=4)

# 加载文本内容到词云对象中。
wordcloud.generate(text)
# 用ImageColorGenerator类方法基于图像模板生成颜色
#image_colors = ImageColorGenerator(cinderella_mask)
ImageColorGenerator(cinderella_mask)

plt.figure(figsize = (32, 16))

# 添加左侧 词云图 子图图像区域。
plt.subplot(121)

# 以常规2D光栅的方式显示图像，其中interpolation参数代表以哪种模糊程度显示。
plt.imshow(wordcloud.recolor(color_func = image_colors), interpolation = 'bilinear')

# 关闭matplotlib图像的轴线和标签。
    plt.axis('off')

# 添加右侧 原始对比图 子图图像区域。
    plt.subplot(122)
plt.imshow(cinderella_mask, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis('off')

# 将图像以定义的图像文件名输出。
plt.savefig('Cinderella_WordCloud_pic.png')
plt.show()