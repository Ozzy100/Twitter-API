# Twitter Data Extraction

* This code extracts data from the Twitter API and saves it to a SQL database.

##  **Requirements**
1. Python 3
2. Tweepy
3. dotenv
4. pandas
5. sqlalchemy
  
##  **Instructions**
1.  Install the required packages.
2.  Create a .env file and store your Twitter API credentials in it.
3.  Run the code.
  
##  **Output**

* The code will create a SQL database called twitter_df.db. The database will contain a table called tweet with the following columns:

* screen_name
* followers_count
* listed_count
* statuses_count

##  Example

To run the code, you can use the following command:

* python3 twitter.py

* This will extract the data for your Twitter account and save it to the twitter_df.db database. You can then query the database to view the data.
