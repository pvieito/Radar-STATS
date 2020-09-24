# RadarCOVID-Report

[![Report Update](https://github.com/pvieito/RadarCOVID-Report/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb)

Project to monitor and report hourly statistics about Spain's “Radar COVID” app Exposure Notification service.

## Links

- [Last Results](#last-results)
- [Documentation](#documentation)
- [Contributions](#contributions)
- [Related Links](#related-links)
- [Archived Reports](https://github.com/pvieito/RadarCOVID-Report/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/RadarCOVID-Report/tree/master/Data/TEKs)
- [Twitter Bot](https://twitter.com/radarcovidstats)

## Last Results

- [Report 2020-09-24@17](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Hourly/RadarCOVID-Report-2020-09-24@17.ipynb)

### Daily Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Daily Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>COVID-19 Cases (7-day Rolling Average)</th>
      <th>Shared TEKs by Generation Date</th>
      <th>Shared TEKs by Upload Date</th>
      <th>Shared Diagnoses (Estimation)</th>
      <th>TEKs Uploaded per Shared Diagnosis</th>
      <th>Usage Ratio (Fraction of Cases Which Shared Diagnosis)</th>
    </tr>
    <tr>
      <th>Sample Date (UTC)</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-09-24</th>
      <td>11314</td>
      <td>14</td>
      <td>242</td>
      <td>81</td>
      <td>2.99</td>
      <td>0.72%</td>
    </tr>
    <tr>
      <th>2020-09-23</th>
      <td>11314</td>
      <td>85</td>
      <td>267</td>
      <td>70</td>
      <td>3.81</td>
      <td>0.62%</td>
    </tr>
    <tr>
      <th>2020-09-22</th>
      <td>11300</td>
      <td>106</td>
      <td>148</td>
      <td>55</td>
      <td>2.69</td>
      <td>0.49%</td>
    </tr>
    <tr>
      <th>2020-09-21</th>
      <td>11105</td>
      <td>142</td>
      <td>190</td>
      <td>45</td>
      <td>4.22</td>
      <td>0.41%</td>
    </tr>
    <tr>
      <th>2020-09-20</th>
      <td>10531</td>
      <td>158</td>
      <td>116</td>
      <td>45</td>
      <td>2.58</td>
      <td>0.43%</td>
    </tr>
    <tr>
      <th>2020-09-19</th>
      <td>10531</td>
      <td>193</td>
      <td>90</td>
      <td>39</td>
      <td>2.31</td>
      <td>0.37%</td>
    </tr>
    <tr>
      <th>2020-09-18</th>
      <td>10531</td>
      <td>165</td>
      <td>138</td>
      <td>52</td>
      <td>2.65</td>
      <td>0.49%</td>
    </tr>
    <tr>
      <th>2020-09-17</th>
      <td>10215</td>
      <td>139</td>
      <td>63</td>
      <td>29</td>
      <td>2.17</td>
      <td>0.28%</td>
    </tr>
    <tr>
      <th>2020-09-16</th>
      <td>10140</td>
      <td>119</td>
      <td>62</td>
      <td>23</td>
      <td>2.70</td>
      <td>0.23%</td>
    </tr>
    <tr>
      <th>2020-09-15</th>
      <td>9808</td>
      <td>82</td>
      <td>58</td>
      <td>23</td>
      <td>2.52</td>
      <td>0.23%</td>
    </tr>
    <tr>
      <th>2020-09-14</th>
      <td>9740</td>
      <td>73</td>
      <td>61</td>
      <td>28</td>
      <td>2.18</td>
      <td>0.29%</td>
    </tr>
    <tr>
      <th>2020-09-13</th>
      <td>9620</td>
      <td>75</td>
      <td>92</td>
      <td>32</td>
      <td>2.88</td>
      <td>0.33%</td>
    </tr>
    <tr>
      <th>2020-09-12</th>
      <td>9620</td>
      <td>67</td>
      <td>92</td>
      <td>33</td>
      <td>2.79</td>
      <td>0.34%</td>
    </tr>
    <tr>
      <th>2020-09-11</th>
      <td>9620</td>
      <td>75</td>
      <td>46</td>
      <td>19</td>
      <td>2.42</td>
      <td>0.20%</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Hourly Summary Plots

![RadarCOVID-Report-Hourly-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Hourly-Summary-Plots.png)

## Documentation

### Definitions

- **TEK** (Temporary Exposure Key): A random identifier generated on-device each day used by [Exposure Notification](https://developer.apple.com/documentation/exposurenotification) apps like Radar COVID to detect exposures and share positive diagnoses. When a user has a confirmed case of COVID-19, he can share the TEKs generated on-device from the last 14 days to the Radar COVID server through the app. Other devices then download the infected TEKs and check if they have detected them nearby via Bluetooth on the previous 14 days.

### Metrics

- **COVID-19 Cases** (`covid_cases`): Confirmed new COVID-19 cases in Spain estimated with a 7-day rolling average.
- **Shared TEKs by Generation Date** (`shared_teks_by_generation_date`): TEKs uploaded to the Radar COVID server by the date they were generated on-device.
- **Shared TEKs by Upload Date** (`shared_teks_by_upload_date`): TEKs uploaded to the Radar COVID server by the date they were uploaded using the one-time code sent by the Health Authorities.
- **Shared Diagnoses** (`shared_diagnoses`): Estimation of the shared diagnoses via the Radar COVID app. The estimation is inferred from the number of TEKs uploaded each day which were generated on-device the previous day: typically each device sharing a positive diagnosis should upload at least the TEK generated on-device the previous day.
- **TEKs Uploaded per Shared Diagnosis** (`teks_per_shared_diagnosis`): The average number of TEKs uploaded with each shared diagnosis. This number should ideally be around 14 TEKs uploaded for each shared diagnosis.
- **Usage Ratio** (`shared_diagnoses_per_covid_case`): Fraction of COVID-19 cases which shared their diagnosis via Radar COVID. Ideally it should be 100% (ie. all confirmed cases sharing their TEKs with Radar COVID). 

**IMPORTANT NOTES**
- TEKs on the Radar COVID server may be padded with artificial random TEKs to increase anonymization. Currently there is no known technique to detect such alterations, so metrics dependent on the number of uploaded TEKs (eg. shared diagnoses or usage ratio) may be lower than the estimated.
- Some devices use the Exposure Notification API version 1, which shares the last TEK (ie. the TEK generated the day the diagnosis is shared) a day after it was generated, so two uploads (one with the previous TEKs and another with the last TEK) will take place on different days. This will lead to a duplication on the shared diagnoses metric. This duplication effect will disappear once all devices are using the Exposure Notification API version 2 which shares all 14 TEKs at once.

### Data Sources

- **COVID-19 Cases**: [Narrativa API](https://covid19tracking.narrativa.com)
- **TEKs**: [Radar COVID API](https://radarcovid.gob.es/)

## Contributions

Contributions to the **RadarCOVID-Report** project are welcome, both as [Pull Requests](https://github.com/pvieito/RadarCOVID-Report/pulls) or [Issues](https://github.com/pvieito/RadarCOVID-Report/issues).

Only files on the following directories should be modified as other files are generated automatically by the [Report Update GitHub Action](https://github.com/pvieito/RadarCOVID-Report/blob/master/.github/workflows/report-update.yml):

- `Data/Templates/`
- `Modules/`
- `Notebooks/*/Source/`

The project _entry point_ is a Python notebook located at [`Notebooks/RadarCOVID-Report/Source/RadarCOVID-Report.ipynb`](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Source/RadarCOVID-Report.ipynb).

## Related Links

- [Radar COVID Website](https://radarcovid.gob.es/)
- [Radar COVID Project](https://github.com/RadarCOVID)
- [DP3T Project](https://github.com/DP-3T)
- [Diagnosis Key Analysis for Corona-Warn-App](https://github.com/micb25/dka/blob/master/README.en.md)
- [Testing Apps for COVID-19 Tracing (TACT) - TEK Survey](https://down.dsg.cs.tcd.ie/tact/tek-counts/)
- [European Federation Gateway Service (EFGS) Project](https://github.com/eu-federation-gateway-service/efgs-federation-gateway)
