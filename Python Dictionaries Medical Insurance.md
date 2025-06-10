# Python Dictionaries: Medical Insurance Project

You have been asked to create a program that organizes and updates medical records efficiently.

In this project, you will use your new knowledge of Python dictionaries to create a database of medical records for patients.

Let's get started!

## Storing Patient Names and Insurance Costs

1. We would like to keep a record of medical patients and their insurance costs.

   First, create an empty dictionary called `medical_costs`.


```python
medical_costs = {}
```

2. Let's populate our `medical_costs` dictionary by adding the following key-value pairs:
   - Add `"Marina"` to `medical_costs` as a key with a value of `6607.0`.
   - Add `"Vinay"` to `medical_costs` as a key with a value of `3225.0`.


```python
medical_costs.update({"Marina":6607.0, "Vinay":3225.0})
```

3. Using one line of code, add the following three patients to the `medical_costs` dictionary:
   - `"Connie"`, with an insurance cost of `8886.0`.
   - `"Isaac"`, with an insurance cost of `16444.0`.
   - `"Valentina"`, with an insurance cost of `6420.0`.


```python
medical_costs.update({"Connie":8886.0, "Isaac":16444.0, "Valentina":6420.0})
```

4. Print `medical_costs`. Make sure the dictionary is what you expected.


```python
print(medical_costs)
```

    {'Marina': 6607.0, 'Vinay': 3225.0, 'Connie': 8886.0, 'Isaac': 16444.0, 'Valentina': 6420.0}


5. You notice that `Vinay`'s insurance cost was incorrectly inputted. Update the value associated with `Vinay` to `3325.0`.

   Print the updated dictionary.


```python
medical_costs.update({"Vinay":3325})
print(medical_costs)
```

    {'Marina': 6607.0, 'Vinay': 3325, 'Connie': 8886.0, 'Isaac': 16444.0, 'Valentina': 6420.0}


6. Let's calculate the average medical cost of each patient. Create a variable called `total_cost` and set it equal to 0.

   Next, iterate through the values in `medical_costs` and add each value to the `total_cost` variable.


```python
total_cost = 0

for cost in medical_costs:
    total_cost += medical_costs[cost]
```

7. After the loop, create a variable called `average_cost` that stores the `total_cost` divided by the length of the `medical_costs` dictionary.

   Print `average_cost` with the following message:
   
   ```
   Average Insurance Cost: {average_cost}
   ```


```python
average_cost = total_cost / len(medical_costs)
print(average_cost)
```

    8336.4


## List Comprehension to Dictionary

8. You have been asked to create a second dictionary that maps patient names to their ages.

   First, create two lists called `names` and `ages` with the following data:
   
   names | ages
   --- | ---
   Marina | 27
   Vinay | 24
   Connie | 43
   Isaac | 35
   Valentina | 52


```python
names = []
ages = []
```

9. Next, create a variable called `zipped_ages` that is a zipped list of pairs between the `names` list and the `ages` list.


```python
zipped_ages = list(zip(names, ages))
```

10. Create a dictionary called `names_to_ages` by using a list comprehension that iterates through `zipped_ages` and turns each pair into a key : value item.

    Print `names_to_ages` to see the result.


```python
names_to_ages = {(name, age) for name, age in zipped_ages}
```

11. Use `.get()` to get the value of Marina's age and store it in a variable called `marina_age`. Use `None` as a default value if the key doesn't exist.

    Print `marina_age` with the following message:
    
    ```
    Marina's age is {marina_age}
    ```


```python
marina_age = medical_costs.get("Marina", None)
print("Marina\'s age is {}".format(marina_age))
```

    Marina's age is 6607.0


## Using a Dictionary to Create a Medical Database

12. Let's create a third dictionary to represent a database of medical records that contains information such as a patient's name, age, sex, gender, BMI, number of children, smoker status, and insurance cost.

    First, create an empty dictionary called `medical_records`.


```python
medical_records = {}
```

13. Next, add `"Marina"` to `medical_records` as a key with the value being a dictionary of medical data:

    ```py
    {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
    ```


```python
medical_records["Marina"] = {"Age":27, 
                             "Sex":"Female", 
                             "BMI":31.1, "Children":2, 
                             "Smoker":"Non-Smoker",
                             "Insurance_cost":6607.0}
```

14. Do the same for the following individuals:
    
    Name | Age | Sex | BMI | Children | Smoker | Insurance Cost
    --- | --- | --- | --- | --- | --- | ---
    Vinay | 24 | Male | 26.9 | 0 | Non-smoker | 3225.0
    Connie | 43 | Female | 25.3 | 3 | Non-smoker | 8886.0
    Isaac | 35 | Male | 20.6 | 4 | Smoker | 16444.0
    Valentina | 52 | Female | 18.7 | 1 | Non-smoker | 6420.0


