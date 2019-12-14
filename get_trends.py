# http://www.apache.org/licenses/LICENSE-2.0
# get_trends.py >> trends_avocado.csv, trends_avocado_toast.csv
from pytrends.request import TrendReq
import os
import pandas as pd
from typing import Dict

pytrends = TrendReq(hl='en-US', tz=480, timeout=(10, 25), retries=2, backoff_factor=0.1)

STATES = ['US-AL', 'US-AK', 'US-AZ', 'US-AR', 'US-CA', 'US-CO', 'US-CT', 'US-DE', 'US-DC', 'US-FL', 'US-GA',
          'US-HI', 'US-ID', 'US-IL', 'US-IN', 'US-IA', 'US-KS', 'US-KY', 'US-LA', 'US-ME', 'US-MD', 'US-MA', 'US-MI',
          'US-MN', 'US-MS', 'US-MO', 'US-MT', 'US-NE', 'US-NV', 'US-NH', 'US-NJ', 'US-NM', 'US-NY', 'US-NC', 'US-ND',
          'US-OH', 'US-OK', 'US-OR', 'US-PA', 'US-RI', 'US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VT', 'US-VA',
          'US-WA', 'US-WV', 'US-WI', 'US-WY']

CITIES = []

TERMS = [['avocado'], ['avocado toast']]

if __name__ == '__main__':

    if not os.path.exists('./out'):
        os.mkdir('./out')

    for term in TERMS:
        res_df = pd.DataFrame()
        t = term[0].replace(' ', '_')
        pytrends.build_payload(term, geo='US', timeframe='2004-01-01 2019-11-30')
        data2 = pytrends.interest_by_region(resolution='CITY')

        for state in STATES:
            fn = f'./out/{state}_{t}.csv'

            if not os.path.exists(fn):
                pytrends.build_payload(term, geo=state, timeframe='2004-01-01 2019-11-30')
                data = pytrends.interest_over_time()
                if 'isPartial' in data.columns:
                    data = data.drop('isPartial', axis=1)
                data = data.T
                if len(data) > 0:
                    data.index = [state]
                    data.index.name = 'state'
                res_df = res_df.append(data, sort=False)
                data.to_csv(fn)
            else:
                data = pd.read_csv(fn, index_col=0)
                res_df = res_df.append(data, sort=False)

        res_df.to_csv(f'./out/trends_{t}.csv')
