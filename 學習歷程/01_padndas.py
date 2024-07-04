import pandas as pd
"""
This module demonstrates basic usage of pandas.
"""
# 示例DataFrame的創建和打印
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
