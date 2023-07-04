import win32com.client

speakOutLoud = win32com.client.Dispatch("SAPI.SpVoice")

while True:
  strSpeak = input("Write the string that you want to speak from the computer:-\n")
  if strSpeak == 'q':
    break
  speakOutLoud.Speak(strSpeak)
