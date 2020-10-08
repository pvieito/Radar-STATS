# Radar STATS

[![Report Update](https://github.com/Radar-STATS/Radar-STATS/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/Radar-STATS/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

Open-source project to monitor and report hourly statistics about Spain's “Radar COVID” app Exposure Notification service – Created by [@pvieito](https://twitter.com/pvieito)

## Links

- [Last Results](#last-results)
- [Documentation](#documentation)
- [Contributions](#contributions)
- [Related Links](#related-links)
- [Archived Reports](https://github.com/Radar-STATS/Radar-STATS/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/Radar-STATS/Radar-STATS/tree/master/Data/TEKs)
- [JSON Results](https://raw.githubusercontent.com/pvieito/RadarCOVID-STATS/master/Data/Resources/Current/RadarCOVID-Report-Summary-Results.json)
- [Twitter Bot](https://twitter.com/radarcovidstats)

## Last Results

- [Report 2020-10-08@21](https://github.com/Radar-STATS/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

### Daily Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/Radar-STATS/Radar-STATS/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Daily Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>COVID-19 Cases (7-day Rolling Average)</th>
      <th>Shared TEKs by Generation Date</th>
      <th>Shared TEKs by Upload Date</th>
      <th>Shared TEKs Uploaded on Generation Date</th>
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
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-10-08</th>
      <td>9530</td>
      <td>1</td>
      <td>267</td>
      <td>1</td>
      <td>85</td>
      <td>3.14</td>
      <td>0.89%</td>
    </tr>
    <tr>
      <th>2020-10-07</th>
      <td>9530</td>
      <td>85</td>
      <td>178</td>
      <td>0</td>
      <td>54</td>
      <td>3.30</td>
      <td>0.57%</td>
    </tr>
    <tr>
      <th>2020-10-06</th>
      <td>11021</td>
      <td>160</td>
      <td>233</td>
      <td>60</td>
      <td>56</td>
      <td>4.16</td>
      <td>0.51%</td>
    </tr>
    <tr>
      <th>2020-10-05</th>
      <td>9307</td>
      <td>185</td>
      <td>273</td>
      <td>52</td>
      <td>69</td>
      <td>3.96</td>
      <td>0.74%</td>
    </tr>
    <tr>
      <th>2020-10-04</th>
      <td>10493</td>
      <td>250</td>
      <td>331</td>
      <td>76</td>
      <td>78</td>
      <td>4.24</td>
      <td>0.74%</td>
    </tr>
    <tr>
      <th>2020-10-03</th>
      <td>10493</td>
      <td>282</td>
      <td>324</td>
      <td>69</td>
      <td>76</td>
      <td>4.26</td>
      <td>0.72%</td>
    </tr>
    <tr>
      <th>2020-10-02</th>
      <td>10493</td>
      <td>296</td>
      <td>299</td>
      <td>72</td>
      <td>72</td>
      <td>4.15</td>
      <td>0.69%</td>
    </tr>
    <tr>
      <th>2020-10-01</th>
      <td>10628</td>
      <td>309</td>
      <td>367</td>
      <td>75</td>
      <td>74</td>
      <td>4.96</td>
      <td>0.70%</td>
    </tr>
    <tr>
      <th>2020-09-30</th>
      <td>10805</td>
      <td>291</td>
      <td>271</td>
      <td>55</td>
      <td>51</td>
      <td>5.31</td>
      <td>0.47%</td>
    </tr>
    <tr>
      <th>2020-09-29</th>
      <td>9428</td>
      <td>263</td>
      <td>178</td>
      <td>32</td>
      <td>44</td>
      <td>4.05</td>
      <td>0.47%</td>
    </tr>
    <tr>
      <th>2020-09-28</th>
      <td>10971</td>
      <td>267</td>
      <td>211</td>
      <td>44</td>
      <td>54</td>
      <td>3.91</td>
      <td>0.49%</td>
    </tr>
    <tr>
      <th>2020-09-27</th>
      <td>10920</td>
      <td>315</td>
      <td>449</td>
      <td>98</td>
      <td>108</td>
      <td>4.16</td>
      <td>0.99%</td>
    </tr>
    <tr>
      <th>2020-09-26</th>
      <td>10920</td>
      <td>339</td>
      <td>448</td>
      <td>79</td>
      <td>110</td>
      <td>4.07</td>
      <td>1.01%</td>
    </tr>
    <tr>
      <th>2020-09-25</th>
      <td>10920</td>
      <td>284</td>
      <td>306</td>
      <td>14</td>
      <td>86</td>
      <td>3.56</td>
      <td>0.79%</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/Radar-STATS/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Hourly Summary Plots

![RadarCOVID-Report-Hourly-Summary-Plot](https://github.com/Radar-STATS/Radar-STATS/raw/master/Data/Resources/Current/RadarCOVID-Report-Hourly-Summary-Plots.png)

## Documentation

### Definitions

- **TEK** (Temporary Exposure Key): A random identifier generated on-device each day used by [Exposure Notification](https://developer.apple.com/documentation/exposurenotification) apps like Radar COVID to detect exposures and share positive diagnoses. When a user has a confirmed case of COVID-19, he can share the TEKs generated on-device from the last 14 days to the Radar COVID server through the app. Other devices then download the infected TEKs and check if they have detected them nearby via Bluetooth on the previous 14 days.

### Metrics

- **COVID-19 Cases** (`covid_cases`): Confirmed new COVID-19 cases in Spain estimated with a 7-day rolling average.
- **Shared TEKs by Generation Date** (`shared_teks_by_generation_date`): TEKs uploaded to the Radar COVID server by the date they were generated on-device.
- **Shared TEKs by Upload Date** (`shared_teks_by_upload_date`): TEKs uploaded to the Radar COVID server by the date they were uploaded using the one-time code sent by the Health Authorities.
- **Shared TEKs Uploaded on Generation Date** (`shared_teks_uploaded_on_generation_date`): TEKs uploaded to the Radar COVID server on the same date they were generated on-device. This metric measures the number of diagnoses shared by devices which already support the new Exposure Notification API version with early TEK release (ie. the current date TEK is released along previous days TEKs), see the notes below for more information.
- **Shared Diagnoses** (`shared_diagnoses`): Estimation of the number of diagnoses shared via the Radar COVID app. The estimation is inferred from the number of TEKs uploaded each day which were generated on-device the previous day: typically each device sharing a positive diagnosis should upload at least the TEK generated on-device the previous day. This estimation represents the maximum number of diagnoses that were shared via the app, the real number can be lower, see the notes below for more information.
- **TEKs Uploaded per Shared Diagnosis** (`teks_per_shared_diagnosis`): Estimation of the average number of TEKs uploaded with each shared diagnosis. This number should ideally be around 14 TEKs uploaded per shared diagnosis.
- **Usage Ratio** (`shared_diagnoses_per_covid_case`): Estimation of the fraction of COVID-19 cases which shared their diagnosis via Radar COVID. Ideally it should be 100% (ie. all confirmed cases sharing their TEKs with Radar COVID).

#### Important Notes

- TEKs on the Radar COVID server may be padded with artificial random TEKs to increase anonymization. Currently there is no known technique to detect such alterations, so metrics dependent on the number of uploaded TEKs (eg. shared diagnoses or usage ratio) may be lower than the estimated. For example, the German [Corona-Warn-App](https://www.coronawarn.app/en/) Exposure Notification server [adds 4 artificial TEKs for each real TEK](https://github.com/sftcd/tek_transparency/issues/9).
- Some devices use the [Exposure Notification API version 1](https://developer.apple.com/documentation/bundleresources/information_property_list/enapiversion), which shares the last TEK (ie. the TEK generated the day the diagnosis is shared) a day after it was generated, so two uploads (one with the previous TEKs and another with the last TEK) will take place on different days. This will lead to a duplication on the shared diagnoses metric. This duplication effect will disappear once all devices are using the [new Exposure Notification API version](https://developer.apple.com/documentation/exposurenotification/enmanager/3583725-getdiagnosiskeys) which shares all 14 TEKs at once.
- Unfortunately neither the [open-source Radar COVID project](https://github.com/RadarCOVID) nor [Spain's Secretariat of State for Digitization and Artificial Intelligence](https://twitter.com/SEDIAgob?s=21) publish the real number of shared diagnoses, [so we cannot more precisely adjust these estimations](https://twitter.com/pvieito/status/1309205729891549184?s=21). Other countries with similar apps built on the same [DP3T technology](https://github.com/DP-3T) do indeed publish [daily statistics of the shared diagnoses and app usage](https://www.experimental.bfs.admin.ch/expstat/en/home/innovative-methods/swisscovid-app-monitoring.html) for transparency and public research.

### Data Sources

- **COVID-19 Cases**: [Narrativa API](https://covid19tracking.narrativa.com)
- **TEKs**: [Radar COVID API](https://radarcovid.gob.es/)

## Contributions

Contributions to the **Radar STATS** project are welcome, both as [Pull Requests](https://github.com/Radar-STATS/Radar-STATS/pulls) or [Issues](https://github.com/Radar-STATS/Radar-STATS/issues).

Only files on the following directories should be modified as other files are generated automatically by the [Report Update GitHub Action](https://github.com/Radar-STATS/Radar-STATS/blob/master/.github/workflows/report-update.yml):

- `Data/Templates/`
- `Modules/`
- `Notebooks/*/Source/`

The project _entry point_ is a Python notebook located at [`Notebooks/RadarCOVID-Report/Source/RadarCOVID-Report.ipynb`](https://github.com/Radar-STATS/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Source/RadarCOVID-Report.ipynb).

## Related Links

- [Radar COVID Website](https://radarcovid.gob.es/)
- [Radar COVID Project](https://github.com/RadarCOVID)
- [DP3T Project](https://github.com/DP-3T)
- [SwissCovid App Monitoring - Swiss Federal Statistical Office](https://www.experimental.bfs.admin.ch/expstat/en/home/innovative-methods/swisscovid-app-monitoring.html)
- [Diagnosis Key Analysis for Corona-Warn-App](https://github.com/micb25/dka/blob/master/README.en.md)
- [Testing Apps for COVID-19 Tracing (TACT) - TEK Survey](https://down.dsg.cs.tcd.ie/tact/tek-counts/)
- [European Federation Gateway Service (EFGS) Project](https://github.com/eu-federation-gateway-service/efgs-federation-gateway)
