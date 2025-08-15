import pandas as pd

dict ={
    "NAME": ['asad','muhsin','afaq'],
    "AGE"  : [24,32,12,33],
    "CGPA" : [3.1,3.0,2.4,2.2]
}

z = pd.DataFrame(dict)

print(z)