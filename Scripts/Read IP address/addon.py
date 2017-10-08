ip = str(xmbc.getIPAddress())
for each in ip:
  if(each=="."):
    xmbc.playSFX("resources/dot.wav")
  elif(each=="0"):
    xmbc.playSFX("resources/zero.wav")
  elif(each=="1"):
    xmbc.playSFX("resources/one.wav")
  elif(each=="2"):
    xmbc.playSFX("resources/two.wav")
  elif(each=="3"):
    xmbc.playSFX("resources/three.wav")
  elif(each=="4"):
    xmbc.playSFX("resources/four.wav")
  elif(each=="5"):
    xmbc.playSFX("resources/five.wav")
  elif(each=="6"):
    xmbc.playSFX("resources/six.wav")
  elif(each=="7"):
    xmbc.playSFX("resources/seven.wav")
  elif(each=="8"):
    xmbc.playSFX("resources/eight.wav")
  elif(each=="9"):
    xmbc.playSFX("resources/nine.wav")
  else:
    xmbc.log("Your IP address contains unknown characters.")
