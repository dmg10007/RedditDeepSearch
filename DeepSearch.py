pip install praw

import praw

reddit = praw.Reddit(client_id='rjzW-PmPp04b6g',
                     client_secret='...',
                     password='...',
                     user_agent='Deep Search by /u/dblock1111',
                     username='dblock1111')

print("Welcome to Reddit Deep Search!")
print("What can we help you find today?")

post_type = input("Submission, Comment, Reply?")

date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)

sorted_by = input("Top, Newest, Oldest, Controversial?")
