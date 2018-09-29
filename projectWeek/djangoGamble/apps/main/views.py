from django.shortcuts import render

def index(request):
    data = [
        {"team_names": ["Minnesota Twins", "Chicago Cubs", "Los Angeles Angels", "Baltimore Orioles", "Boston Red Sox", "New York Yankees", "Washington Nationals", "Philadelphia Phillies", "Detroit Tigers", "Toronto Blue Jays", "Milwaukee Brewers", "Cincinnati Reds", "New York Mets", "Miami Marlins", "Houston Astros", "Tampa Bay Rays", "Chicago White Sox", "Texas Rangers", "Atlanta Braves", "St. Louis Cardinals", "San Francisco Giants", "Arizona Diamondbacks", "Cleveland Indians", "Oakland Athletics", "Kansas City Royals", "Seattle Mariners", "Colorado Rockies", "Los Angeles Dodgers", "Pittsburgh Pirates", "San Diego Padres"], "images": ["http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/min.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/chc.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/laa.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/bal.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/bos.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/nyy.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/wsh.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/phi.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/det.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tor.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/mil.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/cin.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/nym.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/mia.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/hou.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tb.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/chw.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tex.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/atl.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/stl.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sf.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/ari.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/cle.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/oak.png&h=50", "http://a.espncdn.com/redesign/assets/img/logos/networks/channel_logo_espnplus_2x.png", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/kc.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sea.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/col.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/lad.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/pit.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sd.png&h=50"], "dates": ["2018-06-29T21:05Z", "2018-06-29T23:05Z", "2018-06-29T23:05Z", "2018-06-29T23:05Z", "2018-06-29T23:07Z", "2018-06-29T23:10Z", "2018-06-29T23:10Z", "2018-06-29T23:10Z", "2018-06-30T00:05Z", "2018-06-30T00:15Z", "2018-06-30T01:40Z", "2018-06-30T02:05Z", "2018-06-30T02:10Z", "2018-06-30T02:10Z", "2018-06-30T02:10Z"]},
        {"team_names": ["Detroit Tigers", "Toronto Blue Jays", "Minnesota Twins", "Chicago Cubs", "Los Angeles Angels", "Baltimore Orioles", "Cleveland Indians", "Oakland Athletics", "Milwaukee Brewers", "Cincinnati Reds", "New York Mets", "Miami Marlins", "Houston Astros", "Tampa Bay Rays", "Washington Nationals", "Philadelphia Phillies", "Boston Red Sox", "New York Yankees", "Colorado Rockies", "Los Angeles Dodgers", "Atlanta Braves", "St. Louis Cardinals", "Chicago White Sox", "Texas Rangers", "Kansas City Royals", "Seattle Mariners", "Pittsburgh Pirates", "San Diego Padres", "San Francisco Giants", "Arizona Diamondbacks"], "images": ["http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/det.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tor.png&h=50", "http://a.espncdn.com/redesign/assets/img/logos/networks/channel_logo_espnplus_2x.png", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/min.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/chc.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/laa.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/bal.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/cle.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/oak.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/mil.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/cin.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/nym.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/mia.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/hou.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tb.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/wsh.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/phi.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/bos.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/nyy.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/col.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/lad.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/atl.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/stl.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/chw.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tex.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/kc.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sea.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/pit.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sd.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sf.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/ari.png&h=50"], "dates": ["2018-06-30T17:07Z", "2018-06-30T18:20Z", "2018-06-30T20:05Z", "2018-06-30T20:05Z", "2018-06-30T20:10Z", "2018-06-30T20:10Z", "2018-06-30T20:10Z", "2018-06-30T22:05Z", "2018-06-30T23:15Z", "2018-06-30T23:15Z", "2018-06-30T23:15Z", "2018-07-01T01:05Z", "2018-07-01T02:10Z", "2018-07-01T02:10Z", "2018-07-01T02:10Z"]},
        {"team_names": ["Los Angeles Angels", "Baltimore Orioles", "Detroit Tigers", "Toronto Blue Jays", "Milwaukee Brewers", "Cincinnati Reds", "New York Mets", "Miami Marlins", "Houston Astros", "Tampa Bay Rays", "Washington Nationals", "Philadelphia Phillies", "Atlanta Braves", "St. Louis Cardinals", "Minnesota Twins", "Chicago Cubs", "Chicago White Sox", "Texas Rangers", "Cleveland Indians", "Oakland Athletics", "Kansas City Royals", "Seattle Mariners", "Colorado Rockies", "Los Angeles Dodgers", "Pittsburgh Pirates", "San Diego Padres", "San Francisco Giants", "Arizona Diamondbacks", "Boston Red Sox", "New York Yankees"], "images": ["http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/laa.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/bal.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/det.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tor.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/mil.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/cin.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/nym.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/mia.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/hou.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tb.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/wsh.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/phi.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/atl.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/stl.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/min.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/chc.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/chw.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/tex.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/cle.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/oak.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/kc.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sea.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/col.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/lad.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/pit.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sd.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/sf.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/ari.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/bos.png&h=50", "http://a.espncdn.com/combiner/i?img=/i/teamlogos/mlb/500/scoreboard/nyy.png&h=50", "http://a.espncdn.com/redesign/assets/img/logos/networks/espn-red@2x.png", "http://a.espncdn.com/redesign/assets/img/logos/networks/logo-watchespn@2x.png"], "dates": ["2018-07-01T17:05Z", "2018-07-01T17:07Z", "2018-07-01T17:10Z", "2018-07-01T17:10Z", "2018-07-01T17:10Z", "2018-07-01T17:35Z", "2018-07-01T18:15Z", "2018-07-01T18:20Z", "2018-07-01T19:05Z", "2018-07-01T20:05Z", "2018-07-01T20:10Z", "2018-07-01T20:10Z", "2018-07-01T20:10Z", "2018-07-01T20:10Z", "2018-07-02T00:00Z"]}
    ]
    delete = []

    for i in data:
        all_images = []
        for image in i["images"]:    
            if "2x.png" not in image:
                all_images.append(image)
        i['images'] = all_images

    gmt = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    current = ["5","6","7","8","9","10","11","12","1","2","3","4","5","6","7","8","9","10","11","12","1","2","3","4"]
    game_day = []
    game = {}
    time = []
    count=0
    num=0
    for date in data:
        for i in date['dates']:
            if i == "LIVE":
                time.append("Live")
            if i != "LIVE":
                i = i.split("T")
                hour = i[1][0]+i[1][1]
                for t in range(len(gmt)):
                    if gmt[t]==hour:
                        hour = current[t]
                        if t >= 19 or t <= 6:
                            j = current[t] + ":" + i[1][3] + i[1][4] + "PM"
                        else:
                            j = current[t] + ":" + i[1][3] + i[1][4] + "AM"
                        time.append(j)
        date['dates'] = time
        time = [] 
    for obj in data:
        for i in range(len(obj['team_names'])):
            if(i%2!=0):
                game[count+1] = {"away":obj['team_names'][i-1],"home":obj['team_names'][i],"away_img":obj['images'][i-1],"home_img":obj['images'][i],"date":obj['dates'][num]}
                game_day.append(game[count+1])
                count +=1
                num+=1
        num=0
    # print(game_day)
    context = {"data":game_day}
    return render(request, 'main/index.html', context)