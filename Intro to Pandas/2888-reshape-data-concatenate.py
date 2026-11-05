import pandas as pd

# Leetcode submission
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])

# Local testing
if __name__ == "__main__":
    df1_data = [
    [1, "Mason", 8],
    [2, "Ava", 6],
    [3, "Taylor", 15],
    [4, "Georgia", 17],
    ]
    df1 = pd.DataFrame(df1_data, columns=["student_id", "name", "age"])
    
    df2_data = [
    [5, "Leo", 7],
    [6, "Alex", 7],
    ]
    df2 = pd.DataFrame(df2_data, columns=["student_id", "name", "age"])
    print(concatenateTables(df1, df2))