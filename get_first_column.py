import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f=open(data,mode='r')
    a=csv.reader(f)
    b=list(a)
    return b[1]
print(get_first_column('data.csv'))
    
# Read the csv file