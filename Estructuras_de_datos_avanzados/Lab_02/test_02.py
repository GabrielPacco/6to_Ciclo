
import plotly.express as px 
  
# using the tips dataset
df = px.data.tips() 

# print all the data
for index, row in df.iterrows():
    # print all the columns
    for col in df.columns:
        print(row[col], end=' ')
    print()
    
  
# plotting the box chart
fig = px.box(df, x="day", y="total_bill")
  
# showing the plot
fig.show()