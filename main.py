import database
import facebook
import notion


cur = database.get_cursor()

# LOAD FROM NOTION
# download People data, parse out some columns, put into sqlite (some acquaintances will have been promoted)
people = notion.list_people()

# upsert_notion_people to sqlite
database.upsert_notion_people(people)

# FACEBOOK MESSENGER & RECENT FRIENDS
# open FB and download relevant data to ~/Downloads (use selenium)
facebook.download_backup()

# parse messenger events
# parse recent friends


# TWITTER
# recent twitter DMs / interactions
# include people on various lists
# https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/get-event
# CRM should have column for handles

# CONTACT ENRICHMENT
# anyone that hasn't had this done, do it

# DUMP TO NOTION
# i had something along these lines already

# DUMP TO OMNI
