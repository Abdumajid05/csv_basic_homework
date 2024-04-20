import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f=open(data,mode='r')
    a=csv.reader(f)
    b=list(a)
    c=len(b[0])
    
    return c
print(find_number_of_columns('data.csv'))

# Read the csv file