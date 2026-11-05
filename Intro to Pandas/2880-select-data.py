import pandas as pd

# Leetcode submission
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101,["name", "age"]]

# Local testing
if __name__ == "__main__":
    data = [
        [101, "Ulysses", 13],
        [53, "William", 10],
        [128, "Henry", 6],
        [3, "Henry", 11],
    ]
    df = pd.DataFrame(data, columns = ["student_id", "name", "age"])
    print(selectData(df))