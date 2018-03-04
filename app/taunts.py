import random

def taunts(health):
	if health == 100:
		return('Scotty, we\'ve got full power!')
	elif health <= 10:
		return('Scotty, we need more power!')
	else:
		taunt_list = ['__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___', '¯¯̿̿¯̿̿'̿̿̿̿̿̿̿'̿̿'̿̿̿̿̿'̿̿̿)͇̿̿)̿̿̿̿ \'̿̿̿̿̿̿\̵͇̿̿\=(•̪̀●́)=o/̵͇̿̿/\'̿̿ ̿ ̿̿', 'ô¿ô', '♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪', 'd[ o_0 ]b', 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>', ' ¦̵̱ ̵̱ ̵̱ ̵̱ ̵̱(̢ ̡͇̅└͇̅┘͇̅ (▤8כ−◦', 'good meme']
		rand = random.randrange(0,len(taunt_list))
		return(taunt_list[rand])