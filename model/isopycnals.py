# make csv of each water parcel, its WM source, transport, and isopycnal that it lies on at the beginning of its trajectory 
import xarray as xr
import numpy as np
import pandas as pd
import gsw

def isopycnaldata(data_list):
    # for the purpose of seeing which isopycnals get in, only thinking about pacific sources (ie. not return flow)

    trans = np.array([])
    section = np.array([])
    salt_final = np.array([])
    depth_final = np.array([])
    temp_final = np.array([])
    salt_init = np.array([])
    depth_init = np.array([])
    temp_init = np.array([])

    for datapath in data_list:
        data = xr.open_dataset(datapath)
        rebool = (~np.isnan(data.final_section) & (data.final_section != 0))
        salt_final = np.append(salt_final,data.final_salt[rebool].values)
        temp_final = np.append(temp_final,data.final_temp[rebool].values)
        depth_final = np.append(depth_final,data.final_depth[rebool].values)
        salt_init = np.append(salt_init,data.init_salt[rebool].values)
        temp_init = np.append(temp_init,data.init_temp[rebool].values)
        depth_init = np.append(depth_init,data.init_depth[rebool].values)
        section = np.append(section,data.final_section[rebool].values)
        trans = np.append(trans,data.final_transp[rebool].values)

    d = {'transport':trans,'section':section,'Fsalt':salt_final,'Ftemp':temp_final,'Fdepth':depth_final,'Isalt':salt_init,'Itemp':temp_init,'Idepth':depth_init}
    df = pd.DataFrame(d)

    return df

file_list = ['/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/results/down_cas7/S_T/20140306/ariane_positions_quantitative.nc',
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

data = isopycnaldata(file_list)

data['Iisopycnal'] = gsw.density.sigma0(data.Isalt.values,gsw.conversions.CT_from_t(data.Isalt.values,data.Itemp.values,data.Idepth.values))
data['Fisopycnal'] = gsw.density.sigma0(data.Fsalt.values,gsw.conversions.CT_from_t(data.Fsalt.values,data.Ftemp.values,data.Fdepth.values))


# assign each line to a particular water mass
data['wm'] = 'none'

# boundary definitions
bdy_loo = 0
bdy_sou = 2
bdy_off = 3
bdy_nor = 4
saltdiv = 32
sdiv = 33.5

for i in range(len(data)):
    if (data.section[i]==bdy_sou) and (data.Fsalt[i] >= sdiv):
        data.loc[i, "wm"] = 'cuc'
    elif (data.section[i]==bdy_off) & (data.Fdepth[i] > 120):
        data.loc[i, "wm"] = 'offshore deep'
    elif (data.section[i]==bdy_off) & (data.Fdepth[i] <=120):
        data.loc[i, "wm"] = 'offshore surface'
    elif (data.section[i]==bdy_nor):
        data.loc[i, "wm"] = 'north'
    elif (data.section[i]==bdy_sou) & (data.Fsalt[i] >= saltdiv) & (data.Fsalt[i] < sdiv):
        data.loc[i, "wm"] = 'south'
    elif ((data.section[i]==bdy_sou) & (data.Fsalt[i] < saltdiv)):
        data.loc[i, "wm"] =  'fresh'

data.to_csv('/ocean/rbeutel/MOAD/biogeo_paper/FRDR/model/ariane/summary_files/isopycnals.csv')