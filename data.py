import pandas as pd
import praw


def posts(sub_red_lst="Jobs", limit=2000, time_filter="all"):
    reddit = praw.Reddit(client_id="oczvDk-x5EqMnlbAuVz2dg", client_secret="oj5gpwxhDriQe_kCTRDwznSbCvrjuw",
                         redirect_uri="http://localhost:8080", user_agent="Poliscimania")

    data = reddit.subreddit(sub_red_lst).top(time_filter="all", limit=1000)

    post_data = []

    for p in data:
        post_data.append({"ID": p.id,
                          "Subreddit": p.subreddit,
                          "Title": p.title,
                          "Upvote": p.upvote_ratio,
                          "Score": p.score,
                          "Comments": p.comments,
                          "Edited": p.edited,
                          "URL": p.url,
                          "Flair Text": p.link_flair_text,
                          "Nums of Comment": p.num_comments})

    return pd.DataFrame(post_data)


# %%
post_data = posts(sub_red_lst="datascience+cscareerquestions", limit=2000, time_filter="all")
# post_data.to_csv("SUBREDDIT.csv", header=True, index=False)
post_data
# %%

reddit = praw.Reddit(client_id="oczvDk-x5EqMnlbAuVz2dg", client_secret="oj5gpwxhDriQe_kCTRDwznSbCvrjuw",
                         redirect_uri="http://localhost:8080", user_agent="Poliscimania")
comments_lst = []

for post in post_data["ID"]:
    sub = reddit.submission(post)

    sub.comments.replace_more(limit=None)
    for c in sub.comments.list():
        comments_lst.append({"ID": post, "Comments": c.body})

comments_data = pd.Dataframe(comments_lst)
comments_data.to_csv("COMMENTS_DATA.csv", header=True, index=False)
comments_data
