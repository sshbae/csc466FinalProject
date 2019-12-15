import pandas as pd

def main():
    df = pd.read_csv("./finalProj/avo2015.csv")
    df['wage'] = df['region']
            
    data = ['Albany','Atlanta','BaltimoreWashington','Boise','Boston',
            'BuffaloRochester','California','Charlotte','Chicago','CincinnatiDayton',
            'Columbus','DallasFtWorth','Denver','Detroit','GrandRapids','GreatLakes',
            'HarrisburgScranton','HartfordSpringfield','Houston','Indianapolis',
            'Jacksonville','LasVegas','LosAngeles','Louisville','MiamiFtLauderdale',
            'Midsouth','Nashville','NewOrleansMobile','NewYork','Northeast',
            'NorthernNewEngland','Orlando','Philadelphia','PhoenixTucson',
            'Pittsburgh','Plains','Portland','RaleighGreensboro','RichmondNorfolk',
            'Roanoke','Sacramento','SanDiego','SanFrancisco','Seattle',
            'SouthCarolina','SouthCentral','Southeast','Spokane','StLouis','Syracuse',
            'Tampa','TotalUS','West','WestTexNewMexico']

    df = df[df.region != 'TotalUS']
   
    df.loc[df['region'] == 'Albany', 'wage'] = 8.75
    df.loc[df['region'] == 'Atlanta', 'wage'] = 7.25
    df.loc[df['region'] == 'BaltimoreWashington', 'wage'] = 9.50
    df.loc[df['region'] == 'Boise', 'wage'] = 7.25
    df.loc[df['region'] == 'Boston', 'wage'] = 9.00
    df.loc[df['region'] == 'BuffaloRochester', 'wage'] = 8.75
    df.loc[df['region'] == 'California', 'wage'] = 9.00
    df.loc[df['region'] == 'Charlotte', 'wage'] = 7.25
    df.loc[df['region'] == 'Chicago', 'wage'] = 8.25
    df.loc[df['region'] == 'CincinnatiDayton', 'wage'] = 7.75
    df.loc[df['region'] == 'Columbus', 'wage'] = 7.75
    df.loc[df['region'] == 'DallasFtWorth', 'wage'] = 7.25
    df.loc[df['region'] == 'Denver', 'wage'] = 8.25
    df.loc[df['region'] == 'Detroit', 'wage'] = 8.00
    df.loc[df['region'] == 'GrandRapids', 'wage'] = 8.00
    df.loc[df['region'] == 'GreatLakes', 'wage'] = 8.00
    df.loc[df['region'] == 'HarrisburgScranton', 'wage'] = 7.25
    df.loc[df['region'] == 'HartfordSpringfield', 'wage'] = 8.25
    df.loc[df['region'] == 'Houston', 'wage'] = 8.25
    df.loc[df['region'] == 'Indianapolis', 'wage'] = 7.25
    df.loc[df['region'] == 'Jacksonville', 'wage'] = 8.00
    df.loc[df['region'] == 'LasVegas', 'wage'] = 7.75
    df.loc[df['region'] == 'LosAngeles', 'wage'] = 9.00
    df.loc[df['region'] == 'Louisville', 'wage'] = 7.25
    df.loc[df['region'] == 'MiamiFtLauderdale', 'wage'] = 8.00
    df.loc[df['region'] == 'Midsouth', 'wage'] = 7.25
    df.loc[df['region'] == 'Nashville', 'wage'] = 7.25
    df.loc[df['region'] == 'NewOrleansMobile', 'wage'] = 7.25
    df.loc[df['region'] == 'NewYork', 'wage'] = 8.75
    df.loc[df['region'] == 'Northeast', 'wage'] = 7.50
    df.loc[df['region'] == 'NorthernNewEngland', 'wage'] = 7.50
    df.loc[df['region'] == 'Orlando', 'wage'] = 8.00
    df.loc[df['region'] == 'Philadelphia', 'wage'] = 7.25
    df.loc[df['region'] == 'PhoenixTucson', 'wage'] = 8.00
    df.loc[df['region'] == 'Pittsburgh', 'wage'] = 7.25
    df.loc[df['region'] == 'Plains', 'wage'] = 8.00
    df.loc[df['region'] == 'Portland', 'wage'] = 9.25
    df.loc[df['region'] == 'RaleighGreensboro', 'wage'] = 7.25
    df.loc[df['region'] == 'RichmondNorfolk', 'wage'] = 7.25
    df.loc[df['region'] == 'Roanoke', 'wage'] = 7.25
    df.loc[df['region'] == 'Sacramento', 'wage'] = 9.00
    df.loc[df['region'] == 'SanDiego', 'wage'] = 9.00
    df.loc[df['region'] == 'SanFrancisco', 'wage'] = 9.00
    df.loc[df['region'] == 'Seattle', 'wage'] = 9.50
    df.loc[df['region'] == 'SouthCarolina', 'wage'] = 7.25
    df.loc[df['region'] == 'SouthCentral', 'wage'] = 8.00
    df.loc[df['region'] == 'Southeast', 'wage'] = 8.00
    df.loc[df['region'] == 'Spokane', 'wage'] = 9.50
    df.loc[df['region'] == 'StLouis', 'wage'] = 7.75
    df.loc[df['region'] == 'Syracuse', 'wage'] = 8.75
    df.loc[df['region'] == 'Tampa', 'wage'] = 8.00
    df.loc[df['region'] == 'West', 'wage'] = 9.00
    df.loc[df['region'] == 'WestTexNewMexico', 'wage'] = 7.50

    df.to_csv(open("./finalProj/avo2015Fixed.csv", "w+"), index=False)

    df = pd.read_csv("./finalProj/avo2016.csv")
    df['wage'] = df['region']
    df = df[df.region != 'TotalUS']

    df.loc[df['region'] == 'Albany', 'wage'] = 9.00
    df.loc[df['region'] == 'Atlanta', 'wage'] = 7.25
    df.loc[df['region'] == 'BaltimoreWashington', 'wage'] = 9.50
    df.loc[df['region'] == 'Boise', 'wage'] = 7.25
    df.loc[df['region'] == 'Boston', 'wage'] = 10.00
    df.loc[df['region'] == 'BuffaloRochester', 'wage'] = 9.00
    df.loc[df['region'] == 'California', 'wage'] = 10.00
    df.loc[df['region'] == 'Charlotte', 'wage'] = 7.25
    df.loc[df['region'] == 'Chicago', 'wage'] = 8.25
    df.loc[df['region'] == 'CincinnatiDayton', 'wage'] = 7.75
    df.loc[df['region'] == 'Columbus', 'wage'] = 7.75
    df.loc[df['region'] == 'DallasFtWorth', 'wage'] = 7.25
    df.loc[df['region'] == 'Denver', 'wage'] = 8.50
    df.loc[df['region'] == 'Detroit', 'wage'] = 8.50
    df.loc[df['region'] == 'GrandRapids', 'wage'] = 8.50
    df.loc[df['region'] == 'GreatLakes', 'wage'] = 8.50
    df.loc[df['region'] == 'HarrisburgScranton', 'wage'] = 7.25
    df.loc[df['region'] == 'HartfordSpringfield', 'wage'] = 8.25
    df.loc[df['region'] == 'Houston', 'wage'] = 8.25
    df.loc[df['region'] == 'Indianapolis', 'wage'] = 7.25
    df.loc[df['region'] == 'Jacksonville', 'wage'] = 8.00
    df.loc[df['region'] == 'LasVegas', 'wage'] = 7.75
    df.loc[df['region'] == 'LosAngeles', 'wage'] = 9.00
    df.loc[df['region'] == 'Louisville', 'wage'] = 7.25
    df.loc[df['region'] == 'MiamiFtLauderdale', 'wage'] = 8.00
    df.loc[df['region'] == 'Midsouth', 'wage'] = 7.25
    df.loc[df['region'] == 'Nashville', 'wage'] = 7.25
    df.loc[df['region'] == 'NewOrleansMobile', 'wage'] = 7.25
    df.loc[df['region'] == 'NewYork', 'wage'] = 9.00
    df.loc[df['region'] == 'Northeast', 'wage'] = 7.50
    df.loc[df['region'] == 'NorthernNewEngland', 'wage'] = 7.50
    df.loc[df['region'] == 'Orlando', 'wage'] = 8.00
    df.loc[df['region'] == 'Philadelphia', 'wage'] = 7.25
    df.loc[df['region'] == 'PhoenixTucson', 'wage'] = 8.00
    df.loc[df['region'] == 'Pittsburgh', 'wage'] = 7.25
    df.loc[df['region'] == 'Plains', 'wage'] = 8.00
    df.loc[df['region'] == 'Portland', 'wage'] = 9.75
    df.loc[df['region'] == 'RaleighGreensboro', 'wage'] = 7.25
    df.loc[df['region'] == 'RichmondNorfolk', 'wage'] = 7.25
    df.loc[df['region'] == 'Roanoke', 'wage'] = 7.25
    df.loc[df['region'] == 'Sacramento', 'wage'] = 10.00
    df.loc[df['region'] == 'SanDiego', 'wage'] = 10.00
    df.loc[df['region'] == 'SanFrancisco', 'wage'] = 10.00
    df.loc[df['region'] == 'Seattle', 'wage'] = 9.50
    df.loc[df['region'] == 'SouthCarolina', 'wage'] = 7.25
    df.loc[df['region'] == 'SouthCentral', 'wage'] = 8.00
    df.loc[df['region'] == 'Southeast', 'wage'] = 8.00
    df.loc[df['region'] == 'Spokane', 'wage'] = 9.50
    df.loc[df['region'] == 'StLouis', 'wage'] = 7.75
    df.loc[df['region'] == 'Syracuse', 'wage'] = 9.00
    df.loc[df['region'] == 'Tampa', 'wage'] = 8.00
    df.loc[df['region'] == 'West', 'wage'] = 10.00
    df.loc[df['region'] == 'WestTexNewMexico', 'wage'] = 7.50

    df.to_csv(open("./finalProj/avo2016Fixed.csv", "w+"), index=False)

    df = pd.read_csv("./finalProj/avo2017.csv")
    df['wage'] = df['region']
    df = df[df.region != 'TotalUS']

    df.loc[df['region'] == 'Albany', 'wage'] = 9.75
    df.loc[df['region'] == 'Atlanta', 'wage'] = 7.25
    df.loc[df['region'] == 'BaltimoreWashington', 'wage'] = 11.00
    df.loc[df['region'] == 'Boise', 'wage'] = 7.25
    df.loc[df['region'] == 'Boston', 'wage'] = 11.00
    df.loc[df['region'] == 'BuffaloRochester', 'wage'] = 9.75
    df.loc[df['region'] == 'California', 'wage'] = 10.00
    df.loc[df['region'] == 'Charlotte', 'wage'] = 7.25
    df.loc[df['region'] == 'Chicago', 'wage'] = 8.25
    df.loc[df['region'] == 'CincinnatiDayton', 'wage'] = 8.00
    df.loc[df['region'] == 'Columbus', 'wage'] = 8.00
    df.loc[df['region'] == 'DallasFtWorth', 'wage'] = 7.25
    df.loc[df['region'] == 'Denver', 'wage'] = 9.50
    df.loc[df['region'] == 'Detroit', 'wage'] = 9.00
    df.loc[df['region'] == 'GrandRapids', 'wage'] = 9.00
    df.loc[df['region'] == 'GreatLakes', 'wage'] = 9.00
    df.loc[df['region'] == 'HarrisburgScranton', 'wage'] = 7.25
    df.loc[df['region'] == 'HartfordSpringfield', 'wage'] = 8.25
    df.loc[df['region'] == 'Houston', 'wage'] = 8.25
    df.loc[df['region'] == 'Indianapolis', 'wage'] = 7.25
    df.loc[df['region'] == 'Jacksonville', 'wage'] = 8.00
    df.loc[df['region'] == 'LasVegas', 'wage'] = 7.75
    df.loc[df['region'] == 'LosAngeles', 'wage'] = 10.00
    df.loc[df['region'] == 'Louisville', 'wage'] = 7.25
    df.loc[df['region'] == 'MiamiFtLauderdale', 'wage'] = 8.00
    df.loc[df['region'] == 'Midsouth', 'wage'] = 7.25
    df.loc[df['region'] == 'Nashville', 'wage'] = 7.25
    df.loc[df['region'] == 'NewOrleansMobile', 'wage'] = 7.25
    df.loc[df['region'] == 'NewYork', 'wage'] = 9.75
    df.loc[df['region'] == 'Northeast', 'wage'] = 9.00
    df.loc[df['region'] == 'NorthernNewEngland', 'wage'] = 9.00
    df.loc[df['region'] == 'Orlando', 'wage'] = 8.00
    df.loc[df['region'] == 'Philadelphia', 'wage'] = 7.25
    df.loc[df['region'] == 'PhoenixTucson', 'wage'] = 10.00
    df.loc[df['region'] == 'Pittsburgh', 'wage'] = 7.25
    df.loc[df['region'] == 'Plains', 'wage'] = 8.00
    df.loc[df['region'] == 'Portland', 'wage'] = 9.75
    df.loc[df['region'] == 'RaleighGreensboro', 'wage'] = 7.25
    df.loc[df['region'] == 'RichmondNorfolk', 'wage'] = 7.25
    df.loc[df['region'] == 'Roanoke', 'wage'] = 7.25
    df.loc[df['region'] == 'Sacramento', 'wage'] = 10.00
    df.loc[df['region'] == 'SanDiego', 'wage'] = 10.00
    df.loc[df['region'] == 'SanFrancisco', 'wage'] = 10.00
    df.loc[df['region'] == 'Seattle', 'wage'] = 11.00
    df.loc[df['region'] == 'SouthCarolina', 'wage'] = 7.25
    df.loc[df['region'] == 'SouthCentral', 'wage'] = 8.00
    df.loc[df['region'] == 'Southeast', 'wage'] = 8.00
    df.loc[df['region'] == 'Spokane', 'wage'] = 11.00
    df.loc[df['region'] == 'StLouis', 'wage'] = 7.75
    df.loc[df['region'] == 'Syracuse', 'wage'] = 9.75
    df.loc[df['region'] == 'Tampa', 'wage'] = 8.00
    df.loc[df['region'] == 'West', 'wage'] = 10.00
    df.loc[df['region'] == 'WestTexNewMexico', 'wage'] = 7.50

    df.to_csv(open("./finalProj/avo2017Fixed.csv", "w+"), index=False)

    df = pd.read_csv("./finalProj/avo2018.csv")
    df['wage'] = df['region']
    df = df[df.region != 'TotalUS']

    df.loc[df['region'] == 'Albany', 'wage'] = 10.50
    df.loc[df['region'] == 'Atlanta', 'wage'] = 7.25
    df.loc[df['region'] == 'BaltimoreWashington', 'wage'] = 11.50
    df.loc[df['region'] == 'Boise', 'wage'] = 7.25
    df.loc[df['region'] == 'Boston', 'wage'] = 11.00
    df.loc[df['region'] == 'BuffaloRochester', 'wage'] = 10.50
    df.loc[df['region'] == 'California', 'wage'] = 11.00
    df.loc[df['region'] == 'Charlotte', 'wage'] = 7.25
    df.loc[df['region'] == 'Chicago', 'wage'] = 8.25
    df.loc[df['region'] == 'CincinnatiDayton', 'wage'] = 8.50
    df.loc[df['region'] == 'Columbus', 'wage'] = 8.50
    df.loc[df['region'] == 'DallasFtWorth', 'wage'] = 7.25
    df.loc[df['region'] == 'Denver', 'wage'] = 10.00
    df.loc[df['region'] == 'Detroit', 'wage'] = 9.25
    df.loc[df['region'] == 'GrandRapids', 'wage'] = 9.25
    df.loc[df['region'] == 'GreatLakes', 'wage'] = 9.25
    df.loc[df['region'] == 'HarrisburgScranton', 'wage'] = 7.25
    df.loc[df['region'] == 'HartfordSpringfield', 'wage'] = 8.25
    df.loc[df['region'] == 'Houston', 'wage'] = 8.25
    df.loc[df['region'] == 'Indianapolis', 'wage'] = 7.25
    df.loc[df['region'] == 'Jacksonville', 'wage'] = 8.25
    df.loc[df['region'] == 'LasVegas', 'wage'] = 7.75
    df.loc[df['region'] == 'LosAngeles', 'wage'] = 11.00
    df.loc[df['region'] == 'Louisville', 'wage'] = 7.25
    df.loc[df['region'] == 'MiamiFtLauderdale', 'wage'] = 8.25
    df.loc[df['region'] == 'Midsouth', 'wage'] = 7.25
    df.loc[df['region'] == 'Nashville', 'wage'] = 7.25
    df.loc[df['region'] == 'NewOrleansMobile', 'wage'] = 7.25
    df.loc[df['region'] == 'NewYork', 'wage'] = 10.50
    df.loc[df['region'] == 'Northeast', 'wage'] = 10.00
    df.loc[df['region'] == 'NorthernNewEngland', 'wage'] = 10.00
    df.loc[df['region'] == 'Orlando', 'wage'] = 8.25
    df.loc[df['region'] == 'Philadelphia', 'wage'] = 7.25
    df.loc[df['region'] == 'PhoenixTucson', 'wage'] = 10.50
    df.loc[df['region'] == 'Pittsburgh', 'wage'] = 7.25
    df.loc[df['region'] == 'Plains', 'wage'] = 8.00
    df.loc[df['region'] == 'Portland', 'wage'] = 10.75
    df.loc[df['region'] == 'RaleighGreensboro', 'wage'] = 7.25
    df.loc[df['region'] == 'RichmondNorfolk', 'wage'] = 7.25
    df.loc[df['region'] == 'Roanoke', 'wage'] = 7.25
    df.loc[df['region'] == 'Sacramento', 'wage'] = 11.00
    df.loc[df['region'] == 'SanDiego', 'wage'] = 11.00
    df.loc[df['region'] == 'SanFrancisco', 'wage'] = 11.00
    df.loc[df['region'] == 'Seattle', 'wage'] = 11.50
    df.loc[df['region'] == 'SouthCarolina', 'wage'] = 7.25
    df.loc[df['region'] == 'SouthCentral', 'wage'] = 8.00
    df.loc[df['region'] == 'Southeast', 'wage'] = 8.25
    df.loc[df['region'] == 'Spokane', 'wage'] = 11.50
    df.loc[df['region'] == 'StLouis', 'wage'] = 7.75
    df.loc[df['region'] == 'Syracuse', 'wage'] = 10.50
    df.loc[df['region'] == 'Tampa', 'wage'] = 8.25
    df.loc[df['region'] == 'West', 'wage'] = 11.00
    df.loc[df['region'] == 'WestTexNewMexico', 'wage'] = 7.50

    df.to_csv(open("./finalProj/avo2018Fixed.csv", "w+"), index=False)

if __name__ == '__main__':
    main()