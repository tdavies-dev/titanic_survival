import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Use the read_csv() function to read the CSV file into a Pandas DataFrame
titanic_df = pd.read_csv('titanic_train.csv')
#also reading it into seaborn for data vis
titanic_df['PassengerId'] = titanic_df['PassengerId'].astype(int)  # Convert to integer if needed

##From Project Documentation
#survival	Survival	0 = No, 1 = Yes
# pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
# sex	Sex	
# Age	Age in years	
# sibsp	# of siblings / spouses aboard the Titanic	
# parch	# of parents / children aboard the Titanic	
# ticket	Ticket number	
# fare	Passenger fare	
# cabin	Cabin number	
# embarked	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton


# ----- Create subplots showing distribution of passengers for "Embarked" and "PClass"------
plt.figure(figsize=(12, 6))

# Plot for "Embarked"
plt.subplot(1, 2, 1)
sns.countplot(x="Embarked", data=titanic_df, palette="Set1")
plt.title("Number of Passengers by Embarked")

# Plot for "PClass"
plt.subplot(1, 2, 2)
sns.countplot(x="Pclass", data=titanic_df, palette="Set2")
plt.title("Number of Passengers by PClass")

# Adjust the layout
plt.tight_layout()

# Show the plots
plt.show()

# ----- Create histogram of fare prices across passengers------
plt.figure(figsize=(10, 6))
sns.distplot(titanic_df['Fare'], bins=30, color='skyblue', kde=True)
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Histogram of Fares Paid by Passengers')
plt.grid(True)
plt.show()
