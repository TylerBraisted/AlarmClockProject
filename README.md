<h1>Alarm Clock Application</h1>

  This Python mini-project generates a GUI-based alarm clock by using Python's 'tkinter' libary.

  The interface has a clock display and a start button. The clock starts with the time set to "00:00" and 
allows users to input time in the format "MM:SS" by simply typing the numbers on their keyboard. When the user 
enters a number, the clock display will update, shifting digits to the left as new digits are entered.
![image](https://github.com/user-attachments/assets/c0109d22-7e32-4785-81d4-106ad9916500)

 
  When the start button is pressed, the input is disabled, and a countdown begins based on the time set. 
The time is continuously updated on the display. Once the countdown reaches zero, an alarm sound is played
using the playsound library, and the clock resets to "00:00". The input is then re-enabled for further use. 
