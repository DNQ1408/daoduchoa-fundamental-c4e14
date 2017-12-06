from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
db_c4e = client.get_default_database()
# post = db_c4e ['posts']
# new_post = {
#     'title': "My belief",
#     'author': "DNQ",
#     'content': '''Just a young gun with a quick fuse
# I was uptight, wanna let loose
# I was dreaming of bigger things
# And wanna leave my old life behind
# Not a yes-sir, not a follower
# Fit the box, fit the mold
# Have a seat in the foyer, take a number
# I was lightning before the thunder'''
#
# }
# post.insert_one(new_post)


customers = db_c4e['customers'].find()
count_ads = 0
count_wom = 0
count_events = 0

for customer in customers:
    if customer['ref'] == 'ads':
        count_ads += 1
    elif customer['ref'] == 'wom':
        count_wom += 1
    elif customer['ref'] == 'events':
        count_events += 1
print('''Reference:
        {0} Advertisement
        {1} Word of mouth
        {2} Events'''.format(count_ads,count_wom,count_events))

from matplotlib import pyplot

labels = ['Advertisement', 'Word of mouth', 'Event']
colors = ['#49aaff', '#fc626f', '#fcff84']
data = [count_ads, count_wom, count_events]

pyplot.pie(data, labels = labels, colors = colors,autopct = '%1.2f%%')
pyplot.axis('equal')
pyplot.show()
