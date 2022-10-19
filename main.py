num=int(input("enter a number:"));
print(num)


if num % 2 == 0:
   print("Launch")
elif num > 5:
   print("Code")
else:
   print("LaunchCode")

engine_indicator_light = "red blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
shuttle_speed = 15000
if crew_status:
   print("Crew Ready")
else:
   print("Crew Not Ready")
  
if computer_status_code == 200:
   print("Please stand by. Computer is rebooting.")
elif computer_status_code == 400:
   print("Success! Computer online.")
else:
   print("ALERT: Computer offline!")
  
if shuttle_speed > 17500:
   print("ALERT: Escape velocity reached!")
elif shuttle_speed < 8000:
   print("ALERT: Cannot maintain orbit!")
else:
   print("Stable speed.")


