The Twitter Public Streaming API was used to collect data using keyword tracking
(the tweets containing certain predetermined keywords are collected).
The data was collected between June and November 2015.  From the data obtained from Twitter,
certain features have been chosen and provided in a csv file format.  The data has been
split for each keyword.  

6 keywords that were used for tracking (and hence the appropriate filenames) are:
codeine (431625 rows)
percocet (75215 rows)
vicodin (28610 rows)
oxycontin (27734 rows)
oxycodone (18061 rows)
hydrocodone (9981 rows)

Each csv file is has 10 columns.  The column headers are:

1.  in_reply_to_status_id
2.  retweet_count
3.  favorite_count
4.  friends_count
5.  followers_count
6.  hashtags_list
7.  user_location
8.  user_timezone
9.  created_at
10. text

Details about each column:

The first 5 features are numerical features, and will not have any missing values.  

1.  in_reply_to_status_id [N]
Indicates whether or not a tweet is a reply to another tweet.  It is a 0/1 binary feature.

2.  retweet_count [N]
Indicates the number of times a tweet has been retweeted.  If a tweet is a retweet, it indicates the number of times
the original tweet has been retweeted.

3.  favorite_count [N]
Indicates the number of times a tweet has been favorited.

4.  friends_count [N]
Indicates the number of "friends" of the user posting the tweet.  Friends is the number of users
following the user.

5.  followers_count [N]
Indicates the number of users "following" the user.  

--------------------------------------------------------------------------------------

The last five features are non-numerical, and will have missing values.

6.  hashtags_list
This specifies the list of hashtags present in the tweet.  The list of hashtags are separated by '::'.  
NOTE:  The hashtags may have been modified to remove any commas and whitespaces to bring it to CSV format.
This feature is empty when there are no hashtags in the tweet.

7.  user_location
This corresponds to the 'location' key of the 'user' object.  This is free text; the user will free to specify
any location of choice.  This feature was also modified to remove any commas and whitespaces to bring it to
a CSV format.  This feature is empty when the user has not specified any location.

8.  user_timestamp
This corresponds to the time zone that the user declares themselves with.  Nullable.

9.  created_at
UTC timestamp of creation of the tweet.  Non-nullable.  It is for the following format:
WWW MMM DD HH:MM:SS +0000 2015
where WWW is the weekday (e.g Mon, Tue), MMM is the month (e.g Jan, Jun) and DD is the 2-digit date.

10. text
text of the tweet
-----------------------------------------------------------------------------------------
