import pandas as pd

# Step 1: Extract
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'  # Replace with local path if needed
titanic_data = pd.read_csv(url)

# Step 2: Transform
# Check for missing values
print(titanic_data.isnull().sum())

# Fill missing 'Age' values with the median
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)

# Drop the 'Cabin' column
titanic_data.drop(columns=['Cabin'], inplace=True)

# Fill missing 'Embarked' values with the mode
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)

# Convert 'Sex' and 'Embarked' to numerical values
titanic_data['Sex'] = titanic_data['Sex'].map({'male': 0, 'female': 1})
titanic_data['Embarked'] = titanic_data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Create a new feature for family size
titanic_data['FamilySize'] = titanic_data['SibSp'] + titanic_data['Parch'] + 1

# Drop unnecessary columns
cleaned_titanic_data = titanic_data.drop(columns=['Name', 'Ticket', 'PassengerId'])

# Step 3: Load
cleaned_titanic_data.to_csv('cleaned_titanic_data.csv', index=False)
