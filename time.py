x=int(input('enter time in seconds'))
day=x//(24*3600)
x=x%(24*3600)
hour=x//(3600)
x=x%3600
min=x//60
x=x%60
sec=x
print('Days :', day,'Hours :', hour,'Minutes :',min,'Seconds :', sec)
