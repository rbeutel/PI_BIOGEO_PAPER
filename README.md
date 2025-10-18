# PI_BIOGEO_PAPER
Author: Becca Beutel  
Last Updated: 2025-10-03

## 1. Overview
This repository contains Jupyter notebooks and Python scripts for processing and analyzing simulation output and observations from the northern California Current System. The results of these analyses are summarized in Beutel et al. (2025) — “Water property variability into a semi-enclosed sea dominated by dynamics, modulated by properties.”  
The datasets referenced can be accessed at [https://doi.org/10.20383/103.01339](https://doi.org/10.20383/103.01339).

## 2. Repository Structure
- /model/ Scripts and notebooks for working with simulation output.  
- /observations/ Script and notebooks for downloading, processing, and summarizing observational data.  

## 3. File Descriptions

### /model

| Folder/File | Description |
|-------------|-------------|
| `/model/density.ipynb` | Density of inflow into JdF from the different source waters, and variability attribution in isopycnal space. Figs. 4, 9, S9. |
| `/model/isopycnals.py` | Organizes each water parcel physical property data for use in `/model/density.ipynb`. |
| `/model/map.ipynb` | Map of the LiveOcean and analysis domain. Fig. 1. |
| `/model/quant_attribution_Flux.ipynb` | Drivers of interannual variability calculation and plotting. Figs. 5, 8, S6, S7, S10–S12. |
| `/model/quant_dynamics.ipynb` | Daily mean transport from each source over the 10 years of analysis. Fig. 3. |
| `/model/quant_properties.ipynb` | Interannual and seasonal variability in the properties of each source water. Fig. 7. |
| `/model/quant_timing.ipynb` | Parcel age in each source. Fig. S8. |
| `/model/regional_evals.ipynb` | LiveOcean evaluation split into water sources. Fig. S1. |
| `/model/seasontiming.ipynb` | Determination of upwelling and downwelling season start and end. Fig. 2. |
| `/model/sensitivity.ipynb` | Sensitivity analysis for the south and offshore source definitions. Figs. S2, S5. |
| `/model/SensitivityData.py` | Simulation output organization for `/model/sensitivity.ipynb`. |
| `/model/summary_files_combines.py` | Makes annual mean files for use in `/model/quant_attribution_Flux.ipynb`. |
| `/model/summary_files_density.py` | Makes density-binned mean files for use in `/model/density.ipynb`. |
| `/model/summary_files.py` | Makes seasonal mean files for use in `/model/quant_attribution_Flux.ipynb`. |
| `/model/TimingData.py` | Organizes parcel age data for use in `/model/quant_timing.ipynb`. |

### /observations

| Folder/File | Description |
|-------------|-------------|
| `/observations/cucVoffd.ipynb` | Comparison of CUC and offshore deep observed properties. |
| `/observations/downloadERDDAP.py` | Downloads and organizes pertinent observations from various ERDDAP pages. |
| `/observations/myobs.ipynb` | Combines data into one file, bins by day and depth, removes duplicates and outliers. |
| `/observations/wm_divide.ipynb` | Divides data into offshore, slope, and shelf, removes extraneous data. |
| `/observations/wm_properties.ipynb` | Main analysis file: divides data into source waters and analysis properties. Fig. 6. |
| `/observations/wm_sensitivity.ipynb` | Sensitivity analysis for the south and offshore source definitions. Figs. S3, S4. |

## 4. Contact
For questions, please contact [me](mailto:rbeutel@student.ubc.ca).
