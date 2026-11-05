import pandas as pd

# Leetcode submission
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars="product", var_name="quarter", value_name="sales")

# Local testing
if __name__ == "__main__":
    data = [
        ["Umbrella", 417, 224, 379, 611],
        ["SleepingBag", 800, 936, 93, 875],
    ]
    df = pd.DataFrame(data, columns=["product", "quarter1", "quarter2", "quarter3", "quarter4"  ])
    print(meltTable(df))