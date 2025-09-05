```python
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

#task 1:determines the positions of each bar
school_a_x = create_x(t = 2, w = 0.8, n = 1, d = 5)
school_b_x = create_x(t = 2, w = 0.8, n = 2, d = 5)

#task 2: create a figure of width, 10 and height, 8
plt.figure(figsize = (10, 8))

#task 3: create an ax object for later use
ax = plt.subplot()

#task 4: plots the bars side by side
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)

#task 5: finds the average position for each pair of bars
middle_x = [(a+b)/2.0 for a,b in zip(school_a_x, school_b_x)]

#task 6 and 7: change the xtick
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

#task 8: add a legend for more clarity
plt.legend(['Middle School A', 'Middle School B'])

#task 9: adds a title, xlabel and ylabel
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')

#task 10: saves the figure for outside use
plt.savefig('my_side_by_side.png')
plt.show()
```


    
![png](output_0_0.png)
    

