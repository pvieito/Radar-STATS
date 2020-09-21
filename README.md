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

- [Report 2020-09-21@18](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Hourly/RadarCOVID-Report-2020-09-21@18.ipynb)

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
      <th>Average Number of TEKs Uploaded per Shared Diagnose</th>
      <th>Usage Ratio (Shared Diagnoses per COVID-19 Case)</th>
    </tr>
    <tr>
      <th>sample_date</th>
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
      <th>2020-09-21</th>
      <td>10531.0</td>
      <td>NaN</td>
      <td>169.0</td>
      <td>41.0</td>
      <td>4.121951</td>
      <td>0.003893</td>
    </tr>
    <tr>
      <th>2020-09-20</th>
      <td>10531.0</td>
      <td>41.0</td>
      <td>116.0</td>
      <td>45.0</td>
      <td>2.577778</td>
      <td>0.004273</td>
    </tr>
    <tr>
      <th>2020-09-19</th>
      <td>10531.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>39.0</td>
      <td>2.307692</td>
      <td>0.003703</td>
    </tr>
    <tr>
      <th>2020-09-18</th>
      <td>10531.0</td>
      <td>94.0</td>
      <td>138.0</td>
      <td>52.0</td>
      <td>2.653846</td>
      <td>0.004938</td>
    </tr>
    <tr>
      <th>2020-09-17</th>
      <td>10215.0</td>
      <td>112.0</td>
      <td>63.0</td>
      <td>29.0</td>
      <td>2.172414</td>
      <td>0.002839</td>
    </tr>
    <tr>
      <th>2020-09-16</th>
      <td>10140.0</td>
      <td>115.0</td>
      <td>62.0</td>
      <td>23.0</td>
      <td>2.695652</td>
      <td>0.002268</td>
    </tr>
    <tr>
      <th>2020-09-15</th>
      <td>9808.0</td>
      <td>82.0</td>
      <td>58.0</td>
      <td>23.0</td>
      <td>2.521739</td>
      <td>0.002345</td>
    </tr>
    <tr>
      <th>2020-09-14</th>
      <td>9740.0</td>
      <td>73.0</td>
      <td>61.0</td>
      <td>28.0</td>
      <td>2.178571</td>
      <td>0.002875</td>
    </tr>
    <tr>
      <th>2020-09-13</th>
      <td>9620.0</td>
      <td>75.0</td>
      <td>92.0</td>
      <td>32.0</td>
      <td>2.875000</td>
      <td>0.003326</td>
    </tr>
    <tr>
      <th>2020-09-12</th>
      <td>9620.0</td>
      <td>67.0</td>
      <td>92.0</td>
      <td>33.0</td>
      <td>2.787879</td>
      <td>0.003430</td>
    </tr>
    <tr>
      <th>2020-09-11</th>
      <td>9620.0</td>
      <td>75.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>2.421053</td>
      <td>0.001975</td>
    </tr>
    <tr>
      <th>2020-09-10</th>
      <td>9376.0</td>
      <td>68.0</td>
      <td>45.0</td>
      <td>15.0</td>
      <td>3.000000</td>
      <td>0.001600</td>
    </tr>
    <tr>
      <th>2020-09-09</th>
      <td>9118.0</td>
      <td>60.0</td>
      <td>67.0</td>
      <td>21.0</td>
      <td>3.190476</td>
      <td>0.002303</td>
    </tr>
    <tr>
      <th>2020-09-08</th>
      <td>9077.0</td>
      <td>61.0</td>
      <td>44.0</td>
      <td>18.0</td>
      <td>2.444444</td>
      <td>0.001983</td>
    </tr>
    <tr>
      <th>2020-09-07</th>
      <td>8956.0</td>
      <td>58.0</td>
      <td>52.0</td>
      <td>22.0</td>
      <td>2.363636</td>
      <td>0.002456</td>
    </tr>
    <tr>
      <th>2020-09-06</th>
      <td>8529.0</td>
      <td>54.0</td>
      <td>60.0</td>
      <td>24.0</td>
      <td>2.500000</td>
      <td>0.002814</td>
    </tr>
    <tr>
      <th>2020-09-05</th>
      <td>8529.0</td>
      <td>56.0</td>
      <td>40.0</td>
      <td>17.0</td>
      <td>2.352941</td>
      <td>0.001993</td>
    </tr>
    <tr>
      <th>2020-09-04</th>
      <td>8529.0</td>
      <td>52.0</td>
      <td>58.0</td>
      <td>20.0</td>
      <td>2.900000</td>
      <td>0.002345</td>
    </tr>
    <tr>
      <th>2020-09-03</th>
      <td>8429.0</td>
      <td>51.0</td>
      <td>49.0</td>
      <td>19.0</td>
      <td>2.578947</td>
      <td>0.002254</td>
    </tr>
    <tr>
      <th>2020-09-02</th>
      <td>8529.0</td>
      <td>52.0</td>
      <td>57.0</td>
      <td>14.0</td>
      <td>4.071429</td>
      <td>0.001641</td>
    </tr>
    <tr>
      <th>2020-09-01</th>
      <td>8346.0</td>
      <td>46.0</td>
      <td>39.0</td>
      <td>14.0</td>
      <td>2.785714</td>
      <td>0.001677</td>
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

- **COVID-19 Cases** (`covid_cases`): Confirmed COVID-19 cases in Spain estimated with a 7-day rolling average.
- **Shared TEKs by Generation Date** (`shared_teks_by_generation_date`): TEKs uploaded to the Radar COVID server by the date they were generated on-device.
- **Shared TEKs by Upload Date** (`shared_teks_by_upload_date`): TEKs uploaded to the Radar COVID server by the date they were uploaded using the one-time code sent by the Health Authorities.
- **Shared Diagnoses** (`shared_diagnoses`): Estimation of the shared diagnoses via the Radar COVID app. The estimation is inferred from the number of TEKs uploaded each day which were generated on-device the previous day: typically each device sharing a positive diagnose should upload at least the TEK generated on-device the previous day.
- **Average Number of TEKs Uploaded per Shared Diagnose** (`teks_per_shared_diagnose`): The average number of TEKs uploaded with each shared diagnose. This number should ideally be around 13 TEKs uploaded for each shared diagnose.
- **Usage Ratio** (`shared_diagnoses_per_covid_case`): This is the ratio of shared diagnoses per COVID-19 case. Ideally it should be 100% (ie. all confirmed cases sharing their TEKs with Radar COVID). 

**NOTE**: TEKs on the Radar COVID server may be padded with artificial random TEKs to increase anonymization. Currently there is no known technique to detect such alterations, so metrics dependent on the number of uploaded TEKs (eg. shared diagnoses or usage ratio) may be lower than the estimated.

### Data Sources

- **COVID-19 Cases**: [Narrativa API](https://covid19tracking.narrativa.com)
- **TEKs**: [Radar COVID API](https://radarcovid.gob.es/)

## Contributions

Contributions to the **RadarCOVID-Report** project are welcome, both as [Pull Requests](https://github.com/pvieito/RadarCOVID-Report/pulls) or [Issues](https://github.com/pvieito/RadarCOVID-Report/issues).

Only files on these directories should be modified as other files are generated automatically by the [Report Update GitHub Action](https://github.com/pvieito/RadarCOVID-Report/blob/master/.github/workflows/report-update.yml):

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