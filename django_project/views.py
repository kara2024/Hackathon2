import requests
from django.shortcuts import render

def title(request):
  Q = requests.get('https://api.github.com/events')
  data = Q.json()
  result = data[0]["repo"]

  Q2 = requests.get('http://numbersapi.com/random/year?json')
  data2 = Q2.json()
  result2 = data2['text']

  Q3 = requests.get('https://freetestapi.com/api/v1/students')
  data3 = Q3.json()
  result3 = data3[0]

  Q4 = requests.get('https://api.thecatapi.com/v1/images/search')
  data4 = Q4.json()
  result4 = data4[0]['url']

  Q5 = requests.get('https://api.chucknorris.io/jokes/random')
  data5 = Q5.json()
  result5 = data5['value']

  Q6 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data6 = Q6.json()
  result6 = data6['text']
  
  return render(request, 'templates/index.html', {'result': result, 'result2': result2, 'result3': result3, 'result4': result4, 'result5': result5, 'result6': result6})