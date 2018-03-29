# Facebbok_posts_Word_Count


## Word Cloud Package 
```ruby
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)
# Read the whole text.
text = open(path.join(d, 'ClubJ2I_facebook_statuses.txt')).read()
# Generate a word cloud image
wordcloud = WordCloud().generate(text)
```


## Final Output 
![alt text](https://github.com/Rebaiahmed/Facebbok_posts_Word_Count/blob/master/screen.png)
