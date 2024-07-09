import re
from math import ceil


class ArticleReadTimeEngine:
    @staticmethod
    def word_count(text):
        words = re.findall(r"\w+", text)
        return len(words)

    @staticmethod
    def estimate_reading_time(
        article, words_per_minute=250, seconds_per_image=10, seconds_per_tag=2
    ):
        wcb = ArticleReadTimeEngine.word_count(article.body)
        wct = ArticleReadTimeEngine.word_count(article.title)
        wcd = ArticleReadTimeEngine.word_count(article.description)

        total_word_count = wcb + wct + wcd

        reading_time = total_word_count / words_per_minute

        if article.banner_image:
            reading_time += seconds_per_image / 60

        tag_count = article.tags.count()
        reading_time += (tag_count * seconds_per_tag) / 60

        reading_time = ceil(reading_time)

        return reading_time