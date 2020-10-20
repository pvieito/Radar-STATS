# Radar STATS

[![Report Update](https://github.com/pvieito/Radar-STATS/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

**Radar STATS** (_née RadarCOVID-STATS_) is an open-source project developed to monitor and report hourly statistics about Spain's “Radar COVID” app Exposure Notification service – Created by [@pvieito](https://twitter.com/pvieito)

## Links

- [Last Results](#last-results)
- [Documentation](#documentation)
- [Contributions](#contributions)
- [Related Links](#related-links)
- [Archived Reports](https://github.com/pvieito/Radar-STATS/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/Radar-STATS/tree/master/Data/TEKs)
- [JSON Results](https://raw.githubusercontent.com/pvieito/RadarCOVID-STATS/master/Data/Resources/Current/RadarCOVID-Report-Summary-Results.json)
- [Twitter Bot](https://twitter.com/radarcovidstats)

## Last Results

- [Report 2020-10-20@21](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

### Daily Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/Radar-STATS/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

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
      <th>2020-10-20</th>
      <td>12212</td>
      <td>140</td>
      <td>722</td>
      <td>140</td>
      <td>128</td>
      <td>5.64</td>
      <td>1.05%</td>
    </tr>
    <tr>
      <th>2020-10-19</th>
      <td>12212</td>
      <td>270</td>
      <td>791</td>
      <td>142</td>
      <td>123</td>
      <td>6.43</td>
      <td>1.01%</td>
    </tr>
    <tr>
      <th>2020-10-18</th>
      <td>10778</td>
      <td>381</td>
      <td>726</td>
      <td>146</td>
      <td>132</td>
      <td>5.50</td>
      <td>1.22%</td>
    </tr>
    <tr>
      <th>2020-10-17</th>
      <td>10778</td>
      <td>523</td>
      <td>767</td>
      <td>174</td>
      <td>138</td>
      <td>5.56</td>
      <td>1.28%</td>
    </tr>
    <tr>
      <th>2020-10-16</th>
      <td>10778</td>
      <td>578</td>
      <td>769</td>
      <td>149</td>
      <td>141</td>
      <td>5.45</td>
      <td>1.31%</td>
    </tr>
    <tr>
      <th>2020-10-15</th>
      <td>10436</td>
      <td>646</td>
      <td>671</td>
      <td>151</td>
      <td>175</td>
      <td>3.83</td>
      <td>1.68%</td>
    </tr>
    <tr>
      <th>2020-10-14</th>
      <td>10308</td>
      <td>612</td>
      <td>463</td>
      <td>1</td>
      <td>133</td>
      <td>3.48</td>
      <td>1.29%</td>
    </tr>
    <tr>
      <th>2020-10-13</th>
      <td>10097</td>
      <td>551</td>
      <td>334</td>
      <td>1</td>
      <td>112</td>
      <td>2.98</td>
      <td>1.11%</td>
    </tr>
    <tr>
      <th>2020-10-12</th>
      <td>10794</td>
      <td>504</td>
      <td>326</td>
      <td>2</td>
      <td>136</td>
      <td>2.40</td>
      <td>1.26%</td>
    </tr>
    <tr>
      <th>2020-10-11</th>
      <td>10169</td>
      <td>462</td>
      <td>422</td>
      <td>1</td>
      <td>147</td>
      <td>2.87</td>
      <td>1.45%</td>
    </tr>
    <tr>
      <th>2020-10-10</th>
      <td>10169</td>
      <td>429</td>
      <td>429</td>
      <td>0</td>
      <td>133</td>
      <td>3.23</td>
      <td>1.31%</td>
    </tr>
    <tr>
      <th>2020-10-09</th>
      <td>10169</td>
      <td>421</td>
      <td>348</td>
      <td>1</td>
      <td>105</td>
      <td>3.31</td>
      <td>1.03%</td>
    </tr>
    <tr>
      <th>2020-10-08</th>
      <td>9960</td>
      <td>414</td>
      <td>272</td>
      <td>1</td>
      <td>86</td>
      <td>3.16</td>
      <td>0.86%</td>
    </tr>
    <tr>
      <th>2020-10-07</th>
      <td>9530</td>
      <td>375</td>
      <td>178</td>
      <td>0</td>
      <td>54</td>
      <td>3.30</td>
      <td>0.57%</td>
    </tr>
    <tr>
      <th>2020-10-06</th>
      <td>11021</td>
      <td>384</td>
      <td>233</td>
      <td>60</td>
      <td>56</td>
      <td>4.16</td>
      <td>0.51%</td>
    </tr>
    <tr>
      <th>2020-10-05</th>
      <td>9307</td>
      <td>350</td>
      <td>273</td>
      <td>52</td>
      <td>69</td>
      <td>3.96</td>
      <td>0.74%</td>
    </tr>
    <tr>
      <th>2020-10-04</th>
      <td>10493</td>
      <td>353</td>
      <td>331</td>
      <td>76</td>
      <td>78</td>
      <td>4.24</td>
      <td>0.74%</td>
    </tr>
    <tr>
      <th>2020-10-03</th>
      <td>10493</td>
      <td>312</td>
      <td>324</td>
      <td>69</td>
      <td>76</td>
      <td>4.26</td>
      <td>0.72%</td>
    </tr>
    <tr>
      <th>2020-10-02</th>
      <td>10493</td>
      <td>312</td>
      <td>299</td>
      <td>72</td>
      <td>72</td>
      <td>4.15</td>
      <td>0.69%</td>
    </tr>
    <tr>
      <th>2020-10-01</th>
      <td>10628</td>
      <td>317</td>
      <td>367</td>
      <td>75</td>
      <td>74</td>
      <td>4.96</td>
      <td>0.70%</td>
    </tr>
    <tr>
      <th>2020-09-30</th>
      <td>10805</td>
      <td>294</td>
      <td>271</td>
      <td>55</td>
      <td>51</td>
      <td>5.31</td>
      <td>0.47%</td>
    </tr>
    <tr>
      <th>2020-09-29</th>
      <td>9428</td>
      <td>265</td>
      <td>178</td>
      <td>32</td>
      <td>44</td>
      <td>4.05</td>
      <td>0.47%</td>
    </tr>
    <tr>
      <th>2020-09-28</th>
      <td>10971</td>
      <td>269</td>
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
    <tr>
      <th>2020-09-24</th>
      <td>11223</td>
      <td>286</td>
      <td>289</td>
      <td>17</td>
      <td>89</td>
      <td>3.25</td>
      <td>0.79%</td>
    </tr>
    <tr>
      <th>2020-09-23</th>
      <td>11314</td>
      <td>296</td>
      <td>267</td>
      <td>4</td>
      <td>70</td>
      <td>3.81</td>
      <td>0.62%</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Daily Generation to Upload Period Table

![RadarCOVID-Report-Generation-Upload-Period-Table](https://github.com/pvieito/Radar-STATS/raw/master/Data/Resources/Current/RadarCOVID-Report-Generation-Upload-Period-Table.png)

- [Daily Generation to Upload Period Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Generation-Upload-Period-Table.csv)

### Multi-Region Summary Table

_**NOTE:** This table includes data extracted from different Exposure Notification backends for each region (eg. Switzerland data is from the SwissCovid server). You can find the exact region to backend mapping in the [`exposure_notification_io` module](https://github.com/pvieito/Radar-STATS/blob/master/Modules/ExposureNotification/exposure_notification_io.py)._ 

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="6" halign="left">Shared TEKs by Generation Date</th>
    </tr>
    <tr>
      <th>Backend Region</th>
      <th>BE</th>
      <th>CH</th>
      <th>ES</th>
      <th>ES@PRE</th>
      <th>IT</th>
      <th>PT</th>
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
      <th>2020-10-20</th>
      <td>0</td>
      <td>182</td>
      <td>140</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-10-19</th>
      <td>0</td>
      <td>699</td>
      <td>270</td>
      <td>34</td>
      <td>454</td>
      <td>66</td>
    </tr>
    <tr>
      <th>2020-10-18</th>
      <td>171</td>
      <td>1084</td>
      <td>381</td>
      <td>44</td>
      <td>468</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2020-10-17</th>
      <td>342</td>
      <td>1472</td>
      <td>523</td>
      <td>47</td>
      <td>496</td>
      <td>139</td>
    </tr>
    <tr>
      <th>2020-10-16</th>
      <td>487</td>
      <td>1832</td>
      <td>578</td>
      <td>54</td>
      <td>508</td>
      <td>180</td>
    </tr>
    <tr>
      <th>2020-10-15</th>
      <td>595</td>
      <td>2167</td>
      <td>646</td>
      <td>50</td>
      <td>567</td>
      <td>206</td>
    </tr>
    <tr>
      <th>2020-10-14</th>
      <td>666</td>
      <td>2312</td>
      <td>612</td>
      <td>383</td>
      <td>598</td>
      <td>205</td>
    </tr>
    <tr>
      <th>2020-10-13</th>
      <td>664</td>
      <td>2356</td>
      <td>551</td>
      <td>375</td>
      <td>625</td>
      <td>198</td>
    </tr>
    <tr>
      <th>2020-10-12</th>
      <td>609</td>
      <td>2236</td>
      <td>504</td>
      <td>410</td>
      <td>632</td>
      <td>182</td>
    </tr>
    <tr>
      <th>2020-10-11</th>
      <td>510</td>
      <td>2045</td>
      <td>462</td>
      <td>84</td>
      <td>634</td>
      <td>165</td>
    </tr>
    <tr>
      <th>2020-10-10</th>
      <td>428</td>
      <td>1800</td>
      <td>429</td>
      <td>81</td>
      <td>616</td>
      <td>148</td>
    </tr>
    <tr>
      <th>2020-10-09</th>
      <td>386</td>
      <td>1603</td>
      <td>421</td>
      <td>77</td>
      <td>600</td>
      <td>134</td>
    </tr>
    <tr>
      <th>2020-10-08</th>
      <td>349</td>
      <td>1467</td>
      <td>414</td>
      <td>81</td>
      <td>585</td>
      <td>112</td>
    </tr>
    <tr>
      <th>2020-10-07</th>
      <td>297</td>
      <td>1361</td>
      <td>375</td>
      <td>90</td>
      <td>568</td>
      <td>109</td>
    </tr>
  </tbody>
</table>

- [Multi-Region Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Multi-Region-Summary-Table.csv)

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

Contributions to the **Radar STATS** project are welcome, both as [Pull Requests](https://github.com/pvieito/Radar-STATS/pulls) or [Issues](https://github.com/pvieito/Radar-STATS/issues).

Only files on the following directories should be modified as other files are generated automatically by the [Report Update GitHub Action](https://github.com/pvieito/Radar-STATS/blob/master/.github/workflows/report-update.yml):

- `Data/Templates/`
- `Modules/`
- `Notebooks/*/Source/`

The project _entry point_ is a Python notebook located at [`Notebooks/RadarCOVID-Report/Source/RadarCOVID-Report.ipynb`](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Source/RadarCOVID-Report.ipynb).

## Related Links

- [Radar COVID Website](https://radarcovid.gob.es/)
- [Radar COVID Project](https://github.com/RadarCOVID)
- [DP3T Project](https://github.com/DP-3T)
- [SwissCovid App Monitoring - Swiss Federal Statistical Office](https://www.experimental.bfs.admin.ch/expstat/en/home/innovative-methods/swisscovid-app-monitoring.html)
- [Diagnosis Key Analysis for Corona-Warn-App](https://github.com/micb25/dka/blob/master/README.en.md)
- [Testing Apps for COVID-19 Tracing (TACT) - TEK Survey](https://down.dsg.cs.tcd.ie/tact/tek-counts/)
- [European Federation Gateway Service (EFGS) Project](https://github.com/eu-federation-gateway-service/efgs-federation-gateway)
- [Mobile Contact Tracing Apps in EU Member States - European Commission](https://ec.europa.eu/info/live-work-travel-eu/health/coronavirus-response/travel-during-coronavirus-pandemic/mobile-contact-tracing-apps-eu-member-states_en)