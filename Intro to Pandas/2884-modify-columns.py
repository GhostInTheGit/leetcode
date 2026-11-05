import pandas as pd

# Leetcode submission
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees

# Local testing
if __name__ == "__main__":
    data = [
        ["Jack", 19666],
        ["Piper", 74754],
        ["Mia", 62509],
        ["Ulysses", 54866],
    ]
    df = pd.DataFrame(data, columns=["name", "salary"])
    print(modifySalaryColumn(df))