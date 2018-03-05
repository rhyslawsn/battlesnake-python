import random

def taunts(health):
	if health == 100:
		return('Scotty, we\'ve got full power!')
	elif health <= 10:
		return('Scotty, we need more power!')
	else:
		taunt_list = ['good meme']
		rand = random.randrange(0,len(taunt_list))
		return(taunt_list[rand])