# Radar STATS

[![Report Update](https://github.com/pvieito/Radar-STATS/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

**Radar STATS** (_née RadarCOVID-STATS_) is an open-source project developed to monitor and report hourly statistics about Spain’s “Radar COVID” Exposure Notification app – Created by [@pvieito](https://twitter.com/pvieito)

## Links

- [Last Results](#last-results)
- [Documentation](#documentation)
- [Contributions](#contributions)
- [Press References](#press-references)
- [Related Links](#related-links)
- [Archived Reports](https://github.com/pvieito/Radar-STATS/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/Radar-STATS/tree/master/Data/TEKs)
- [JSON Results](https://raw.githubusercontent.com/pvieito/RadarCOVID-STATS/master/Data/Resources/Current/RadarCOVID-Report-Summary-Results.json)
- [Twitter Bot](https://twitter.com/radarcovidstats)

## Last Results

- [Report 2022-01-22@16](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

### Daily Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/Radar-STATS/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Daily Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>COVID-19 Cases (Source Countries)</th>
      <th>Shared TEKs by Generation Date (Source Countries)</th>
      <th>Shared TEKs by Upload Date (Source Countries)</th>
      <th>Shared TEKs Uploaded on Generation Date (Source Countries)</th>
      <th>Shared Diagnoses (Source Countries – Estimation)</th>
      <th>TEKs Uploaded per Shared Diagnosis (Source Countries)</th>
      <th>Usage Ratio (Source Countries)</th>
      <th>COVID-19 Cases (Spain)</th>
      <th>App Downloads (Spain – Official)</th>
      <th>Shared Diagnoses (Spain – Official)</th>
      <th>Usage Ratio (Spain)</th>
    </tr>
    <tr>
      <th>Sample Date (UTC)</th>
      <th>Source Countries</th>
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
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-01-22</th>
      <th>ES</th>
      <td>141095</td>
      <td>141</td>
      <td>522</td>
      <td>141</td>
      <td>141</td>
      <td>3.70</td>
      <td>0.10%</td>
      <td>141095</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-21</th>
      <th>ES</th>
      <td>126060</td>
      <td>552</td>
      <td>1281</td>
      <td>432</td>
      <td>432</td>
      <td>2.97</td>
      <td>0.34%</td>
      <td>126060</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-20</th>
      <th>ES</th>
      <td>129119</td>
      <td>595</td>
      <td>892</td>
      <td>304</td>
      <td>304</td>
      <td>2.93</td>
      <td>0.24%</td>
      <td>129119</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-19</th>
      <th>ES</th>
      <td>129364</td>
      <td>1021</td>
      <td>1892</td>
      <td>601</td>
      <td>601</td>
      <td>3.15</td>
      <td>0.46%</td>
      <td>129364</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-18</th>
      <th>ES</th>
      <td>132390</td>
      <td>1187</td>
      <td>1829</td>
      <td>528</td>
      <td>528</td>
      <td>3.46</td>
      <td>0.40%</td>
      <td>132390</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-17</th>
      <th>ES</th>
      <td>138172</td>
      <td>1533</td>
      <td>2159</td>
      <td>596</td>
      <td>596</td>
      <td>3.62</td>
      <td>0.43%</td>
      <td>138172</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-16</th>
      <th>ES</th>
      <td>132590</td>
      <td>1384</td>
      <td>1269</td>
      <td>377</td>
      <td>377</td>
      <td>3.37</td>
      <td>0.28%</td>
      <td>132590</td>
      <td>4256</td>
      <td>836</td>
      <td>0.63%</td>
    </tr>
    <tr>
      <th>2022-01-15</th>
      <th>ES</th>
      <td>132590</td>
      <td>1583</td>
      <td>1813</td>
      <td>566</td>
      <td>566</td>
      <td>3.20</td>
      <td>0.43%</td>
      <td>132590</td>
      <td>4256</td>
      <td>836</td>
      <td>0.63%</td>
    </tr>
    <tr>
      <th>2022-01-14</th>
      <th>ES</th>
      <td>132590</td>
      <td>1675</td>
      <td>2084</td>
      <td>549</td>
      <td>654</td>
      <td>3.19</td>
      <td>0.49%</td>
      <td>132590</td>
      <td>4256</td>
      <td>836</td>
      <td>0.63%</td>
    </tr>
    <tr>
      <th>2022-01-13</th>
      <th>ES</th>
      <td>144009</td>
      <td>2241</td>
      <td>3091</td>
      <td>803</td>
      <td>803</td>
      <td>3.85</td>
      <td>0.56%</td>
      <td>144009</td>
      <td>4256</td>
      <td>836</td>
      <td>0.58%</td>
    </tr>
    <tr>
      <th>2022-01-12</th>
      <th>ES</th>
      <td>121272</td>
      <td>1817</td>
      <td>2557</td>
      <td>712</td>
      <td>712</td>
      <td>3.59</td>
      <td>0.59%</td>
      <td>121272</td>
      <td>4256</td>
      <td>836</td>
      <td>0.69%</td>
    </tr>
    <tr>
      <th>2022-01-11</th>
      <th>ES</th>
      <td>115279</td>
      <td>1178</td>
      <td>2652</td>
      <td>814</td>
      <td>814</td>
      <td>3.26</td>
      <td>0.71%</td>
      <td>115279</td>
      <td>4256</td>
      <td>836</td>
      <td>0.73%</td>
    </tr>
    <tr>
      <th>2022-01-10</th>
      <th>ES</th>
      <td>112827</td>
      <td>1102</td>
      <td>1941</td>
      <td>627</td>
      <td>627</td>
      <td>3.10</td>
      <td>0.56%</td>
      <td>112827</td>
      <td>4256</td>
      <td>836</td>
      <td>0.74%</td>
    </tr>
    <tr>
      <th>2022-01-09</th>
      <th>ES</th>
      <td>124309</td>
      <td>1179</td>
      <td>1548</td>
      <td>495</td>
      <td>495</td>
      <td>3.13</td>
      <td>0.40%</td>
      <td>124309</td>
      <td>4955</td>
      <td>849</td>
      <td>0.68%</td>
    </tr>
    <tr>
      <th>2022-01-08</th>
      <th>ES</th>
      <td>124309</td>
      <td>1180</td>
      <td>1726</td>
      <td>481</td>
      <td>481</td>
      <td>3.59</td>
      <td>0.39%</td>
      <td>124309</td>
      <td>4955</td>
      <td>849</td>
      <td>0.68%</td>
    </tr>
    <tr>
      <th>2022-01-07</th>
      <th>ES</th>
      <td>124309</td>
      <td>1023</td>
      <td>1922</td>
      <td>605</td>
      <td>605</td>
      <td>3.18</td>
      <td>0.49%</td>
      <td>124309</td>
      <td>4955</td>
      <td>849</td>
      <td>0.68%</td>
    </tr>
    <tr>
      <th>2022-01-06</th>
      <th>ES</th>
      <td>89674</td>
      <td>933</td>
      <td>1611</td>
      <td>418</td>
      <td>530</td>
      <td>3.04</td>
      <td>0.59%</td>
      <td>89674</td>
      <td>4955</td>
      <td>849</td>
      <td>0.95%</td>
    </tr>
    <tr>
      <th>2022-01-05</th>
      <th>ES</th>
      <td>112773</td>
      <td>962</td>
      <td>2741</td>
      <td>775</td>
      <td>775</td>
      <td>3.54</td>
      <td>0.69%</td>
      <td>112773</td>
      <td>4955</td>
      <td>849</td>
      <td>0.75%</td>
    </tr>
    <tr>
      <th>2022-01-04</th>
      <th>ES</th>
      <td>107570</td>
      <td>904</td>
      <td>3746</td>
      <td>1216</td>
      <td>1216</td>
      <td>3.08</td>
      <td>1.13%</td>
      <td>107570</td>
      <td>4955</td>
      <td>849</td>
      <td>0.79%</td>
    </tr>
    <tr>
      <th>2022-01-03</th>
      <th>ES</th>
      <td>104984</td>
      <td>1012</td>
      <td>1781</td>
      <td>538</td>
      <td>538</td>
      <td>3.31</td>
      <td>0.51%</td>
      <td>104984</td>
      <td>4955</td>
      <td>849</td>
      <td>0.81%</td>
    </tr>
    <tr>
      <th>2022-01-02</th>
      <th>ES</th>
      <td>82391</td>
      <td>1146</td>
      <td>1238</td>
      <td>417</td>
      <td>417</td>
      <td>2.97</td>
      <td>0.51%</td>
      <td>82391</td>
      <td>6029</td>
      <td>951</td>
      <td>1.15%</td>
    </tr>
    <tr>
      <th>2022-01-01</th>
      <th>ES</th>
      <td>82391</td>
      <td>1110</td>
      <td>1279</td>
      <td>379</td>
      <td>379</td>
      <td>3.37</td>
      <td>0.46%</td>
      <td>82391</td>
      <td>6029</td>
      <td>951</td>
      <td>1.15%</td>
    </tr>
    <tr>
      <th>2021-12-31</th>
      <th>ES</th>
      <td>82391</td>
      <td>944</td>
      <td>1898</td>
      <td>459</td>
      <td>682</td>
      <td>2.78</td>
      <td>0.83%</td>
      <td>82391</td>
      <td>6029</td>
      <td>951</td>
      <td>1.15%</td>
    </tr>
    <tr>
      <th>2021-12-30</th>
      <th>ES</th>
      <td>82391</td>
      <td>842</td>
      <td>3295</td>
      <td>909</td>
      <td>909</td>
      <td>3.62</td>
      <td>1.10%</td>
      <td>82391</td>
      <td>6029</td>
      <td>951</td>
      <td>1.15%</td>
    </tr>
    <tr>
      <th>2021-12-29</th>
      <th>ES</th>
      <td>69709</td>
      <td>845</td>
      <td>2624</td>
      <td>708</td>
      <td>720</td>
      <td>3.64</td>
      <td>1.03%</td>
      <td>69709</td>
      <td>6029</td>
      <td>951</td>
      <td>1.36%</td>
    </tr>
    <tr>
      <th>2021-12-28</th>
      <th>ES</th>
      <td>63892</td>
      <td>1087</td>
      <td>3789</td>
      <td>1244</td>
      <td>1244</td>
      <td>3.05</td>
      <td>1.95%</td>
      <td>63892</td>
      <td>6029</td>
      <td>951</td>
      <td>1.49%</td>
    </tr>
    <tr>
      <th>2021-12-27</th>
      <th>ES</th>
      <td>56771</td>
      <td>1175</td>
      <td>2484</td>
      <td>819</td>
      <td>819</td>
      <td>3.03</td>
      <td>1.44%</td>
      <td>56771</td>
      <td>6029</td>
      <td>951</td>
      <td>1.68%</td>
    </tr>
    <tr>
      <th>2021-12-26</th>
      <th>ES</th>
      <td>37497</td>
      <td>918</td>
      <td>1644</td>
      <td>579</td>
      <td>579</td>
      <td>2.84</td>
      <td>1.54%</td>
      <td>37497</td>
      <td>9995</td>
      <td>946</td>
      <td>2.52%</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Daily Generation to Upload Period Table

![RadarCOVID-Report-Generation-Upload-Period-Table](https://github.com/pvieito/Radar-STATS/raw/master/Data/Resources/Current/RadarCOVID-Report-Generation-Upload-Period-Table.png)

- [Daily Generation to Upload Period Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Generation-Upload-Period-Table.csv)

### Multi-Backend Results

_**NOTE:** These tables include data extracted from different Exposure Notification backends (eg. the `CH` backend data is extracted from the SwissCovid server). You can find the exact backend definitions in the [`exposure_notification_io` module](https://github.com/pvieito/Radar-STATS/blob/master/Modules/ExposureNotification/exposure_notification_io.py)._ 

#### Multi-Backend Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="7" halign="left">Shared TEKs by Generation Date (Source Countries)</th>
    </tr>
    <tr>
      <th>Backend</th>
      <th>CH</th>
      <th>DE</th>
      <th>DE@ES</th>
      <th>ES</th>
      <th>EU@ES</th>
      <th>IT@ES</th>
      <th>MT</th>
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
      <th>2022-01-22</th>
      <td>487</td>
      <td>0</td>
      <td>0</td>
      <td>141</td>
      <td>0</td>
      <td>0</td>
      <td>2463</td>
    </tr>
    <tr>
      <th>2022-01-21</th>
      <td>1770</td>
      <td>32496</td>
      <td>0</td>
      <td>552</td>
      <td>0</td>
      <td>2</td>
      <td>6091</td>
    </tr>
    <tr>
      <th>2022-01-20</th>
      <td>2714</td>
      <td>63209</td>
      <td>0</td>
      <td>595</td>
      <td>0</td>
      <td>206</td>
      <td>6414</td>
    </tr>
    <tr>
      <th>2022-01-19</th>
      <td>3542</td>
      <td>87618</td>
      <td>0</td>
      <td>1021</td>
      <td>0</td>
      <td>374</td>
      <td>6400</td>
    </tr>
    <tr>
      <th>2022-01-18</th>
      <td>4085</td>
      <td>107767</td>
      <td>0</td>
      <td>1187</td>
      <td>0</td>
      <td>743</td>
      <td>6392</td>
    </tr>
    <tr>
      <th>2022-01-17</th>
      <td>4264</td>
      <td>111658</td>
      <td>0</td>
      <td>1533</td>
      <td>0</td>
      <td>993</td>
      <td>6331</td>
    </tr>
    <tr>
      <th>2022-01-16</th>
      <td>3916</td>
      <td>109642</td>
      <td>0</td>
      <td>1384</td>
      <td>0</td>
      <td>1211</td>
      <td>6608</td>
    </tr>
    <tr>
      <th>2022-01-15</th>
      <td>3631</td>
      <td>121198</td>
      <td>242</td>
      <td>1583</td>
      <td>3</td>
      <td>1256</td>
      <td>6620</td>
    </tr>
    <tr>
      <th>2022-01-14</th>
      <td>3669</td>
      <td>130641</td>
      <td>21259</td>
      <td>1675</td>
      <td>13869</td>
      <td>1458</td>
      <td>6650</td>
    </tr>
    <tr>
      <th>2022-01-13</th>
      <td>3695</td>
      <td>128271</td>
      <td>36428</td>
      <td>2241</td>
      <td>39465</td>
      <td>1762</td>
      <td>6687</td>
    </tr>
    <tr>
      <th>2022-01-12</th>
      <td>3182</td>
      <td>126786</td>
      <td>39367</td>
      <td>1817</td>
      <td>46366</td>
      <td>2268</td>
      <td>6685</td>
    </tr>
    <tr>
      <th>2022-01-11</th>
      <td>2327</td>
      <td>125532</td>
      <td>31135</td>
      <td>1178</td>
      <td>37992</td>
      <td>2283</td>
      <td>6684</td>
    </tr>
    <tr>
      <th>2022-01-10</th>
      <td>1717</td>
      <td>113422</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6679</td>
    </tr>
    <tr>
      <th>2022-01-09</th>
      <td>1130</td>
      <td>102100</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6674</td>
    </tr>
  </tbody>
</table>

- [Multi-Backend Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Multi-Backend-Summary-Table.csv)

#### Multi-Backend Cross-Sharing Summary Table

<table border="1" class="dataframe table-center">
  <thead>
    <tr style="text-align: center;">
      <th></th>
      <th colspan="7" halign="left">Fraction of TEKs in Backend (A) Available in Backend (B)</th>
    </tr>
    <tr style="text-align: center;">
      <th>Backend (A)</th>
      <th>CH</th>
      <th>DE</th>
      <th>DE@ES</th>
      <th>ES</th>
      <th>EU@ES</th>
      <th>IT@ES</th>
      <th>MT</th>
    </tr>
    <tr style="text-align: center;">
      <th>Backend (B)</th>
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
    <tr style="text-align: center;">
      <th>CH</th>
      <td>-</td>
      <td>2.7%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>91.5%</td>
      <td>-</td>
      <td>95.9%</td>
      <td>60.9%</td>
      <td>80.4%</td>
      <td>0.5%</td>
      <td>9.7%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>9.1%</td>
      <td>-</td>
      <td></td>
      <td>74.1%</td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES</th>
      <td></td>
      <td>0.7%</td>
      <td></td>
      <td>-</td>
      <td>3.0%</td>
      <td></td>
      <td>0.4%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>8.1%</td>
      <td>79.4%</td>
      <td>27.8%</td>
      <td>-</td>
      <td>18.5%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.7%</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>0.6%</td>
      <td></td>
      <td>2.1%</td>
      <td></td>
      <td></td>
      <td>-</td>
    </tr>
  </tbody>
</table>

- [Multi-Backend Cross-Sharing Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Multi-Backend-Cross-Sharing-Summary-Table.csv)

## Documentation

### Definitions

- **TEK** (Temporary Exposure Key): A random identifier generated on-device each day used by [Exposure Notification](https://developer.apple.com/documentation/exposurenotification) apps like Radar COVID to detect exposures and share positive diagnoses. When a user has a confirmed case of COVID-19, he can share the TEKs generated on-device from the last 14 days through an Exposure Notification app which will be published on a server like the Radar COVID server. Other devices then download the infected TEKs from the server and check if they have detected them nearby via Bluetooth on the previous 14 days.
- **Source Countries**: Countries with an Exposure Notification app that can share TEKs with the Radar COVID server directly or through the EFGS (see the notes below for more information). Currently the following countries are considered source countries: ES.

### Metrics

- **COVID-19 Cases in Source Countries** (`covid_cases`): Confirmed new COVID-19 cases in applicable source countries estimated with a 7-day rolling average (see the notes below for more information).
- **Shared TEKs by Generation Date** (`shared_teks_by_generation_date`): TEKs published on the Radar COVID server by the date they were generated on-device.
- **Shared TEKs by Upload Date** (`shared_teks_by_upload_date`): TEKs published on the Radar COVID server by the date they were added to the server. Typically this is the date when the user shares the positive diagnosis using the app with the one-time code sent by the Health Authorities or when TEKs from other countries backends are loaded from the EFGS.
- **Shared TEKs Uploaded on Generation Date** (`shared_teks_uploaded_on_generation_date`): TEKs uploaded to the Radar COVID server on the same date they were generated on-device. This metric measures the number of diagnoses shared by devices which already support the new Exposure Notification API version with early TEK release (ie. the current date TEK is released along previous days TEKs), see the notes below for more information.
- **Shared Diagnoses** (`shared_diagnoses`): Estimation of the number of diagnoses shared via Exposure Notification apps published on the Radar COVID server. The estimation is inferred from the maximum number of TEKs uploaded each date that were generated on-device on a unique date, as each device can only upload 1 TEK per generation date.
- **TEKs Uploaded per Shared Diagnosis** (`teks_per_shared_diagnosis`): Estimation of the average number of TEKs uploaded with each shared diagnosis. This number should ideally be around 14 TEKs uploaded per shared diagnosis.
- **Usage Ratio** (`shared_diagnoses_per_covid_case`): Estimation of the fraction of COVID-19 cases in applicable source countries which shared their diagnosis via an Exposure Notification app (see the notes below for more information). Ideally it should be 100% (ie. all confirmed cases sharing their TEKs with an Exposure Notification app).

#### Important Notes

- As Radar COVID is [integrated](https://twitter.com/eu_commission/status/1318152800887558144?s=21) with the [EU Federation Gateway Service (EFGS)](https://github.com/eu-federation-gateway-service/efgs-federation-gateway) project, the server may publish TEKs from multiple source countries. Those EU-wide TEKs are published merged with TEKs shared directly from the Radar COVID app and they cannot be distinguished. To compute a valid usage ratio, we take in account COVID-19 cases from all applicable source countries [integrated with the EFGS](https://ec.europa.eu/info/live-work-travel-eu/health/coronavirus-response/travel-during-coronavirus-pandemic/mobile-contact-tracing-apps-eu-member-states_en), currently the following countries are considered source countries: ES.
- TEKs on the Radar COVID server may also be padded with artificial random TEKs to increase anonymization. Currently there is no known technique to detect such alterations, so metrics dependent on the number of uploaded TEKs (eg. shared diagnoses or usage ratio) may be lower than the estimated.
- Some devices use the [Exposure Notification API version 1](https://developer.apple.com/documentation/bundleresources/information_property_list/enapiversion), which shares the last TEK (ie. the TEK generated the day the diagnosis is shared) a day after it was generated, so two uploads (one with the previous TEKs and another with the last TEK) will take place on different days. This will lead to a duplication on the shared diagnoses metric. This duplication effect will disappear once all devices are using the [new Exposure Notification API version](https://developer.apple.com/documentation/exposurenotification/enmanager/3583725-getdiagnosiskeys) which shares all 14 TEKs at once.

### Data Sources

- **COVID-19 Cases**: [Our World in Data](https://ourworldindata.org/coronavirus)
- **Official Statistics & TEKs**: [Radar COVID API](https://radarcovid.gob.es/)

## Contributions

Contributions to the **Radar STATS** project are welcome, both as [Pull Requests](https://github.com/pvieito/Radar-STATS/pulls) or [Issues](https://github.com/pvieito/Radar-STATS/issues).

Only files on the following directories should be modified as other files are generated automatically by the [Report Update GitHub Action](https://github.com/pvieito/Radar-STATS/blob/master/.github/workflows/report-update.yml):

- `Data/Templates/`
- `Modules/`
- `Notebooks/*/Source/`

The project _entry point_ is a Python notebook located at [`Notebooks/RadarCOVID-Report/Source/RadarCOVID-Report.ipynb`](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Source/RadarCOVID-Report.ipynb).

## Press References

The **Radar STATS** project has been referenced and featured on multiple news articles:

- [El País](https://elpais.com/tecnologia/2020-09-27/por-que-la-app-radar-covid-apenas-manda-avisos-de-contagio-a-sus-usuarios.html?ssm=TW_CM)
- [Xataka](https://www.xataka.com/aplicaciones/nadie-supo-darme-codigo-caos-radar-covid-codigos-que-no-llegan-notificaciones-retraso-mucho-trabajo-hacer)
- [Genbeta](https://www.genbeta.com/actualidad/bot-publica-estadisticas-nivel-uso-radarcovid-estima-que-casi-1-positivos-sube-sus-datos-a-app)
- [El Independiente](https://www.elindependiente.com/futuro/gadget/2020/09/25/radar-covid-rastrea-menos-del-1-de-los-contagios-que-se-detectan-en-espana/?utm_source=share_buttons&utm_medium=twitter&utm_campaign=social_share2)
- [Business Insider](https://www.businessinsider.es/crean-herramienta-medir-uso-radarcovid-espana-728625?utm_medium=Social&utm_campaign=BI&utm_source=Twitter#Echobox=1601638989)

## Related Links

- [Radar COVID – Website](https://radarcovid.gob.es/)
- [Radar COVID – Project](https://github.com/RadarCOVID)
- [Radar COVID – Statistics](https://radarcovid.gob.es/estadisticas/codigos-introducidos-a-casos-confirmados)
- [DP3T Project](https://github.com/DP-3T)
- [SwissCovid App Monitoring - Swiss Federal Statistical Office](https://www.experimental.bfs.admin.ch/expstat/en/home/innovative-methods/swisscovid-app-monitoring.html)
- [Diagnosis Key Analysis for Corona-Warn-App](https://github.com/micb25/dka/blob/master/README.en.md)
- [Testing Apps for COVID-19 Tracing (TACT) - TEK Survey](https://down.dsg.cs.tcd.ie/tact/tek-counts/)
- [EU Federation Gateway Service (EFGS) Project](https://github.com/eu-federation-gateway-service/efgs-federation-gateway)
- [Mobile Contact Tracing Apps in EU Member States - European Commission](https://ec.europa.eu/info/live-work-travel-eu/health/coronavirus-response/travel-during-coronavirus-pandemic/mobile-contact-tracing-apps-eu-member-states_en)
- [Corona-Warn-App – FAQ – Interoperability Countries](https://www.coronawarn.app/en/faq/#interoperability_countries)
