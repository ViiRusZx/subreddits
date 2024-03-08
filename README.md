# subreddits

для работы вам понадобится в папке **lib** создать файл **config.py**


в **config.py** вам необходимо импортировать: 
**from datetime import timedelta, datetime**
**import praw**


reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_id",
    user_agent="your_user_agent"
    )
замените "your_client_id", "your_client_id", "your_user_agent" на ваши данные из полученного API
