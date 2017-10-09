ip = str(xmbc.getIPAddress())
for each in ip:
  if(each=="."):
    xmbc.playSFX("resources/media/dot.wav")
  elif(each=="0"):
    xmbc.playSFX("resources/media/zero.wav")
  elif(each=="1"):
    xmbc.playSFX("resources/media/one.wav")
  elif(each=="2"):
    xmbc.playSFX("resources/media/two.wav")
  elif(each=="3"):
    xmbc.playSFX("resources/media/three.wav")
  elif(each=="4"):
    xmbc.playSFX("resources/media/four.wav")
  elif(each=="5"):
    xmbc.playSFX("resources/media/five.wav")
  elif(each=="6"):
    xmbc.playSFX("resources/media/six.wav")
  elif(each=="7"):
    xmbc.playSFX("resources/media/seven.wav")
  elif(each=="8"):
    xmbc.playSFX("resources/media/eight.wav")
  elif(each=="9"):
    xmbc.playSFX("resources/media/nine.wav")
  else:
    xmbc.log("Your IP address contains unknown characters.")
  xmbc.sleep(1000)
