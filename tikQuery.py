from TikTokApi import TikTokApi
import pprint

pp = pprint.PrettyPrinter(indent=4)

verifyFp = ""

api = TikTokApi.get_instance()
count = 1000
tiktoks = api.by_username("jdisjustin", count=count)

# trending = api.by_trending(count=results, custom_verifyFp=verifyFp)
printHeader = True
totalViews = 0
totalLikes = 0
totalFollowers = 0
for tiktok in tiktoks:
    if printHeader:
        printHeader = False
        totalFollowers = tiktok['authorStats']['followerCount']
        # pp.pprint(tiktoks)
        print('\n\n')
        print('      Views   Comments      Likes  Shares  Description')
        print('-----------   --------   -------- -------  ------------------------------------------------------------')

    # print(f"{tiktok['desc']}")
    print(f"{tiktok['stats']['playCount']:11,.0f} ", end='')
    print(f"{tiktok['stats']['commentCount']:10,.0f} ", end='')
    print(f"{tiktok['stats']['diggCount']:10,.0f} ", end='')
    print(f"{tiktok['stats']['shareCount']:7,.0f}  ", end='')
    descr = tiktok['desc']
    if len(descr) > 60:
        descr = descr[0:59]
    print(f"{descr}")
    totalViews = totalViews + tiktok['stats']['playCount']
    totalLikes = totalLikes + tiktok['stats']['diggCount']
    # Prints the id of the tiktok
    # print(f"author: {tiktok['author']['uniqueId']}, views: {tiktok['stats']['playCount']:10.0f}")

print('')
print(f'Total Followers: {totalFollowers:11,.0f}')
print(f'Total Likes:     {totalLikes:11,.0f}')
print(f'Total Views:     {totalViews:11,.0f}\n\n')
