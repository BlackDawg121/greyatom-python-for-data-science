# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#print(data)
#Code starts here
census=np.concatenate((new_record,data),axis=0)
#print(census)
print(np.shape(data))
print(np.shape(census))

age=np.array(census[:,0])
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)
race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]
#race=np.array()
#print(race)
for i in census[:,2]:
    if i==0:
        race_0=np.append(i,race_0)
    if i==1:
        race_1=np.append(i,race_1)
    if i==2:
        race_2=np.append(i,race_2)
    if i==3:
        race_3=np.append(i,race_3)
    if i==4:
        race_4=np.append(i,race_4)

#print(race_0)

len_0=race_0.size
len_1=race_1.size
len_2=race_2.size
len_3=race_3.size
len_4=race_4.size
#print(len_0)

minority_race=min(len_0,len_1,len_2,len_3,len_4)
if minority_race==len_0:
    minority_race=0
if minority_race==len_1:
    minority_race=1
if minority_race==len_2:
    minority_race=2
if minority_race==len_3:
    minority_race=3
if minority_race==len_4:
    minority_race=4
print(minority_race)


#s4

senior_citizens=census[census[:,0]>60]
#print(senior_citizens)

working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)

avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)

#s5

high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)



