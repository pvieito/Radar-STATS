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

- [Report 2020-10-25@19](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

### Daily Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/Radar-STATS/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Daily Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>COVID-19 Cases in Source Countries (7-day Rolling Average)</th>
      <th>Shared TEKs by Generation Date</th>
      <th>Shared TEKs by Upload Date</th>
      <th>Shared TEKs Uploaded on Generation Date</th>
      <th>Shared Diagnoses (Estimation)</th>
      <th>TEKs Uploaded per Shared Diagnosis</th>
      <th>Usage Ratio (Fraction of Cases in Source Countries Which Shared Diagnosis)</th>
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
      <th>2020-10-25</th>
      <td>15653</td>
      <td>138</td>
      <td>578</td>
      <td>138</td>
      <td>92</td>
      <td>6.28</td>
      <td>0.59%</td>
    </tr>
    <tr>
      <th>2020-10-24</th>
      <td>15653</td>
      <td>269</td>
      <td>703</td>
      <td>177</td>
      <td>125</td>
      <td>5.62</td>
      <td>0.80%</td>
    </tr>
    <tr>
      <th>2020-10-23</th>
      <td>15653</td>
      <td>377</td>
      <td>769</td>
      <td>167</td>
      <td>145</td>
      <td>5.30</td>
      <td>0.93%</td>
    </tr>
    <tr>
      <th>2020-10-22</th>
      <td>14987</td>
      <td>504</td>
      <td>726</td>
      <td>180</td>
      <td>132</td>
      <td>5.50</td>
      <td>0.88%</td>
    </tr>
    <tr>
      <th>2020-10-21</th>
      <td>13891</td>
      <td>570</td>
      <td>841</td>
      <td>157</td>
      <td>153</td>
      <td>5.50</td>
      <td>1.10%</td>
    </tr>
    <tr>
      <th>2020-10-20</th>
      <td>13177</td>
      <td>640</td>
      <td>772</td>
      <td>149</td>
      <td>135</td>
      <td>5.72</td>
      <td>1.02%</td>
    </tr>
    <tr>
      <th>2020-10-19</th>
      <td>12212</td>
      <td>680</td>
      <td>791</td>
      <td>142</td>
      <td>123</td>
      <td>6.43</td>
      <td>1.01%</td>
    </tr>
    <tr>
      <th>2020-10-18</th>
      <td>10778</td>
      <td>691</td>
      <td>726</td>
      <td>146</td>
      <td>132</td>
      <td>5.50</td>
      <td>1.22%</td>
    </tr>
    <tr>
      <th>2020-10-17</th>
      <td>10778</td>
      <td>739</td>
      <td>767</td>
      <td>174</td>
      <td>138</td>
      <td>5.56</td>
      <td>1.28%</td>
    </tr>
    <tr>
      <th>2020-10-16</th>
      <td>10778</td>
      <td>710</td>
      <td>769</td>
      <td>149</td>
      <td>141</td>
      <td>5.45</td>
      <td>1.31%</td>
    </tr>
    <tr>
      <th>2020-10-15</th>
      <td>10436</td>
      <td>730</td>
      <td>671</td>
      <td>151</td>
      <td>175</td>
      <td>3.83</td>
      <td>1.68%</td>
    </tr>
    <tr>
      <th>2020-10-14</th>
      <td>10308</td>
      <td>670</td>
      <td>463</td>
      <td>1</td>
      <td>133</td>
      <td>3.48</td>
      <td>1.29%</td>
    </tr>
    <tr>
      <th>2020-10-13</th>
      <td>10097</td>
      <td>588</td>
      <td>334</td>
      <td>1</td>
      <td>112</td>
      <td>2.98</td>
      <td>1.11%</td>
    </tr>
    <tr>
      <th>2020-10-12</th>
      <td>10794</td>
      <td>532</td>
      <td>326</td>
      <td>2</td>
      <td>136</td>
      <td>2.40</td>
      <td>1.26%</td>
    </tr>
    <tr>
      <th>2020-10-11</th>
      <td>10169</td>
      <td>479</td>
      <td>422</td>
      <td>1</td>
      <td>147</td>
      <td>2.87</td>
      <td>1.45%</td>
    </tr>
    <tr>
      <th>2020-10-10</th>
      <td>10169</td>
      <td>438</td>
      <td>429</td>
      <td>0</td>
      <td>133</td>
      <td>3.23</td>
      <td>1.31%</td>
    </tr>
    <tr>
      <th>2020-10-09</th>
      <td>10169</td>
      <td>426</td>
      <td>348</td>
      <td>1</td>
      <td>105</td>
      <td>3.31</td>
      <td>1.03%</td>
    </tr>
    <tr>
      <th>2020-10-08</th>
      <td>9960</td>
      <td>417</td>
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
      <td>9605</td>
      <td>384</td>
      <td>233</td>
      <td>60</td>
      <td>56</td>
      <td>4.16</td>
      <td>0.58%</td>
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
      <td>10844</td>
      <td>265</td>
      <td>178</td>
      <td>32</td>
      <td>44</td>
      <td>4.05</td>
      <td>0.41%</td>
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
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Daily Generation to Upload Period Table

![RadarCOVID-Report-Generation-Upload-Period-Table](https://github.com/pvieito/Radar-STATS/raw/master/Data/Resources/Current/RadarCOVID-Report-Generation-Upload-Period-Table.png)

- [Daily Generation to Upload Period Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Generation-Upload-Period-Table.csv)

### Multi-Backend Summary Table

_**NOTE:** This table includes data extracted from different Exposure Notification backends (eg. the `CH` backend data is extracted from the SwissCovid server). You can find the exact backend definitions in the [`exposure_notification_io` module](https://github.com/pvieito/Radar-STATS/blob/master/Modules/ExposureNotification/exposure_notification_io.py)._ 

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="10" halign="left">Shared TEKs by Generation Date</th>
    </tr>
    <tr>
      <th>Backend Identifier</th>
      <th>BE</th>
      <th>BE@TST</th>
      <th>CH</th>
      <th>DE</th>
      <th>EE</th>
      <th>ES</th>
      <th>ES@PRE</th>
      <th>IT</th>
      <th>MT</th>
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
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-10-25</th>
      <td>0</td>
      <td>0</td>
      <td>272</td>
      <td>0</td>
      <td>0</td>
      <td>138</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-10-24</th>
      <td>0</td>
      <td>0</td>
      <td>1032</td>
      <td>0</td>
      <td>2</td>
      <td>269</td>
      <td>6</td>
      <td>548</td>
      <td>104</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2020-10-23</th>
      <td>376</td>
      <td>47</td>
      <td>1730</td>
      <td>1360</td>
      <td>2</td>
      <td>377</td>
      <td>64</td>
      <td>1886</td>
      <td>109</td>
      <td>105</td>
    </tr>
    <tr>
      <th>2020-10-22</th>
      <td>794</td>
      <td>52</td>
      <td>2355</td>
      <td>3152</td>
      <td>6</td>
      <td>504</td>
      <td>130</td>
      <td>3516</td>
      <td>112</td>
      <td>168</td>
    </tr>
    <tr>
      <th>2020-10-21</th>
      <td>1191</td>
      <td>47</td>
      <td>2802</td>
      <td>4478</td>
      <td>13</td>
      <td>570</td>
      <td>242</td>
      <td>3282</td>
      <td>116</td>
      <td>201</td>
    </tr>
    <tr>
      <th>2020-10-20</th>
      <td>1419</td>
      <td>48</td>
      <td>3147</td>
      <td>5552</td>
      <td>17</td>
      <td>640</td>
      <td>240</td>
      <td>4104</td>
      <td>122</td>
      <td>232</td>
    </tr>
    <tr>
      <th>2020-10-19</th>
      <td>1503</td>
      <td>50</td>
      <td>3341</td>
      <td>6267</td>
      <td>17</td>
      <td>680</td>
      <td>282</td>
      <td>4433</td>
      <td>124</td>
      <td>269</td>
    </tr>
    <tr>
      <th>2020-10-18</th>
      <td>1349</td>
      <td>45</td>
      <td>3329</td>
      <td>6455</td>
      <td>17</td>
      <td>691</td>
      <td>288</td>
      <td>4208</td>
      <td>127</td>
      <td>293</td>
    </tr>
    <tr>
      <th>2020-10-17</th>
      <td>1252</td>
      <td>55</td>
      <td>3243</td>
      <td>6776</td>
      <td>20</td>
      <td>739</td>
      <td>289</td>
      <td>4089</td>
      <td>128</td>
      <td>277</td>
    </tr>
    <tr>
      <th>2020-10-16</th>
      <td>1086</td>
      <td>56</td>
      <td>3097</td>
      <td>8264</td>
      <td>16</td>
      <td>710</td>
      <td>297</td>
      <td>3986</td>
      <td>132</td>
      <td>288</td>
    </tr>
    <tr>
      <th>2020-10-15</th>
      <td>976</td>
      <td>54</td>
      <td>3027</td>
      <td>12166</td>
      <td>14</td>
      <td>730</td>
      <td>291</td>
      <td>3943</td>
      <td>132</td>
      <td>286</td>
    </tr>
    <tr>
      <th>2020-10-14</th>
      <td>855</td>
      <td>50</td>
      <td>2878</td>
      <td>15365</td>
      <td>11</td>
      <td>670</td>
      <td>623</td>
      <td>3895</td>
      <td>135</td>
      <td>267</td>
    </tr>
    <tr>
      <th>2020-10-13</th>
      <td>749</td>
      <td>48</td>
      <td>2701</td>
      <td>17816</td>
      <td>11</td>
      <td>588</td>
      <td>616</td>
      <td>3833</td>
      <td>131</td>
      <td>240</td>
    </tr>
    <tr>
      <th>2020-10-12</th>
      <td>638</td>
      <td>43</td>
      <td>2447</td>
      <td>19653</td>
      <td>11</td>
      <td>532</td>
      <td>650</td>
      <td>3786</td>
      <td>131</td>
      <td>212</td>
    </tr>
  </tbody>
</table>

- [Multi-Backend Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Multi-Backend-Summary-Table.csv)

## Documentation

### Definitions

- **TEK** (Temporary Exposure Key): A random identifier generated on-device each day used by [Exposure Notification](https://developer.apple.com/documentation/exposurenotification) apps like Radar COVID to detect exposures and share positive diagnoses. When a user has a confirmed case of COVID-19, he can share the TEKs generated on-device from the last 14 days to the Radar COVID server through the app. Other devices then download the infected TEKs and check if they have detected them nearby via Bluetooth on the previous 14 days.

### Metrics

- **COVID-19 Cases in Source Countries** (`covid_cases`): Confirmed new COVID-19 cases in applicable source countries estimated with a 7-day rolling average (see the notes below for more information).
- **Shared TEKs by Generation Date** (`shared_teks_by_generation_date`): TEKs uploaded to the Radar COVID server by the date they were generated on-device.
- **Shared TEKs by Upload Date** (`shared_teks_by_upload_date`): TEKs uploaded to the Radar COVID server by the date they were uploaded using the one-time code sent by the Health Authorities.
- **Shared TEKs Uploaded on Generation Date** (`shared_teks_uploaded_on_generation_date`): TEKs uploaded to the Radar COVID server on the same date they were generated on-device. This metric measures the number of diagnoses shared by devices which already support the new Exposure Notification API version with early TEK release (ie. the current date TEK is released along previous days TEKs), see the notes below for more information.
- **Shared Diagnoses** (`shared_diagnoses`): Estimation of the number of diagnoses shared via Exposure Notification apps published on the Radar COVID server. The estimation is inferred from the number of TEKs uploaded each day which were generated on-device the previous day: typically each device sharing a positive diagnosis should upload at least the TEK generated on-device the previous day. This estimation represents the maximum number of diagnoses that were shared via the app, the real number can be lower, see the notes below for more information.
- **TEKs Uploaded per Shared Diagnosis** (`teks_per_shared_diagnosis`): Estimation of the average number of TEKs uploaded with each shared diagnosis. This number should ideally be around 14 TEKs uploaded per shared diagnosis.
- **Usage Ratio** (`shared_diagnoses_per_covid_case`): Estimation of the fraction of COVID-19 cases in applicable source countries which shared their diagnosis via an Exposure Notification app. Ideally it should be 100% (ie. all confirmed cases sharing their TEKs with an Exposure Notification app).

#### Important Notes

- As Radar COVID is [integrated](https://twitter.com/eu_commission/status/1318152800887558144?s=21) with the [EU Federation Gateway Service (EFGS)](https://github.com/eu-federation-gateway-service/efgs-federation-gateway) project, the server may publish TEKs from multiple source countries. Those EU-wide TEKs are published merged with TEKs shared directly from the Radar COVID app and they cannot be distinguished. To compute a valid usage ratio, we take in account COVID-19 cases from all applicable source countries [integrated with the EFGS](https://ec.europa.eu/info/live-work-travel-eu/health/coronavirus-response/travel-during-coronavirus-pandemic/mobile-contact-tracing-apps-eu-member-states_en), currently the following countries are considered source countries: ES. 
- TEKs on the Radar COVID server may also be padded with artificial random TEKs to increase anonymization. Currently there is no known technique to detect such alterations, so metrics dependent on the number of uploaded TEKs (eg. shared diagnoses or usage ratio) may be lower than the estimated.
- Some devices use the [Exposure Notification API version 1](https://developer.apple.com/documentation/bundleresources/information_property_list/enapiversion), which shares the last TEK (ie. the TEK generated the day the diagnosis is shared) a day after it was generated, so two uploads (one with the previous TEKs and another with the last TEK) will take place on different days. This will lead to a duplication on the shared diagnoses metric. This duplication effect will disappear once all devices are using the [new Exposure Notification API version](https://developer.apple.com/documentation/exposurenotification/enmanager/3583725-getdiagnosiskeys) which shares all 14 TEKs at once.
- Unfortunately neither the [open-source Radar COVID project](https://github.com/RadarCOVID) nor [Spain's Secretariat of State for Digitization and Artificial Intelligence](https://twitter.com/SEDIAgob?s=21) publish the real number of shared diagnoses, [so we cannot more precisely adjust these estimations](https://twitter.com/pvieito/status/1309205729891549184?s=21). Other countries with similar apps built on the same [DP3T technology](https://github.com/DP-3T) do indeed publish [daily statistics of the shared diagnoses and app usage](https://www.experimental.bfs.admin.ch/expstat/en/home/innovative-methods/swisscovid-app-monitoring.html) for transparency and public research.

### Data Sources

- **COVID-19 Cases**: [EU – European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)
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
- [EU Federation Gateway Service (EFGS) Project](https://github.com/eu-federation-gateway-service/efgs-federation-gateway)
- [Mobile Contact Tracing Apps in EU Member States - European Commission](https://ec.europa.eu/info/live-work-travel-eu/health/coronavirus-response/travel-during-coronavirus-pandemic/mobile-contact-tracing-apps-eu-member-states_en)