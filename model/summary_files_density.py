import argparse
import xarray as xr
import pandas as pd
import numpy as np
import gsw

# allow file selection to be input in the command line
# example run: python3 summary_files.py 20171012 up
parser = argparse.ArgumentParser(description='Get bins')
parser.add_argument('iso_bins', type=float, nargs="+",
                    help='isopycnal bins')
args = parser.parse_args()

isobins = args.iso_bins

# bring in files
st_files = ['/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20140306/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20150212/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20160319/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20170419/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20180201/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20190406/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20200127/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20210202/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20220125/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20230419/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20140903/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20150905/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20160913/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20171012/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20180906/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20191105/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20201017/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20210922/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20221015/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/S_T/20230922/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20140921/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20151021/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20161002/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20171101/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20181024/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20191204/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20201111/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20211006/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20221024/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/S_T/20231013/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20140325/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20150413/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20160407/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20170508/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20180430/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20190425/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20200215/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20210318/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20220611/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/S_T/20230508/ariane_positions_quantitative.nc'
             ]
st=xr.open_mfdataset(st_files, combine="nested", concat_dim="ntraj", chunks="auto", compat="no_conflicts",)

dn_files = ['/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20140306/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20150212/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20160319/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20170419/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20180201/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20190406/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20200127/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20210202/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20220125/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/DO_NO3/20230419/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20140903/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20150905/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20160913/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20171012/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20180906/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20191105/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20201017/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20210922/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20221015/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/DO_NO3/20230922/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20140921/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20151021/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20161002/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20171101/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20181024/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20191204/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20201111/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20211006/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20221024/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/DO_NO3/20231013/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20140325/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20150413/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20160407/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20170508/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20180430/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20190425/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20200215/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20210318/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20220611/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/DO_NO3/20230508/ariane_positions_quantitative.nc'
             ]
dn=xr.open_mfdataset(dn_files, combine="nested", concat_dim="ntraj", chunks="auto", compat="no_conflicts",)

td_files = ['/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20140306/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20150212/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20160319/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20170419/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20180201/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20190406/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20200127/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20210202/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20220125/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/TA_DIC/20230419/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20140903/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20150905/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20160913/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20171012/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20180906/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20191105/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20201017/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20210922/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20221015/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/up_cas7/TA_DIC/20230922/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20140921/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20151021/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20161002/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20171101/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20181024/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20191204/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20201111/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20211006/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20221024/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/fall_cas7/TA_DIC/20231013/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20140325/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20150413/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20160407/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20170508/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20180430/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20190425/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20200215/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20210318/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20220611/ariane_positions_quantitative.nc',
             '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/spring_cas7/TA_DIC/20230508/ariane_positions_quantitative.nc'
             ]
td=xr.open_mfdataset(td_files, combine="nested", concat_dim="ntraj", chunks="auto", compat="no_conflicts",)

# make array of final iso and init iso
final_iso = gsw.density.sigma0(st.final_salt.values,gsw.conversions.CT_from_t(st.final_salt.values,st.final_temp.values,st.final_depth.values))
print('final range = {}-{}'.format(np.min(final_iso),np.max(final_iso)))
init_iso = gsw.density.sigma0(st.init_salt.values,gsw.conversions.CT_from_t(st.init_salt.values,st.init_temp.values,st.init_depth.values))
print('init range = {}-{}'.format(np.min(init_iso),np.max(init_iso)))

# boundary definitions
bdy_loo = 0
bdy_sou = 2
bdy_off = 3
bdy_nor = 4
saltdiv = 32
sdiv = 33.5


