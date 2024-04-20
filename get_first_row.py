import csv 
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   f=open(data,mode='r')
   a=csv.reader(f)
   b=list(a)
   l=[]
   for i in b[1:]:
       l.append(i[0])
   return l
print(get_first_row('data.csv'))
   

# Read the csv file