factr = raw_input("What warp factor do you wish to travel at? ")
if factr > 10:
	print ("That warp factor is unattainable.")
	factr = raw_input("What warp factor do you wish to travel at? ")
elif factr != int:
	print ("Please enter a number.")
	factr = raw_input("What warp factor do you wish to travel at? ")
else:
	break
	
choice = raw_input("What equivalent measurement do you want for your warp factor? If none, it will default to meters per second: ")
speed = (int(factr) ** 3) * (1292.7238)
warp = speed * 299792458
measurement = (" meters per second")
if choice == "miles" or "Miles":
	warp * 0.0006213712
	str.replace(choice, (" meters"), (" miles"))
elif choice == "" or " ":
	   pass
elif choice == "kilometers" or "Kilometers" or "kilometres" or "Kilometres":
	   warp / 100
	   str.replace(choice, (" meters"), ("kilometers")
#else:
 #   print ("That is not a valid measurement.")
	#choice = raw_input("What equivalent measurement do you want for your warp factor? If none, it will default to meters per second: ")
rsult == '{:.1f}'.format(warp)
print("At this warp factor, you are travelling the equivalent of "), rsult, measurement
