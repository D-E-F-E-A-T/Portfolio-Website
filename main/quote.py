import praw
def quote():
    reddit = praw.Reddit(client_id = 'AW7uCde_gwkGeg',
                     client_secret = 'ymlEQKiKR339IPal-cM6nk4nyZQ',
                     username = 'prawAndDjango',
                     password = 'QQbdTJHPHT22',
                     user_agent = 'praw')

    subreddit = reddit.subreddit('quotes')

    hot_python = subreddit.hot(limit = 7)

    submission_list = []

    for submission in hot_python:
            if not submission.stickied:
                submission_list.append(submission.title)

    return submission_list
