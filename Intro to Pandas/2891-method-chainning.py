import pandas as pd

# Leetcode submission
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[["name"]]

# Local testing
if __name__ == "__main__":
    data = [
    ["Tatiana", "Snake", 98, 464],
    ["Khaled", "Giraffe", 50, 41],
    ["Alex", "Leopard", 6, 328],
    ["Jonathan", "Monkey", 45, 463],
    ["Stefan", "Bear", 100, 50],
    ["Tommy", "Panda", 26, 349],
    ]
    df = pd.DataFrame(data, columns=["name", "species", "age", "weight"])
    print(findHeavyAnimals(df))