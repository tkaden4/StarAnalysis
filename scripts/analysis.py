import matplotlib.pyplot as plt
import pandas as pd
import os.path as path

def languages(df):
    dfl = df.groupby(["language"]).filter(lambda col: len(col) > 110)
    dfl = dfl["stargazers"]
    print(dfl)

if __name__ == "__main__":
    df = pd.read_json("stars_munged.json")
    #df.plot(kind="scatter", x="stargazers", y="forks_count", color="blue")
    #plt.show()
    languages(df)
