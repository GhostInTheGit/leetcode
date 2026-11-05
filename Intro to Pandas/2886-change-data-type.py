import pandas as pd

# Leetcode submission
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students

# Local testing
if __name__ == "__main__":
    data = [
        [1, "Ava", 6, 73.0],
        [2, "Kate", 15, 87.0],
    ]
    df = pd.DataFrame(data, columns=["student_id", "name", "age", "grade"])
    print(changeDatatype(df))