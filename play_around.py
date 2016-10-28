# team = 'New England Patriots'
# win_pct = 65

# print('%s %d' % (team, win_pct))






def check_team(team):


    if team == ('Patriots' and 'New England Patriots'):
        return 'Good'
    else:
        return 'Bad'


team = input('Enter your favorite team: ').lower()
print(check_team(team))
