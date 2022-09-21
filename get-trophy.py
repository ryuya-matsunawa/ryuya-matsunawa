import requests

for column in (4, 8):
    for theme in ('onedark', 'flat'):
        if column == 4:
            r = requests.get(f"https://github-profile-trophy.vercel.app/?username=ryuya-matsunawa&theme={theme}&column={column}&no-frame=true&margin-w=15&margin-h=15")
        else:
            r = requests.get(f"https://github-profile-trophy.vercel.app/?username=ryuya-matsunawa&theme={theme}&column={column}&no-frame=true&margin-w=15")
        
        file = open(f"./profile-trophy-output/trophy-{theme}-column-{column}.svg", mode="w")
        file.write(r.text)
        file.close()
