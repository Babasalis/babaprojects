# U.S. Medical Insurance Costs


```python
#Project tasks:
#1. Find out which region has the highest and lowest charges.
#2. Find out which age gets charged the lowest and highest.
#3. Find out the difference in charges between male and female patients.
#4. Find the total amount of charges
import csv
```


```python
#import insurance.csv into python file, converts the csv content into python dictionary to inspect.
with open('insurance.csv') as insurance_sheet:
    dic_convert = csv.DictReader(insurance_sheet)
    #makes sure DictReader iterates more than once
    insurance = list(dic_convert)
    ages = []
    sex = []
    bmis = []
    children = []
    smokers = []
    regions = []
    charges = []

#adding column content in named variables
    for row in insurance:
        ages.append(row['age'])
        sex.append(row['sex'])
        bmis.append(row['bmi'])
        children.append(row['children'])
        smokers.append(row['smoker'])
        regions.append(row['region'])
        charges.append(row['charges'])
        # print(row)
```


```python
#Prints out the unique region values
unique_regions = set(regions)
print(unique_regions)
```

    {'southeast', 'southwest', 'northwest', 'northeast'}



```python
#Finds out the highest and lowest charges per region
def region_charges(regions, charges):
    combined_list = list(zip(regions, charges))
    total_charges = 0
    nw_charges = 0
    ne_charges = 0
    sw_charges = 0
    se_charges = 0

    for region, charge in combined_list:
        #Finds the total amount of charges for all regions
        total_charges += float(charge)
        #Adds respective charges to regions
        if region == 'northwest':
            nw_charges += float(charge)
        elif region == 'northeast':
            ne_charges += float(charge)
        elif region == 'southwest':
            sw_charges += float(charge)
        elif region == 'southeast':
            se_charges += float(charge)

    print('The total amount of charges is ' + str(total_charges))

    print('''The charges for the Northeastern region is {} 
The charges for the Northwestern region is {} 
The charges for the Southeastern region is {} 
The charges for the Southwestern region is {}'''.
          format(ne_charges, nw_charges, se_charges, sw_charges))  

region_charges(regions, charges)
```

    The total amount of charges is 17755824.990759
    The charges for the Northeastern region is 4343668.583308999 
    The charges for the Northwestern region is 4035711.9965399993 
    The charges for the Southeastern region is 5363689.763290002 
    The charges for the Southwestern region is 4012754.647620001



```python
#prints out the unique ages
ages = []
count = 0
for row in insurance:
    ages.append(row['age'])
unique_ages = set(ages)
print(unique_ages)
for age in unique_ages:
    count += 1
print(count)
```

    {'35', '24', '18', '64', '63', '49', '44', '30', '55', '56', '47', '28', '48', '40', '58', '21', '52', '29', '51', '31', '22', '61', '60', '38', '59', '19', '53', '42', '37', '50', '36', '33', '34', '54', '43', '27', '25', '46', '41', '62', '45', '26', '20', '23', '57', '39', '32'}
    47



```python
def age_charges(ages, charges):
    combined_list = list(zip(ages, charges))
    unique_ages = {'34':0, '29':0, '35':0, '25':0, '50':0, '55':0, '64':0, '52':0, '53':0, '21':0, 
               '39':0, '44':0, '47':0, '51':0, '27':0, '22':0, '62':0, '19':0, '33':0, '28':0, 
               '49':0, '23':0, '31':0, '43':0, '42':0, '61':0, '26':0, '37':0, '54':0, '20':0, 
               '45':0, '56':0, '36':0, '46':0, '30':0, '58':0, '57':0, '38':0, '59':0, '48':0, 
               '41':0, '18':0, '60':0, '63':0, '32':0, '24':0, '40':0}
    for age, charges in combined_list:
        if age in unique_ages:
            unique_ages[age] += float(charges)

#Prints out a tuple containing ages and their respective charges
    # for i in unique_ages.items():
    #      print(i)

#Finds the age with the maximum and minimum charges
    max_charge = max(unique_ages, key = unique_ages.get)
    min_charge = min(unique_ages, key = unique_ages.get)
    print('The age with the most charges of {} is {}'.
          format(unique_ages[max_charge], max_charge))
    print('The age with the least charges of {} is {}'.
          format(unique_ages[min_charge], min_charge))
    
age_charges(ages, charges)
```

    The age with the most charges of 662857.8347499999 is 19
    The age with the least charges of 132453.00123 is 21



```python
def gender_charge_difference(sex, charges):
    combined_list = list(zip(sex, charges))
    total_male_charge = 0
    total_female_charge = 0

    #Find the total amount of charges for both male and female
    for sex, charge in combined_list:
        if sex == 'male':
            total_male_charge += float(charge)
        else:
            total_female_charge += float(charge)

    #Finds the difference b/w male and female charges
    charge_difference = total_male_charge - total_female_charge
    
    print('The total amount of charges for the male sex = ' + str(total_male_charge))
    print('The total amount of charges for the female sex = ' + str(total_female_charge))
    print('The difference between the male and female charges is ' + str(charge_difference))
gender_charge_difference(sex, charges)
```

    The total amount of charges for the male sex = 9434763.796139995
    The total amount of charges for the female sex = 8321061.194618994
    The difference between the male and female charges is 1113702.6015210003

