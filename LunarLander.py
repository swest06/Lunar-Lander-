'''Sean West swest06.
   Text based lunar lander game.'''
   
def fuel_use1(fuel):
	while fuel > 0:
		f_use = float(input("How much fuel do you want to use?: "))
		
		if f_use < 0:
			print("Cannot use negative values!")
			print("No fuel burned")
			return 0
		elif fuel - f_use < 0:
			print("You only have " + str(fuel) + " litres of fuel.")
			print("All remaining fuel will be burned")
			return fuel
			break
		else:
			return f_use
			break
	if fuel <= 0:
		print("OUT OF FUEL")
		return 0


def velocity_up(f_use):
	return f_use * 0.15
   

def velocity_down(veloc_d, veloc_u):
	veloc_d = (veloc_d + 1.16) - veloc_u
	return veloc_d
	
	
def altitude_1(alti, veloc_d):
	alti = alti - veloc_d
	return alti
	
	
def crater_1(alti):
    a = alti 
    crater = a - a*2
    return crater
	
	
def game_ll(alti, veloc_u, veloc_d, fuel):
	# Welcome screen	
	print("")
	print("Welcome to Lunar Lander")
	print("Your goal is to land the rocket safely on the moon's surface without crashing")
	print("The game ends when you reach an altitude of zero.")
	print("A safe landing occurs if your speed is under 10 meters/second.")
	print("Good luck.")
	print("")
	
	f_use = 0
	veloc_u = velocity_up(f_use)
	veloc_d = velocity_down(veloc_d, veloc_u)
	alti = altitude_1(alti, veloc_d)
	
	print("Your downwards 'velocity' towards the moons surface is " + str(veloc_d) + " m/s") 
	print("Your remaining 'fuel' is " + str(fuel) + " litres")	   
	print("Your 'altitude' is " + str(alti) + " meters")
	print("")
	
	while alti > 0:
		# Asks for fuel usage and calculates remaining fuel
		f_use = fuel_use1(fuel)
		fuel -= f_use
			
		# Calculates upwards velocity
		veloc_u = velocity_up(f_use)
			
		# Calculates downwards velocity
		veloc_d = velocity_down(veloc_d, veloc_u)
			
		# Calculates altitude
		alti = altitude_1(alti, veloc_d)
			
		# Displays values
		if alti > 0:
			print("Your downwards 'velocity' towards the moons surface is " + str(veloc_d) + " m/s") 
			print("Your remaining 'fuel' is " + str(fuel) + " litres")	   
			print("Your 'altitude' is " + str(alti) + " meters")
			print("")

	# Calculates crater made (if any)
	crater = crater_1(alti)

	if veloc_d < 10:
		print("Congratulations you landed the rocket safely.")

	else:
		print("You crashed and made a crater " + str(crater) + " meters deep.")
	print("")


def main():
        # Replay loop			
        finished = False
        while not finished:
                alti = 1000.0
                veloc_u = 0.0
                veloc_d = 0.0
                fuel = 1000.0
                
                game_ll(alti, veloc_u, veloc_d, fuel)
                answer = False
                while not answer:
                        replay = input("Do you want to play again? y/n: ").lower()
                        if replay[0] == "y":
                                print("")
                                answer = True
                                finished = False
                        elif replay[0] == "n":
                                print("")
                                print("Thank you for playing")
                                print("Goodbye.")
                                answer = True
                                finished = True
                        else:
                                print("Incorrect response please answer either 'YES' or 'NO'. ")
                                print("")
                                answer = False
                                finished = True


if __name__ == "__main__":
        main()
