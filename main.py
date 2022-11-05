from pymongo import MongoClient
import tweepy
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-bearer", "--bearer", required=True)
    args = parser.parse_args()

    rule2 = '\"the wall\" OR \"fuck ice\" OR undocumented OR illegals OR \"an illegal\" OR \"muslim ban\" OR \"travel ban\" OR refugee OR asylum OR #wherearethechildren OR \"child cage\" OR \"children cage\" OR #wall OR daca OR #dreamer OR \"sanctuary city\" OR \"sanctuary cities\" OR \"baby cage\" OR \"babies cage\" OR \"abolish ice\" OR \"ice raid\" OR #abolishice OR #muslimban OR #nobannohate OR #refugeeswelcome OR #refugeeswelcomehere OR ms-13 OR \"build the wall\" OR #buildthewall OR ms- 13 OR \"ms 13\" OR deport OR citizenship OR birthright OR \"illegal alien\" OR ms13 lang:en -is:retweet'

    rule1 = 'secureourborders OR #familiesbelongtogether OR #closethecamps OR #defenddaca OR #nocamps OR #noban OR #savedaca OR #immigrationreform OR #uslatino OR #openborders OR \"open border\" OR \"kid cage\" OR \"kids cage\" OR USCIS OR #proimmigration OR \"farm worker\" OR \"farm workers\" OR farmworker OR #farmworkerjustice OR #immigrationpolicy OR migrant OR amnesty OR #noamnesty OR #imalreadyhome OR #proopenborders OR #immigrantnation OR #nohumanisillegal OR #welcomeimmigrants OR \"no human is illegal\" OR #MSW52170 OR #immigrantsmatter OR #immigrantrights OR \"learn to speak English\" OR \"steal jobs\" OR \"job stealing\" OR \"mexican border\" OR \"mexico pay\" OR visa OR \"chain migration\" OR \"dream act\" OR \"merit based\" OR citizen OR foreigner OR \"foreign national\" OR \"trump wall\" OR \"mexico policy\" OR \"foreign worker\" OR \"human trafficking\"  OR xenophobe OR xenophobia OR schengen OR \"british national\" OR #BNO OR \"free movement\" lang:en -is:retweet'

    database = "fresh_mongo_immigration"
    collection = "immigration_collection"

    class IDPrinter(tweepy.StreamingClient):

             def on_tweet(self, tweet):
                 client = MongoClient()
                 self.db = client[database][collection]
                 print(tweet.id)
                 if not tweet.retweeted and 'RT @' not in tweet.text:
                    self.db.insert(tweet._json)

    streaming_client = IDPrinter(args.bearer)
    streaming_client.add_rules(tweepy.StreamRule(rule1))
    streaming_client.add_rules(tweepy.StreamRule(rule2))

    streaming_client.filter()

