import scipy
import pandas as pd
import numpy as np
#from sklearn import tree

def classify_region(df: pd.DataFrame, region):
    bounds = {}
    temp_df = df.loc[(df['region'] == region)]
    bounds['cheapest'] = (temp_df.quantile([0.15]))['AveragePrice'].iloc[0]
    bounds['cheap'] = (temp_df.quantile([0.3]))['AveragePrice'].iloc[0]
    bounds['moderate'] = (temp_df.quantile([0.7]))['AveragePrice'].iloc[0]
    bounds['expensive'] = (temp_df.quantile([0.85]))['AveragePrice'].iloc[0]
    bounds['most_expensive'] = (temp_df.quantile([1]))
    df.loc[(df['region'] == region) & (df['AveragePrice'] <= bounds['cheapest']), 'PriceRange'] = 'v_cheap'
    df.loc[(df['region'] == region) & (df['AveragePrice'] <= bounds['cheap']) &
                                       (df['PriceRange'].isna()), 'PriceRange'] = 'cheap'
    df.loc[(df['region'] == region) & (df['AveragePrice'] <= bounds['moderate']) &
                                       (df['PriceRange'].isna()), 'PriceRange'] = 'moderate'
    df.loc[(df['region'] == region) & (df['AveragePrice'] <= bounds['expensive']) &
                                       (df['PriceRange'].isna()), 'PriceRange'] = 'expensive'
    df.loc[(df['region'] == region) & (df['PriceRange'].isna()), 'PriceRange'] = 'v_expensive'
    # print(df.loc[df['region'] == region])
    # for index, row in df.loc[df['region'] == region].iterrows():
    #     price = row['AveragePrice']
    #     if price <= bounds['cheapest']:
    #         df.loc[index, 'PriceRange'] = 'v_cheap'
    #     elif price <= bounds['cheap']:
    #         df.loc[index, 'PriceRange'] = 'cheap'
    #     elif price <= bounds['moderate']:
    #         df.loc[index, 'PriceRange'] = 'moderate'
    #     elif price <= bounds['expensive']:
    #         df.loc[index, 'PriceRange'] = 'expensive'
    #     else:
    #         df.loc[index, 'PriceRange'] = 'v_expensive'
    return df

def main():
    apdf = pd.read_csv("./finalProj/avoPrices.csv")
    apdf.sort_values('AveragePrice', inplace=True)
    for region in apdf['region'].unique():
        apdf = classify_region(apdf, region)

    # print(apdf)
    # prices = pd.unique(apdf["AveragePrice"])
    # prices = np.sort(prices)
    # divisions = int(prices.size/5)
    # v_cheap = prices[:divisions]
    # cheap = prices[divisions:2*divisions]
    # moderate = prices[2*divisions:3*divisions]
    # expensive = prices[3*divisions:4*divisions]
    # v_expensive = prices[4*divisions:]
    #
    # apdf["PriceRange"] = ""
    # for index,rows in apdf.iterrows():
    #     price = rows["AveragePrice"]
    #     if np.isin(price,v_cheap):
    #         apdf.loc[index,"PriceRange"] = "v_cheap"
    #     elif np.isin(price, cheap):
    #         apdf.loc[index, "PriceRange"] = "cheap"
    #     elif np.isin(price, moderate):
    #         apdf.loc[index,"PriceRange"] = "moderate"
    #     elif np.isin(price, expensive):
    #         apdf.loc[index,"PriceRange"] = "expensive"
    #     elif np.isin(price, v_expensive):
    #         apdf.loc[index,"PriceRange"] = "v_expensive"
    #

    outfile = open("./finalProj/avoPricesCategor.csv", "w+")
    apdf.to_csv(outfile)

if __name__ == '__main__':
    main()
