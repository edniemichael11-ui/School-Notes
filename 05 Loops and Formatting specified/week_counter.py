# Your end of week challenge:
"""

Ask the user how much time we have (in seconds)
Verify they provide an positive int, ask again until they do

After getting a valid int:
clear the screem
display the number
pause for one second
clear the screen
reduce the number and display in
pause for 1 second
do this until it hits zero
then open a broswer to this link:https://gifdb.com/images/high/homer-running-away-from-explosion-bsb0orb1dmn498e3.webp
"""

import os
import time
import webbrowser
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
url = "https://gifdb.com/images/high/homer-running-away-from-explosion-bsb0orb1dmn498e3.webp"
countdown = int(input("How much time do we got (sec): "))

while countdown <0:
    time = int(input("Invalid Time, How much time: "))
clear_screen()
print(time, flush = True)
while countdown > 0:
    time.sleep(1)
    countdown -= 1
    print(countdown)
    time.sleep(1)
    clear_screen()
webbrowser.open(url)