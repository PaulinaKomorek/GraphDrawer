import pandas as pd
from io import StringIO

class DataService:
    data: pd.DataFrame

    def __init__(self, content: str):
        buff = StringIO(content)
        self.data=pd.read_csv(buff, sep=' ', header=None)

    def columns(self, x_column: int,  y_columns: list):
        rows=self.data.values.tolist()
        x_values=list(map(lambda row : row[x_column], rows))
        y_values=[]
        for n in y_columns:
            y_values.append(list(map(lambda row: row[n], rows)))
        return x_values, y_values


