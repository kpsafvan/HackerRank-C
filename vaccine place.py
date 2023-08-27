a=['Palakkad','THQH', 'HealthifyMe,','Vaccine:', 'COVISHIELD','Dose)','Pincode:','Age', 'Group:','Center', 'Name:', 'CHC','FHC', 'PHC','Date:','Jul','Aug','Available', 'slots:','Cost:', '₹', 'Free']
while(1) :
 c = input()
 [x for x in c if not any(v.isdigit() for v in x)]
 b=c.split()
 for ele in b :
  if any(v.isdigit() for v in ele):
   break
  if ele not in a :
   print(ele,",",end='')
  