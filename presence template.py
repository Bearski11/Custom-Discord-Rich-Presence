from pypresence import Presence
import time

client_id = 'YOU CLIENT ID HERE' #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

print(RPC.update(state="STATE HERE", details="DETAILS HERE", large_image="NAME OF LARGE IMAGE HERE", small_image="NAME OF SMALL IMAGE HERE", large_text="LARGE IMAGE TEXT HERE", start=time.time()))  # Set the presence

while True: 
    time.sleep(15) 