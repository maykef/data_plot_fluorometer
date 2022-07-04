import pandas as pd


apps = pd.read_csv('Basil_Trial/03-07-22/03-07-2022_05_00_peaks_valleys.csv')

apps_1 = apps[['Peaks']]

apps_2 = apps[['True Valleys']]

apps_3 = apps_1.dropna()

apps_4 = apps_2.dropna()

apps_4['Peaks'] = apps_3['Peaks'].values

pd.DataFrame(apps_4).to_csv('Basil_Trial/03-07-22/03-07-2022_05_00_peaks_valleys_2.csv', index=False)

print(apps_4)