# make dictionary of transport and tracer concentrations of each water parcel within a specified region within a specified isopycnal range
# the region is based on the boolean input into the function defined here
## region options are salish, cuc, offshore deep, offshore surface, north, south, fresh, loop
for i in range(len(isobins)-1):

    d = {'regions':['salish', 'cuc', 'offshore deep', 'offshore surface', 'north', 'south', 'fresh','loop'],
        'transport':np.zeros(8),'salt':np.zeros(8),'temp':np.zeros(8),'DO':np.zeros(8),
        'NO3':np.zeros(8),'TA':np.zeros(8),'DIC':np.zeros(8),'[TA-DIC]':np.zeros(8)}
    df = pd.DataFrame(d)

    # total
    booo = ((abs(st.init_t-st.final_t) > 24) & ~np.isnan(st.final_section) & (final_iso>=isobins[i]) & (final_iso<isobins[i+1])) # total between the iso range.. but not including tidal pumping or lost particles
    transport = st.init_transp[booo].values
    df.loc[0,'transport'] = np.sum(transport)
    if np.sum(transport)>0:
        df.loc[0,'salt'] = np.average(st.init_salt[booo].values,weights=transport)
        df.loc[0,'temp'] = np.average(st.init_temp[booo].values,weights=transport)
        df.loc[0,'NO3'] = np.average(dn.init_salt[booo].values,weights=transport)
        df.loc[0,'DO'] = np.average(dn.init_temp[booo].values,weights=transport)
        # ta, dic converted to the proper units for init values
        dens = st.init_dens.values
        ta = td.init_temp.values/(dens+1000)*1000
        dic = td.init_salt.values/(dens+1000)*1000 
        df.loc[0,'DIC'] = np.average(dic[booo],weights=transport)
        df.loc[0,'TA'] = np.average(ta[booo],weights=transport)
        df.loc[0,'[TA-DIC]'] = np.average(ta[booo]-dic[booo],weights=transport)
    else:
        df.loc[0,'salt'] = np.nan
        df.loc[0,'temp'] = np.nan
        df.loc[0,'NO3'] = np.nan
        df.loc[0,'DO'] = np.nan
        df.loc[0,'DIC'] = np.nan
        df.loc[0,'TA'] =np.nan
        df.loc[0,'[TA-DIC]'] =np.nan

    # for the rest of the water masses we use final properties, because we care about the properties of the water masses at they enter the region (before mixing with the other water masses)
    # ta, dic converted to the proper units for init values
    dens = st.final_dens.values
    ta = td.final_temp.values/(dens+1000)*1000
    dic = td.final_salt.values/(dens+1000)*1000 

    # loop 7
    booo = ((abs(st.init_t-st.final_t) > 24) & (st.final_section==bdy_loo) & (final_iso>=isobins[i]) & (final_iso<isobins[i+1]))
    transport = st.init_transp[booo].values
    df.loc[7,'transport'] = np.sum(transport)
    if np.sum(transport)>0:
        df.loc[7,'salt'] = np.average(st.final_salt[booo].values,weights=transport)
        df.loc[7,'temp'] = np.average(st.final_temp[booo].values,weights=transport)
        df.loc[7,'NO3'] = np.average(dn.final_salt[booo].values,weights=transport)
        df.loc[7,'DO'] = np.average(dn.final_temp[booo].values,weights=transport)
        df.loc[7,'DIC'] = np.average(dic[booo],weights=transport)
        df.loc[7,'TA'] = np.average(ta[booo],weights=transport)
        df.loc[7,'[TA-DIC]'] = np.average(ta[booo]-dic[booo],weights=transport)
    else:
        df.loc[7,'salt'] = np.nan
        df.loc[7,'temp'] = np.nan
        df.loc[7,'NO3'] = np.nan
        df.loc[7,'DO'] = np.nan
        df.loc[7,'DIC'] = np.nan
        df.loc[7,'TA'] =np.nan
        df.loc[7,'[TA-DIC]'] =np.nan

    # fresh 6
    booo = ((st.final_salt < saltdiv) & (st.final_section==bdy_sou)& (final_iso>=isobins[i]) & (final_iso<isobins[i+1]))
    transport = st.init_transp[booo].values
    df.loc[6,'transport'] = np.sum(transport)
    if np.sum(transport)>0:
        df.loc[6,'salt'] = np.average(st.final_salt[booo].values,weights=transport)
        df.loc[6,'temp'] = np.average(st.final_temp[booo].values,weights=transport)
        df.loc[6,'NO3'] = np.average(dn.final_salt[booo].values,weights=transport)
        df.loc[6,'DO'] = np.average(dn.final_temp[booo].values,weights=transport)
        df.loc[6,'DIC'] = np.average(dic[booo],weights=transport)
        df.loc[6,'TA'] = np.average(ta[booo],weights=transport)
        df.loc[6,'[TA-DIC]'] = np.average(ta[booo]-dic[booo],weights=transport)
    else:
        df.loc[6,'salt'] = np.nan
        df.loc[6,'temp'] = np.nan
        df.loc[6,'NO3'] = np.nan
        df.loc[6,'DO'] = np.nan
        df.loc[6,'DIC'] = np.nan
        df.loc[6,'TA'] =np.nan
        df.loc[6,'[TA-DIC]'] =np.nan

    # south 5
    booo = ((st.final_salt>=saltdiv) & (st.final_salt < sdiv) & (st.final_section==bdy_sou)& (final_iso>=isobins[i]) & (final_iso<isobins[i+1]))
    transport = st.init_transp[booo].values
    df.loc[5,'transport'] = np.sum(transport)
    if np.sum(transport)>0:
        df.loc[5,'salt'] = np.average(st.final_salt[booo].values,weights=transport)
        df.loc[5,'temp'] = np.average(st.final_temp[booo].values,weights=transport)
        df.loc[5,'NO3'] = np.average(dn.final_salt[booo].values,weights=transport)
        df.loc[5,'DO'] = np.average(dn.final_temp[booo].values,weights=transport)
        df.loc[5,'DIC'] = np.average(dic[booo],weights=transport)
        df.loc[5,'TA'] = np.average(ta[booo],weights=transport)
        df.loc[5,'[TA-DIC]'] = np.average(ta[booo]-dic[booo],weights=transport)
    else:
        df.loc[5,'salt'] = np.nan
        df.loc[5,'temp'] = np.nan
        df.loc[5,'NO3'] = np.nan
        df.loc[5,'DO'] = np.nan
        df.loc[5,'DIC'] = np.nan
        df.loc[5,'TA'] =np.nan
        df.loc[5,'[TA-DIC]'] =np.nan


    # cuc 1
    booo = ((st.final_salt>=sdiv) & (st.final_section==bdy_sou)& (final_iso>=isobins[i]) & (final_iso<isobins[i+1]))
    transport = st.init_transp[booo].values
    df.loc[1,'transport'] = np.sum(transport)
    if np.sum(transport)>0:
        df.loc[1,'salt'] = np.average(st.final_salt[booo].values,weights=transport)
        df.loc[1,'temp'] = np.average(st.final_temp[booo].values,weights=transport)
        df.loc[1,'NO3'] = np.average(dn.final_salt[booo].values,weights=transport)
        df.loc[1,'DO'] = np.average(dn.final_temp[booo].values,weights=transport)
        df.loc[1,'DIC'] = np.average(dic[booo],weights=transport)
        df.loc[1,'TA'] = np.average(ta[booo],weights=transport)
        df.loc[1,'[TA-DIC]'] = np.average(ta[booo]-dic[booo],weights=transport)
    else:
        df.loc[1,'salt'] = np.nan
        df.loc[1,'temp'] = np.nan
        df.loc[1,'NO3'] = np.nan
        df.loc[1,'DO'] = np.nan
        df.loc[1,'DIC'] = np.nan
        df.loc[1,'TA'] =np.nan
        df.loc[1,'[TA-DIC]'] =np.nan


    # off_d 2
    booo = ((st.final_depth>120) & (st.final_section==bdy_off)& (final_iso>=isobins[i]) & (final_iso<isobins[i+1]))
    transport = st.init_transp[booo].values
    df.loc[2,'transport'] = np.sum(transport)
    if np.sum(transport)>0:
        df.loc[2,'salt'] = np.average(st.final_salt[booo].values,weights=transport)
        df.loc[2,'temp'] = np.average(st.final_temp[booo].values,weights=transport)
        df.loc[2,'NO3'] = np.average(dn.final_salt[booo].values,weights=transport)
        df.loc[2,'DO'] = np.average(dn.final_temp[booo].values,weights=transport)
        df.loc[2,'DIC'] = np.average(dic[booo],weights=transport)
        df.loc[2,'TA'] = np.average(ta[booo],weights=transport)
        df.loc[2,'[TA-DIC]'] = np.average(ta[booo]-dic[booo],weights=transport)
    else:
        df.loc[2,'salt'] = np.nan
        df.loc[2,'temp'] = np.nan
        df.loc[2,'NO3'] = np.nan
        df.loc[2,'DO'] = np.nan
        df.loc[2,'DIC'] = np.nan
        df.loc[2,'TA'] =np.nan
        df.loc[2,'[TA-DIC]'] =np.nan


    # off_s 3
    booo = ((st.final_depth<=120) & (st.final_section==bdy_off)& (final_iso>=isobins[i]) & (final_iso<isobins[i+1]))
    transport = st.init_transp[booo].values
    df.loc[3,'transport'] = np.sum(transport)
    if np.sum(transport)>0:
        df.loc[3,'salt'] = np.average(st.final_salt[booo].values,weights=transport)
        df.loc[3,'temp'] = np.average(st.final_temp[booo].values,weights=transport)
        df.loc[3,'NO3'] = np.average(dn.final_salt[booo].values,weights=transport)
        df.loc[3,'DO'] = np.average(dn.final_temp[booo].values,weights=transport)
        df.loc[3,'DIC'] = np.average(dic[booo],weights=transport)
        df.loc[3,'TA'] = np.average(ta[booo],weights=transport)
        df.loc[3,'[TA-DIC]'] = np.average(ta[booo]-dic[booo],weights=transport)
    else:
        df.loc[3,'salt'] = np.nan
        df.loc[3,'temp'] = np.nan
        df.loc[3,'NO3'] = np.nan
        df.loc[3,'DO'] = np.nan
        df.loc[3,'DIC'] = np.nan
        df.loc[3,'TA'] =np.nan
        df.loc[3,'[TA-DIC]'] =np.nan

    # north 4
    booo = ((st.final_section==bdy_nor)& (final_iso>=isobins[i]) & (final_iso<isobins[i+1]))
    transport = st.init_transp[booo].values
    df.loc[4,'transport'] = np.sum(transport)
    if np.sum(transport)>0:
        df.loc[4,'salt'] = np.average(st.final_salt[booo].values,weights=transport)
        df.loc[4,'temp'] = np.average(st.final_temp[booo].values,weights=transport)
        df.loc[4,'NO3'] = np.average(dn.final_salt[booo].values,weights=transport)
        df.loc[4,'DO'] = np.average(dn.final_temp[booo].values,weights=transport)
        df.loc[4,'DIC'] = np.average(dic[booo],weights=transport)
        df.loc[4,'TA'] = np.average(ta[booo],weights=transport)
        df.loc[4,'[TA-DIC]'] = np.average(ta[booo]-dic[booo],weights=transport)
    else:
        df.loc[4,'salt'] = np.nan
        df.loc[4,'temp'] = np.nan
        df.loc[4,'NO3'] = np.nan
        df.loc[4,'DO'] = np.nan
        df.loc[4,'DIC'] = np.nan
        df.loc[4,'TA'] =np.nan
        df.loc[4,'[TA-DIC]'] =np.nan

    # save the file
    filename = '/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/summary_files/isocombo_{}_{}.csv'.format(isobins[i],isobins[i+1])
    df.to_csv(filename)
    print(filename)