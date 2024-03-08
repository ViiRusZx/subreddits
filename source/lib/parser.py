from datetime import datetime, timedelta

from source.lib.config import reddit, start_time


class Parser():

    def __init__(self, reddit = reddit, start_time = start_time) -> None:

        self.reddit = reddit
        self.start_time = start_time

    def _top_posts_autors(self) -> dict:
        authors_dict = {}
        top_posts = reddit.subreddit("Python").new(limit = None)
        recent_posts = [post for post in top_posts if
                        datetime.utcfromtimestamp(post.created_utc) > start_time]
        for post in recent_posts:
            author = str(post.author)
            if author in authors_dict:
                authors_dict[author] += 1
            else:
                authors_dict[author] = 1

        sorted_authors = dict(
                sorted(authors_dict.items(), key = lambda item: item[1],
                       reverse = True))

        return sorted_authors

    def _top_commen_authors(self) -> dict:
        subreddit = reddit.subreddit("Python")
        start_date = datetime.now() - timedelta(days = 3)
        comment_dict = {}
        for post in subreddit.new():
            post_date = datetime.utcfromtimestamp(post.created_utc)
            post.comments.replace_more(limit = None)
            if post_date >= start_date:
                for comment in post.comments.list():
                    author_name = str(comment.author)
                    if author_name in comment_dict:
                        comment_dict[author_name] += 1
                    else:
                        comment_dict[author_name] = 1

        sorted_comments = dict(
                sorted(comment_dict.items(), key = lambda item: item[1],
                       reverse = True))

        return sorted_comments

    def print_top_authors_in_posts(self) -> None:
        for k, v in self._top_posts_autors().items():
            print(f"Автор: {k}, количество постов: {v}")

    def print_top_authors_in_comments(self) -> None:
        for k, v in self._top_commen_authors().items():
            print(f"Автор: {k}, количество комментариев: {v}")