```python
medical_records.update({"Vinay":{"Age":24, 
                                "Sex":"Male", 
                                "BMI":26.9, "Children":0,
                                "Smoker":"Non-smoker",
                                "Insurance_cost":3225.0}, 
                        "Connie":{"Age":43, 
                                "Sex":"Female", 
                                "BMI":25.3, "Children":3,
                                "Smoker":"Non-smoker",
                                "Insurance_cost":8886.0},
                        "Isaac":{"Age":35, 
                                "Sex":"Male", 
                                "BMI":20.6, "Children":4,
                                "Smoker":"Smoker",
                                "Insurance_cost":16444.0},
                        "Valentina":{"Age":52, 
                                "Sex":"Female", 
                                "BMI":18.7, "Children":1,
                                "Smoker":"Non-smoker",
                                "Insurance_cost":6420.0}})
```

15. Print `medical_records` to see the result.


```python
print(medical_records)
```

    {'Marina': {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Children': 2, 'Smoker': 'Non-Smoker', 'Insurance_cost': 6607.0}, 'Vinay': {'Age': 24, 'Sex': 'Male', 'BMI': 26.9, 'Children': 0, 'Smoker': 'Non-smoker', 'Insurance_cost': 3225.0}, 'Connie': {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Children': 3, 'Smoker': 'Non-smoker', 'Insurance_cost': 8886.0}, 'Isaac': {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4, 'Smoker': 'Smoker', 'Insurance_cost': 16444.0}, 'Valentina': {'Age': 52, 'Sex': 'Female', 'BMI': 18.7, 'Children': 1, 'Smoker': 'Non-smoker', 'Insurance_cost': 6420.0}}


16. The `medical_records` dictionary acts like a database of medical records. Let's access a specific piece of data in `medical_records`.

    Print out `Connie`'s insurance cost with the following message:
    
    ```
    Connie's insurance cost is X dollars.
    ```


```python
connies_insurance = medical_records["Connie"]["Insurance_cost"]
print("Connie\'s insurance cost is " + str(connies_insurance) + " dollars.")
```

    Connie's insurance cost is 8886.0 dollars.


17. `Vinay` has moved to a new country, and we no longer want to include him in our medical records.

    Remove `Vinay` from `medical_records`.


```python
medical_records.pop("Vinay")
```




    {'Age': 24,
     'Sex': 'Male',
     'BMI': 26.9,
     'Children': 0,
     'Smoker': 'Non-smoker',
     'Insurance_cost': 3225.0}



18. Let's take a closer look at each patient's medical record.

    Use a `for` loop to iterate through the items of `medical_records`. For each key-value pair, print out a string that looks like the following:
    
    ```
    {Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}
    ```


```python
for record in medical_records:
    name = record
    age = medical_records[record]['Age']
    sex = medical_records[record]['Sex']
    smoker = medical_records[record]['Smoker']
    bmi = medical_records[record]['BMI']
    insurance_cost = medical_records[record]['Insurance_cost']
    
    print("{name} is a {age} year old {sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}".format(
        name = name, age = age, sex = sex, Smoker = smoker, BMI = bmi, Insurance_cost = insurance_cost))
    
```

    Marina is a 27 year old Female Non-Smoker with a BMI of 31.1 and insurance cost of 6607.0
    Connie is a 43 year old Female Non-smoker with a BMI of 25.3 and insurance cost of 8886.0
    Isaac is a 35 year old Male Smoker with a BMI of 20.6 and insurance cost of 16444.0
    Valentina is a 52 year old Female Non-smoker with a BMI of 18.7 and insurance cost of 6420.0


## Extra

19. Congratulations! In this project, you used Python dictionaries to store and update medical data for individuals.

    If you'd like extra practice with dictionaries, here are some suggestions to go further with this project:
    - Create a function called `update_medical_records()` that takes in the name of an individual as well as their medical data, and then updates the `medical_records` dictionary accordingly.
    - Create a new dictionary of your choice - feel free to get creative!
    
    Happy coding!


```python
def update_medical_records(name, age, sex, children, smoker, bmi, insurance_cost, medical_records):
    medical_records.update({name:{"Age":age, 
                                "Sex":sex, 
                                "BMI":bmi, "Children":children,
                                "Smoker":smoker,
                                "Insurance_cost":insurance_cost}})
    return medical_records

update_medical_records = update_medical_records(name = "Baba", 
                                                age = 25, 
                                                sex = "Male", 
                                                children = 0,
                                                smoker = "Non-smoker",
                                                bmi = 23.3, 
                                                insurance_cost = 2000.0, 
                                                medical_records = medical_records)
print(update_medical_records)
    
```

    {'Marina': {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Children': 2, 'Smoker': 'Non-Smoker', 'Insurance_cost': 6607.0}, 'Connie': {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Children': 3, 'Smoker': 'Non-smoker', 'Insurance_cost': 8886.0}, 'Isaac': {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4, 'Smoker': 'Smoker', 'Insurance_cost': 16444.0}, 'Valentina': {'Age': 52, 'Sex': 'Female', 'BMI': 18.7, 'Children': 1, 'Smoker': 'Non-smoker', 'Insurance_cost': 6420.0}, 'Baba': {'Age': 25, 'Sex': 'Male', 'BMI': 23.3, 'Children': 0, 'Smoker': 'Non-smoker', 'Insurance_cost': 2000.0}}



```python

```
