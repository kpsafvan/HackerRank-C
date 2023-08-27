a=['U45', 'Palakkad', 'HealthifyMe,', '[15.07.21', '16:50]','Vaccine:', 'COVISHIELD', '(1st', 'Dose)','Pincode:', '679308']
['U45', '1', 'Palakkad', 'HealthifyMe,', '[15.07.21', '16:50]']
['Vaccine:', 'COVISHIELD', '(1st', 'Dose)']
['Pincode:', '679308']

x=str(input().split())
print(x)
x=str(input().split())
print(x)
x=str(input().split())
print(x)
x=str(input().split())
print(x)
x=str(input().split())
print(x)
while(1) :
 c = input()
 b=c.split()
 for ele in b :
  if ele not in a :
   print(ele)
  