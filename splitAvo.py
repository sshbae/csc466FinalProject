import pandas as pd

def main():
        df = pd.read_csv("./finalProj/avoPrices.csv")
        df2015 = df[df['year'] == 2015]
        df2016 = df[df['year'] == 2016]
        df2017 = df[df['year'] == 2017]
        df2018 = df[df['year'] == 2017]

        out2015 = open("./finalProj/avo2015.csv", "w+")
        out2016 = open("./finalProj/avo2016.csv", "w+")
        out2017 = open("./finalProj/avo2017.csv", "w+")
        out2018 = open("./finalProj/avo2018.csv", "w+")

        df2015.to_csv(out2015, index=False)
        df2016.to_csv(out2016, index=False)
        df2017.to_csv(out2017, index=False)
        df2018.to_csv(out2018, index=False)        


if __name__ == '__main__':
    main()