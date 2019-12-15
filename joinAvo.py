import pandas as pd

def main():
    df1 = pd.read_csv("./finalProj/avo2015Fixed.csv")
    df2 = pd.read_csv("./finalProj/avo2016Fixed.csv")
    df3 = pd.read_csv("./finalProj/avo2017Fixed.csv")
    df4 = pd.read_csv("./finalProj/avo2018Fixed.csv")

    a = pd.concat([df1, df2])
    b = pd.concat([df3, df4])

    c = pd.concat([a, b])
    c.to_csv(open("./finalProj/avoWagesFixed.csv", "w+"), index=False)

if __name__ == '__main__':
    main()

