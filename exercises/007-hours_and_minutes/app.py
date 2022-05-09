#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  hora=int(secs/3600)
  minutes=int(((secs/3600)-hora)*60+1)
  result =(hora, minutes)
  return result

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))