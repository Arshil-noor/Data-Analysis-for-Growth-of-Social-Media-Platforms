# B.Tech IT Third Year (Technical Assessment-1)
# Given by: MR. ARSHIL NOOR
import pandas as pd
import matplotlib.pyplot as plt

fig, ax=plt.subplots()
df = pd.read_excel("C:\\Users\\पज\\Desktop\\Impor\\Social.xlsx","Sheet1")
print(df)
plt.plot(df['Social Media'],df['In Year: 2020'])
plt.plot(df['Social Media'],df['In Year: 2021'])
plt.plot(df['Social Media'],df['In Year: 2022'])
plt.plot(df['Social Media'],df['In Year: 2023'])
plt.plot(df['Social Media'],df['In Year: 2024'])

plt.xlabel('Social Media Sites',color='blue')
plt.ylabel('No. of Users per Year',color='blue')
plt.title('IT-III Technical Assessment 1: Learning Popularity of Social Media sites over the Years',color='red')
plt.grid()
plt.show() 
