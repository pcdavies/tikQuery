from TikTokApi import TikTokApi
import pprint

pp = pprint.PrettyPrinter(indent=4)

verifyFp = ""

api = TikTokApi.get_instance()
count = 1000
tiktoks = api.by_username("jdisjustin", count=count, custom_verifyFp=verifyFp)

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
        print('      Views   Comments    %        Likes     %   Shares      %  Description')
        print('-----------   -------- -----  ---------- -----   ------   ----  ------------------------------------------------------------')

    playCount = tiktok['stats']['playCount']
    commentCount = tiktok['stats']['commentCount']
    diggCount = tiktok['stats']['diggCount']
    shareCount = tiktok['stats']['shareCount']
    descr = tiktok['desc']

    percentComments = commentCount / playCount * 100.0
    percentDiggs = diggCount / playCount * 100.0
    percentShares = shareCount / playCount * 100.0

    # print(f"{tiktok['desc']}")
    print(f'{playCount:11,.0f} ', end='')
    print(f"{commentCount:10,.0f} ", end='')
    print(f"{percentComments:5.2f} ", end=' ')
    print(f"{diggCount:10,.0f} ", end='')
    print(f"{percentDiggs:5.1f} ", end=' ')
    print(f"{shareCount:7,.0f}  ", end='')
    print(f"{percentShares:5.2f} ", end=' ')
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
