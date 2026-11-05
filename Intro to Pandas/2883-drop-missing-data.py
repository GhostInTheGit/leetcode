import pandas as pd

# Leetcode submission
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset="name")

# Local testing
if __name__ == "__main__":
    data = [
        [32, "Piper", 5],
        [217, None, 19],
        [779, "Georgia", 20],
        [849, "Willow", 14],
    ]
    df = pd.DataFrame(data, columns=["student_id", "name", "age"])
    print(dropMissingData(df))