**Startup guide for the WannaBe Engineering 3x3 macropad:**

First off, thank you for purchasing this PCB, and I hope it works out well for you. I'll do my best to provide clear instructions, 
but if it's a bit hard to follow, or flawed in any way, please let me know via the email provided at the bottom. 

**Things you'll need:**

**1:** The latest version of circuit python, available here https://circuitpython.org/board/waveshare_rp2040_zero/
- Follow the link, then download the .UF2 file by clicking the big purple button

![1 uf2 download](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/4b70e3a0-4237-45cb-bec1-074be9acae2b)

---------------------------------------------------------------------------------------------------------
  
**2:** The latest and greatest KMK firmware, available here https://github.com/KMKfw/kmk_firmware
- Click the green button labeled “Code”
- Then select the bottom option “Download ZIP”
  
![2 kmk download](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/9d53793d-32ff-44c2-af8c-f09a5dc07f95)

---------------------------------------------------------------------------------------------------------

**3:** The code.py file, used to program this macropad, available on our Github here https://github.com/WannaBeEngineering/3x3-macropad
- Click the green button labeled “Code”
- Then select the bottom option “Download ZIP”
  
![3 codedownload](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/7914ef2e-f7d4-4087-b14f-d2dfe47743be)

---------------------------------------------------------------------------------------------------------

**Alright lets begin.** 

**1:** Go ahead and unzip both folders, as seen in the two pictures below. After unzipping them, feel free to de-clutter by deleting the original zipped files. 

![5 unzip code](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/3ba33c04-e322-4d5e-ba0b-43014f68cc5b)
![4 unzip kmk](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/ec969e9a-796b-49c6-a958-8666368121bc)

- Once you've done that, your downloads folder should look like this

![6  unzipped files](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/7c6e7810-1724-403f-8ad3-51a86df9139f)

---------------------------------------------------------------------------------------------------------

**2:** Now you're ready to plug in your device. While holding down the "Boot" button on your RP2040-Zero (as seen below), plug in your macropad.

![7 boot button](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/573ad20e-98d5-420c-9f5d-a24c72beddf3)

---------------------------------------------------------------------------------------------------------

3: Once the macropad connects to your computer, look for the drive "RPI-RP2" on the left side. Once you verify it's there, go ahead and drag the Circuitpython .UF2 file directly onto it.

![8 uf2 to rpi](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/05e9e422-3df5-4685-aae2-d2f5cd522d4e)

- After completing this step, the RPI drive will dismount, then remount under the name "CIRCUITPY", as seen in the picture below.
  
![9 circuitpyreboot](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/b85f2a2c-15b4-44e1-8a15-1c9853142e02)

---------------------------------------------------------------------------------------------------------

**4:** In a similar fashion to how you loaded the .UF2 file, you'll now do the same with the KMK folder, and the code.py file from our Github.

![10 kmktocp](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/92e5b64b-b063-47b7-9e7a-006a8112535c)
![11 codetocp](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/9b11e8f2-8c7f-442b-afdb-a9a7c3e758d7)

- Once thats done, click into your CIRCUITPY drive and verify your files are there.

![12 checkfiles](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/4a610fb1-e407-454b-8801-080583568f8b)

**5:** Testing your macropad. Now that everything's in place, you can press the "Reset" button on your RP2040-Zero, and check the functionality. 

![13 reset_test](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/b4bf63a9-3fd1-400f-b83e-ce7dd77012a2)

- Open up your notepad app, or whatever you'd like and give the macropad a go. Left to right, bottom to top (as a regular number pad) the keys are programmed as
  numbers 1-9, the rotary encoder will control volume, and the rotary encoder switch will mute/unmute. All of which can be customized, as detailed below. 
  
---------------------------------------------------------------------------------------------------------

**Customization:**
On the KMK Github, you can find a whole plethora of options for your macropad. You can assign keystrokes, hot-keys, mouse inputs, etc etc etc. I'll attach the link to
the "keys overview" page on the KMK Github, and you can find the alternate options on the left side directory. 
https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/keycodes.md

![14 keyoverview](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/61f9cf9a-e7c4-48d9-b19e-7323c18f775e)

- You can use any text editor you'd like, including something as basic as your Notepad app. My personal recommendation would be Thonny (https://thonny.org/), as I find that the best for
programming microcontrollers. 
- Pictured below is the code.py file provided, here you can see the keymaps. To customize your macropad, you'll simply swap out
the existing inputs for the ones you'd like.

![13 keymap (1)](https://github.com/WannaBeEngineering/3x3-macropad/assets/165714796/cc032c64-4d24-43f7-b844-02db5afa7552)

---------------------------------------------------------------------------------------------------------

Alright well hopefully that went smoothly 👍 Like mentioned above, if there are any holes in these instructions please let me know!

Thanks again,
Alex
alex@wannab.shop

