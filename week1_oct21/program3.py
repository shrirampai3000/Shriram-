average_score=int(input('Enter your average score to print your result'))
if average_score>=0 and average_score<=50:
    print('fail')
elif average_score>=51 and average_score<=75:
    print('second class')
elif average_score>=76 and average_score<=90:
    print('first class')
elif average_score>=91 and average_score<=100:
    print('distinction')
else:
    print('Invalid input')