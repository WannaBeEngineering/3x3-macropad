**Startup guide for the WannaBe Engineering 3x3 macropad:**

First off, thank you for purchasing this PCB, and I hope it works out well for you. I'll do my best to provide clear instructions, 
but if it's a bit hard to follow, or flawed in any way, please let me know via the email provided at the bottom. 

**Things you'll need:**

**1:** The latest version of circuit python, available here https://circuitpython.org/board/waveshare_rp2040_zero/
- Follow the link, then download the .UF2 file by clicking the big purple button
  
![1 uf2 download](https://github.com/WannaBeEngineering/testing_area/assets/165714796/b1e01394-2d74-4bca-859c-ef9478c3c5ea)

---------------------------------------------------------------------------------------------------------
  
**2:** The latest and greatest KMK firmware, available here https://github.com/KMKfw/kmk_firmware
- Click the green button labeled “Code”
- Then select the bottom option “Download ZIP”
  
![2 kmk download](https://github.com/WannaBeEngineering/testing_area/assets/165714796/7acc8ffb-6362-4da4-b126-c676240a3c91)

---------------------------------------------------------------------------------------------------------

**3:** The code.py file, used to program this macropad, available on our Github here https://github.com/WannaBeEngineering/3x3-macropad
- Click the green button labeled “Code”
- Then select the bottom option “Download ZIP”
  
![3 codedownload](https://github.com/WannaBeEngineering/testing_area/assets/165714796/1a259a7e-ce4a-4e14-a6ba-79573ef75ef9)

---------------------------------------------------------------------------------------------------------

**Alright lets begin.** 

**1:** Go ahead and unzip both folders, as seen in the two pictures below. After unzipping them, feel free to de-clutter by deleting the original zipped files. 

![5 unzip code](https://github.com/WannaBeEngineering/testing_area/assets/165714796/553ca175-8065-4bcc-9a0d-839c1f5e6f16)
![4 unzip kmk](https://github.com/WannaBeEngineering/testing_area/assets/165714796/33b1559a-9518-4696-830c-1b09d13d1a9b)

- Once you've done that, your downloads folder should look like this

![6  unzipped files](https://github.com/WannaBeEngineering/testing_area/assets/165714796/885d4016-5117-40cb-8975-b9e8693c98c4)

---------------------------------------------------------------------------------------------------------

**2:** Now you're ready to plug in your device. While holding down the "Boot" button on your RP2040-Zero (as seen below), plug in your macropad.

![7 boot button](https://github.com/WannaBeEngineering/testing_area/assets/165714796/3689458b-a0a4-4f8d-b545-9128899bd41f)

---------------------------------------------------------------------------------------------------------

3: Once the macropad connects to your computer, look for the drive "RPI-RP2" on the left side. Once you verify it's there, go ahead and drag the Circuitpython .UF2 file directly onto it.

![8 uf2 to rpi](https://github.com/WannaBeEngineering/testing_area/assets/165714796/a8b11d16-4637-402f-b53d-7a9ad9ca7f29)


- After completing this step, the RPI drive will dismount, then remount under the name "CIRCUITPY", as seen in the picture below. 

![9 circuitpyreboot](https://github.com/WannaBeEngineering/testing_area/assets/165714796/b0aec058-1df5-487f-84b2-2c851bcec1d4)

---------------------------------------------------------------------------------------------------------

**4:** In a similar fashion to how you loaded the .UF2 file, you'll now do the same with the KMK folder, and the code.py file from our Github.

![10 kmktocp](https://github.com/WannaBeEngineering/testing_area/assets/165714796/844bd40b-f417-4d1b-945f-9dc09064d112)
![11 codetocp](https://github.com/WannaBeEngineering/testing_area/assets/165714796/be6d6b7d-34ad-4344-bd8e-bffd585d1a18)

- Once thats done, click into your Circuitpy drive and verify your files are there.

![12 checkfiles](https://github.com/WannaBeEngineering/testing_area/assets/165714796/c0f82776-4f32-4aed-8560-86616680b8e9)

**5:** Testing your macropad. Now that everything's in place, you can press the "Reset" button on your RP2040-Zero, and check the functionality. 

![13 reset_test](https://github.com/WannaBeEngineering/testing_area/assets/165714796/1549597e-a407-485a-b875-9dc6bd872e96)

- Open up your notepad app, or whatever you'd like and give the macropad a go. Left to right, bottom to top (as a regular number pad) the keys are programmed as
  numbers 1-9, the rotary encoder will control volume, and the rotary encoder switch will mute/unmute. All of which can be customized, as detailed below. 
  
---------------------------------------------------------------------------------------------------------

**Customization:**
On the KMK Github, you can find a whole plethora of options for your macropad. You can assign keystrokes, hot-keys, mouse inputs, etc etc etc. I'll attach the link to
the "keys overview" page on the KMK Github, and you can find the alternate options on the left side directory. 
https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/keycodes.md

![14 keyoverview](https://github.com/WannaBeEngineering/testing_area/assets/165714796/32e999f3-35e0-45fb-9666-3a5f1fb67c55)

- You can use any text editor you'd like, including something as basic as your Notepad app. My personal recommendation would be Thonny (https://thonny.org/), as I find that the best for
programming microcontrollers. 
- Pictured below is the code.py file provided, here you can see the keymaps. To customize your macropad, you'll simply swap out
the existing inputs for the ones you'd like.

![13 keymap (1)](https://github.com/WannaBeEngineering/testing_area/assets/165714796/3e66839b-7436-4d74-82d7-9b4c9e64a98a)

---------------------------------------------------------------------------------------------------------

Alright well hopefully that went smoothly 👍 Like mentioned above, if there are any holes in these instructions please let me know!

Thanks again,
Alex
alex@wannab.shop

