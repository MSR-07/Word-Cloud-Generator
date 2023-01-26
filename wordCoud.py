import numpy as np
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt


text = """
Meet 'Muhammad Saif ur Rehman', the code wizard, software sorcerer, and all-around tech-savvy genius! With his mad skills in programming and problem-solving, this software engineer can turn any project into a work of art. When he's not busy making computers dance to his tune, he's probably playing video games or eating pizza.
"""

# Analyze and transform a mask picture. It should have a black item on a white (not translucent) backdrop.
mask_img = np.array(Image.open(".\Assets\Img\h2.png"))

wordcloud = WordCloud(background_color="#ffff",
                      max_words=400, mask=mask_img).generate(text)

# store to file
wordcloud.to_file("Output.jpg")

# Show the image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
