# lets get the ariane output into a nice formate for easy timing analysis of each water mass
import datetime as dt
import xarray as xr
import pandas as pd
import numpy as np

# upwelling runs
upendday = [dt.datetime(2014, 9, 3), 
            dt.datetime(2015, 9, 5), dt.datetime(2016, 9, 13), 
            dt.datetime(2017, 10, 12), dt.datetime(2018, 9, 6), 
            dt.datetime(2019, 11, 5),dt.datetime(2020, 10, 17),
            dt.datetime(2021, 9, 22), dt.datetime(2022, 10, 15), 
            dt.datetime(2023, 9, 22)]

# downwelling runs
dwendday = [dt.datetime(2014, 3, 6), dt.datetime(2015, 2, 12), dt.datetime(2016, 3, 19),dt.datetime(2017, 4, 19), dt.datetime(2018, 2, 1),
            dt.datetime(2019, 4, 6), dt.datetime(2020, 1, 27),dt.datetime(2021, 2, 2), dt.datetime(2022, 1, 25),dt.datetime(2023, 4, 19)]

# spring runs
spendday = [dt.datetime(2014, 3, 25), 
            dt.datetime(2015, 4, 13), dt.datetime(2016, 4, 7), 
            dt.datetime(2017, 5, 8), dt.datetime(2018, 4, 30), 
            dt.datetime(2019, 4, 25),dt.datetime(2020, 2, 15),
            dt.datetime(2021, 3, 18), dt.datetime(2022, 6, 11), 
            dt.datetime(2023, 5, 8)]

# fall runs
flendday = [dt.datetime(2014, 9, 21), 
            dt.datetime(2015, 10, 21), dt.datetime(2016, 10, 2), 
            dt.datetime(2017, 11, 1), dt.datetime(2018, 10, 24), 
            dt.datetime(2019, 12, 4),dt.datetime(2020, 11, 11),
            dt.datetime(2021, 10, 6), dt.datetime(2022, 10,24), 
            dt.datetime(2023, 10, 13)]

# make one big csv file with section (my definition), transport, age, period (upwelling, downwelling, spring, fall)

def get_tracers_all(enday, period):
    #function to get the temperature, and salinity + section info for each parcel
    #south div is to set up boolean for the three south water masses, 1=CUC, 2=south shelf/davidson, 3=Columbia, 0=NA 

    section = np.array([])
    depth = np.array([])
    trans = np.array([])
    salt = np.array([])
    age = np.array([], dtype='timedelta64[ns]')

    st_files = ['/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/{}_cas7/S_T/{:%Y%m%d}/ariane_positions_quantitative.nc'.format(period,day) for day in enday]

    for i in range(len(enday)):
        s_t = xr.open_dataset(st_files[i])

        tides = ((abs(s_t.init_t-s_t.final_t) > 24) & ~np.isnan(s_t.final_section)) # boolean to ignore tidally pumped parcels and lost parcels

        # not removing lost parcels for now bc we want to quantify these

        section = np.append(section,s_t.final_section[tides])
        trans = np.append(trans,s_t.final_transp[tides])
        depth = np.append(depth,s_t.final_depth[tides])
        salt = np.append(salt,s_t.final_salt[tides])
        age = np.append(age,s_t.final_age[tides])
        age = pd.to_timedelta(age)


    d = {'transport':trans,'age':age}
    df = pd.DataFrame(d)

    # add period
    df['period'] = period

    # split into water masses
    bdy_loo = 0
    bdy_sou = 2
    bdy_off = 3
    bdy_nor = 4
    saltdiv = 32
    sdiv = 33.5

    df['wm'] = np.nan
    df.wm[(section==bdy_sou) & (salt >= sdiv)] = 'cuc'
    df.wm[(section==bdy_off) & (depth > 120)] = 'off_d'
    df.wm[(section==bdy_off) & (depth <=120)] = 'off_s'
    df.wm[(section==bdy_sou) & (salt >= saltdiv) & (salt < sdiv)] = 'south'
    df.wm[(section==bdy_nor)] = 'north'
    df.wm[(section==bdy_sou) & (salt < saltdiv)] = 'fresh'
    df.wm[(section==bdy_loo)] = 'loop' # already removed the tides earlier

    return df

dw = get_tracers_all(dwendday, "down")
print("down done")
spring = get_tracers_all(spendday, "spring")
print("spring done")
up = get_tracers_all(upendday, "up")
print("up done")
fall = get_tracers_all(flendday, "fall")
print("fall done")

all = pd.concat([dw,spring,up,fall])

all.to_csv('/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/summary_files/TimingData.csv')
print('done done')