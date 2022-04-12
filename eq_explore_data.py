import json
from textwrap import indent

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent=4)
all_eq_dics = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dics:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)




print(len(all_eq_dics))
print(mags[:10])
print(lons[:5])
print(lats[:5])