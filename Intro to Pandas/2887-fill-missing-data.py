import pandas as pd

# Leetcode submission
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna({"quantity": 0})

# Local testing
if __name__ == "__main__":
    data = [
    ["Wristwatch", None, 135],
    ["WirelessEarbuds", None, 821],
    ["GolfClubs", 779, 9319],
    ["Printer", 849, 3051],
    ]
    df = pd.DataFrame(data, columns=["name", "quantity", "price"])
    print(fillMissingValues(df))