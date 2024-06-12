#Example dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the dataset
df=pd.read_csv("C:\\Users\\novyp\\Desktop\\abcd\\abcd.csv")
df.head()

#Pivot the values in the dataset
df_wide= df.pivot(index= 'Year', columns= 'Type', values= 'Amount')

#Remove dashed lines, add data markers
ax= sns.lineplot(data=df_wide, dashes= False, markers= True)

#Fix x-axis ticks
ax.set_xticks([2019, 2020, 2021, 2022, 2023])

#Change legend location
sns.move_legend(ax, "upper left", bbox_to_anchor=(1,1))

plt.show()