

from textblob import TextBlob
from twython import Twython
APP_KEY = "I1WJ9lPZKo6bOPLZA4KDgA";
APP_SECRET = "27IfEiv2yK8eDVmeiDUN0peSqS2YKpsnirNN0xx32Lo";

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
print 'Write what you want to search!'
search = twitter.cursor(twitter.search,q='obama',count=10)
totalSent = 0
i = 0
for result in search:
	if i > 2:
		break;
	totalSent += TextBlob(result['text']).sentiment.polarity
	i += 1


print str(totalSent/i)