print("[+] Loading imports...")

import sys, time, random

from pyrogram.raw.functions.channels import GetMessages

from pyrogram import Client

from random import randint, randrange, choice, randbytes

print("[✓] Loaded!")

def random_with_N_digits(n):

    range_start = 10**(n-1)

    range_end = (10**n)-1

    return randint(range_start, range_end)

dc = choice([0, 3])

code = str(dc) + str(dc) + str(dc) + str(dc) + str(dc)

random_number = "+99966" + str(dc) + str(random_with_N_digits(4))

print("[+] Generating data...")

api = [API_ID, API_HASH]
print(f"[->] Reserved number: {random_number}")

print(f"[->] Code: {code}")

app = Client(random_number, api_id=api[0], api_hash=api[1], test_mode=True, phone_number=random_number,

             phone_code=code)

print("[✓] Client inited!")

while True:

    with app:

        

       # print("[...] Trying to enable cloud password & update profile")

        try:


       # 	print("[✓] Cloud pass enabled!")

          app.update_profile(first_name="bot", last_name=f"", bio="bio")

          app.set_profile_photo(photo="image.jpg")
        
          app.send_reaction("tmbmost", 2, "🔥")

            

          app.join_chat("@rostelecom_vf")

          app.send_message("@rostelecom_support", "ростелеком топ")



        except Exception as e:
          print(e)



      

       
        print("[✓] Stopping script..")

        app.stop()

        dc = choice([0, 3])

        code = str(dc) + str(dc) + str(dc) + str(dc) + str(dc)

        random_number = "+99966" + str(dc) + str(random_with_N_digits(4))

        print("[+] Generating data...")





        api = [API_ID, API_HASH]
        print(f"[->] Reserved number: {random_number}")

        print(f"[->] Code: {code}")

        app = Client(random_number, api_id=api[0], api_hash=api[1], test_mode=True, phone_number=random_number,

             phone_code=code)

         

        

        

#app.run(main())
