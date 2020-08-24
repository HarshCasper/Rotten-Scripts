# Get sports updates

This script gives live scores for matches, team info and match info

#### Requirements

sports.py
```
$ pip install sports.py
```

---

The following sports are supported:
```
Baseball: baseball
Basketball: basketball 
Cricket,: cricket
Football: football 
Handball: handball 
Hockey: hockey 
Rugby League: rugby-league 
Rugby Union: rugby-union 
Soccer: soccer 
Tennis: tennis 
Volleyball: volleyball
```

#### How to use it?

* To get the live details of matches of a particular sport:
```
$ python script.py <sportName>
```

* To get the details of match between two teams:
```
$ python script.py <sportName> <team1> <team2>
```

* To get the details of a team:
```
$ python script.py <sportName> <teamName>
```

**Note:** This is only supported for MLB, NBA, NFL, and NHL teams