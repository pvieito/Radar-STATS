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

- [Report 2021-07-29@01](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-07-29</th>
      <th>ES</th>
      <td>26399</td>
      <td></td>
      <td>16</td>
      <td></td>
      <td>16</td>
      <td>1.00</td>
      <td>0.06%</td>
      <td>26399</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-07-28</th>
      <th>ES</th>
      <td>26399</td>
      <td>219</td>
      <td>650</td>
      <td>203</td>
      <td>203</td>
      <td>3.20</td>
      <td>0.77%</td>
      <td>26399</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-07-27</th>
      <th>ES</th>
      <td>25617</td>
      <td>422</td>
      <td>963</td>
      <td>318</td>
      <td>318</td>
      <td>3.03</td>
      <td>1.24%</td>
      <td>25617</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-07-26</th>
      <th>ES</th>
      <td>25743</td>
      <td>404</td>
      <td>588</td>
      <td>201</td>
      <td>201</td>
      <td>2.93</td>
      <td>0.78%</td>
      <td>25743</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-07-25</th>
      <th>ES</th>
      <td>25744</td>
      <td>402</td>
      <td>425</td>
      <td>138</td>
      <td>138</td>
      <td>3.08</td>
      <td>0.54%</td>
      <td>25744</td>
      <td>3671</td>
      <td>290</td>
      <td>1.13%</td>
    </tr>
    <tr>
      <th>2021-07-24</th>
      <th>ES</th>
      <td>25744</td>
      <td>515</td>
      <td>614</td>
      <td>210</td>
      <td>210</td>
      <td>2.92</td>
      <td>0.82%</td>
      <td>25744</td>
      <td>3671</td>
      <td>290</td>
      <td>1.13%</td>
    </tr>
    <tr>
      <th>2021-07-23</th>
      <th>ES</th>
      <td>25744</td>
      <td>616</td>
      <td>817</td>
      <td>273</td>
      <td>273</td>
      <td>2.99</td>
      <td>1.06%</td>
      <td>25744</td>
      <td>3671</td>
      <td>290</td>
      <td>1.13%</td>
    </tr>
    <tr>
      <th>2021-07-22</th>
      <th>ES</th>
      <td>25728</td>
      <td>693</td>
      <td>916</td>
      <td>296</td>
      <td>296</td>
      <td>3.09</td>
      <td>1.15%</td>
      <td>25728</td>
      <td>3671</td>
      <td>290</td>
      <td>1.13%</td>
    </tr>
    <tr>
      <th>2021-07-21</th>
      <th>ES</th>
      <td>25464</td>
      <td>882</td>
      <td>1210</td>
      <td>377</td>
      <td>377</td>
      <td>3.21</td>
      <td>1.48%</td>
      <td>25464</td>
      <td>3671</td>
      <td>290</td>
      <td>1.14%</td>
    </tr>
    <tr>
      <th>2021-07-20</th>
      <th>ES</th>
      <td>24865</td>
      <td>841</td>
      <td>924</td>
      <td>294</td>
      <td>294</td>
      <td>3.14</td>
      <td>1.18%</td>
      <td>24865</td>
      <td>3671</td>
      <td>290</td>
      <td>1.17%</td>
    </tr>
    <tr>
      <th>2021-07-19</th>
      <th>ES</th>
      <td>27247</td>
      <td>835</td>
      <td>716</td>
      <td>246</td>
      <td>246</td>
      <td>2.91</td>
      <td>0.90%</td>
      <td>27247</td>
      <td>3671</td>
      <td>290</td>
      <td>1.06%</td>
    </tr>
    <tr>
      <th>2021-07-18</th>
      <th>ES</th>
      <td>23290</td>
      <td>566</td>
      <td>572</td>
      <td>199</td>
      <td>199</td>
      <td>2.87</td>
      <td>0.85%</td>
      <td>23290</td>
      <td>3427</td>
      <td>299</td>
      <td>1.28%</td>
    </tr>
    <tr>
      <th>2021-07-17</th>
      <th>ES</th>
      <td>23290</td>
      <td>448</td>
      <td>651</td>
      <td>212</td>
      <td>212</td>
      <td>3.07</td>
      <td>0.91%</td>
      <td>23290</td>
      <td>3427</td>
      <td>299</td>
      <td>1.28%</td>
    </tr>
    <tr>
      <th>2021-07-16</th>
      <th>ES</th>
      <td>23290</td>
      <td>326</td>
      <td>1041</td>
      <td>324</td>
      <td>324</td>
      <td>3.21</td>
      <td>1.39%</td>
      <td>23290</td>
      <td>3427</td>
      <td>299</td>
      <td>1.28%</td>
    </tr>
    <tr>
      <th>2021-07-15</th>
      <th>ES</th>
      <td>21978</td>
      <td>238</td>
      <td>1127</td>
      <td>339</td>
      <td>339</td>
      <td>3.32</td>
      <td>1.54%</td>
      <td>21978</td>
      <td>3427</td>
      <td>299</td>
      <td>1.36%</td>
    </tr>
    <tr>
      <th>2021-07-14</th>
      <th>ES</th>
      <td>20497</td>
      <td>214</td>
      <td>1399</td>
      <td>378</td>
      <td>378</td>
      <td>3.70</td>
      <td>1.84%</td>
      <td>20497</td>
      <td>3427</td>
      <td>299</td>
      <td>1.46%</td>
    </tr>
    <tr>
      <th>2021-07-13</th>
      <th>ES</th>
      <td>19210</td>
      <td>199</td>
      <td>669</td>
      <td>224</td>
      <td>224</td>
      <td>2.99</td>
      <td>1.17%</td>
      <td>19210</td>
      <td>3427</td>
      <td>299</td>
      <td>1.56%</td>
    </tr>
    <tr>
      <th>2021-07-12</th>
      <th>ES</th>
      <td>14950</td>
      <td>246</td>
      <td>684</td>
      <td>210</td>
      <td>210</td>
      <td>3.26</td>
      <td>1.40%</td>
      <td>14950</td>
      <td>3427</td>
      <td>299</td>
      <td>2.00%</td>
    </tr>
    <tr>
      <th>2021-07-11</th>
      <th>ES</th>
      <td>14761</td>
      <td>271</td>
      <td>456</td>
      <td>128</td>
      <td>128</td>
      <td>3.56</td>
      <td>0.87%</td>
      <td>14761</td>
      <td>3470</td>
      <td>223</td>
      <td>1.51%</td>
    </tr>
    <tr>
      <th>2021-07-10</th>
      <th>ES</th>
      <td>14761</td>
      <td>310</td>
      <td>497</td>
      <td>143</td>
      <td>143</td>
      <td>3.48</td>
      <td>0.97%</td>
      <td>14761</td>
      <td>3470</td>
      <td>223</td>
      <td>1.51%</td>
    </tr>
    <tr>
      <th>2021-07-09</th>
      <th>ES</th>
      <td>14761</td>
      <td>263</td>
      <td>868</td>
      <td>277</td>
      <td>277</td>
      <td>3.13</td>
      <td>1.88%</td>
      <td>14761</td>
      <td>3470</td>
      <td>223</td>
      <td>1.51%</td>
    </tr>
    <tr>
      <th>2021-07-08</th>
      <th>ES</th>
      <td>13430</td>
      <td>248</td>
      <td>784</td>
      <td>278</td>
      <td>278</td>
      <td>2.82</td>
      <td>2.07%</td>
      <td>13430</td>
      <td>3470</td>
      <td>223</td>
      <td>1.66%</td>
    </tr>
    <tr>
      <th>2021-07-07</th>
      <th>ES</th>
      <td>12719</td>
      <td>212</td>
      <td>820</td>
      <td>241</td>
      <td>241</td>
      <td>3.40</td>
      <td>1.89%</td>
      <td>12719</td>
      <td>3470</td>
      <td>223</td>
      <td>1.75%</td>
    </tr>
    <tr>
      <th>2021-07-06</th>
      <th>ES</th>
      <td>11554</td>
      <td>199</td>
      <td>694</td>
      <td>230</td>
      <td>230</td>
      <td>3.02</td>
      <td>1.99%</td>
      <td>11554</td>
      <td>3470</td>
      <td>223</td>
      <td>1.93%</td>
    </tr>
    <tr>
      <th>2021-07-05</th>
      <th>ES</th>
      <td>10548</td>
      <td>233</td>
      <td>435</td>
      <td>143</td>
      <td>143</td>
      <td>3.04</td>
      <td>1.36%</td>
      <td>10548</td>
      <td>3470</td>
      <td>223</td>
      <td>2.11%</td>
    </tr>
    <tr>
      <th>2021-07-04</th>
      <th>ES</th>
      <td>7344</td>
      <td>221</td>
      <td>347</td>
      <td>108</td>
      <td>108</td>
      <td>3.21</td>
      <td>1.47%</td>
      <td>7344</td>
      <td>3089</td>
      <td>93</td>
      <td>1.27%</td>
    </tr>
    <tr>
      <th>2021-07-03</th>
      <th>ES</th>
      <td>7344</td>
      <td>196</td>
      <td>295</td>
      <td>96</td>
      <td>96</td>
      <td>3.07</td>
      <td>1.31%</td>
      <td>7344</td>
      <td>3089</td>
      <td>93</td>
      <td>1.27%</td>
    </tr>
    <tr>
      <th>2021-07-02</th>
      <th>ES</th>
      <td>7344</td>
      <td>177</td>
      <td>304</td>
      <td>103</td>
      <td>103</td>
      <td>2.95</td>
      <td>1.40%</td>
      <td>7344</td>
      <td>3089</td>
      <td>93</td>
      <td>1.27%</td>
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
      <th colspan="8" halign="left">Shared TEKs by Generation Date (Source Countries)</th>
    </tr>
    <tr>
      <th>Backend</th>
      <th>CH</th>
      <th>DE</th>
      <th>DE@ES</th>
      <th>EE</th>
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
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-07-28</th>
      <td>14</td>
      <td>425</td>
      <td>148</td>
      <td>4</td>
      <td>219</td>
      <td>493</td>
      <td>0</td>
      <td>564</td>
    </tr>
    <tr>
      <th>2021-07-27</th>
      <td>50</td>
      <td>1607</td>
      <td>528</td>
      <td>5</td>
      <td>422</td>
      <td>1912</td>
      <td>20</td>
      <td>2274</td>
    </tr>
    <tr>
      <th>2021-07-26</th>
      <td>65</td>
      <td>1996</td>
      <td>638</td>
      <td>7</td>
      <td>404</td>
      <td>2486</td>
      <td>39</td>
      <td>2825</td>
    </tr>
    <tr>
      <th>2021-07-25</th>
      <td>69</td>
      <td>2233</td>
      <td>576</td>
      <td>7</td>
      <td>402</td>
      <td>2932</td>
      <td>63</td>
      <td>3264</td>
    </tr>
    <tr>
      <th>2021-07-24</th>
      <td>89</td>
      <td>2828</td>
      <td>754</td>
      <td>7</td>
      <td>515</td>
      <td>3681</td>
      <td>76</td>
      <td>3986</td>
    </tr>
    <tr>
      <th>2021-07-23</th>
      <td>103</td>
      <td>3361</td>
      <td>967</td>
      <td>7</td>
      <td>616</td>
      <td>4426</td>
      <td>106</td>
      <td>4716</td>
    </tr>
    <tr>
      <th>2021-07-22</th>
      <td>125</td>
      <td>3945</td>
      <td>1103</td>
      <td>10</td>
      <td>693</td>
      <td>5185</td>
      <td>116</td>
      <td>5330</td>
    </tr>
    <tr>
      <th>2021-07-21</th>
      <td>128</td>
      <td>4591</td>
      <td>1273</td>
      <td>12</td>
      <td>882</td>
      <td>6023</td>
      <td>130</td>
      <td>5515</td>
    </tr>
    <tr>
      <th>2021-07-20</th>
      <td>136</td>
      <td>5153</td>
      <td>1506</td>
      <td>13</td>
      <td>841</td>
      <td>6743</td>
      <td>138</td>
      <td>5596</td>
    </tr>
    <tr>
      <th>2021-07-19</th>
      <td>130</td>
      <td>5532</td>
      <td>1528</td>
      <td>14</td>
      <td>835</td>
      <td>7333</td>
      <td>131</td>
      <td>5711</td>
    </tr>
    <tr>
      <th>2021-07-18</th>
      <td>97</td>
      <td>5834</td>
      <td>1436</td>
      <td>14</td>
      <td>566</td>
      <td>6875</td>
      <td>126</td>
      <td>5787</td>
    </tr>
    <tr>
      <th>2021-07-17</th>
      <td>71</td>
      <td>6370</td>
      <td>1395</td>
      <td>13</td>
      <td>448</td>
      <td>6072</td>
      <td>107</td>
      <td>5904</td>
    </tr>
    <tr>
      <th>2021-07-16</th>
      <td>42</td>
      <td>6935</td>
      <td>1356</td>
      <td>12</td>
      <td>326</td>
      <td>5373</td>
      <td>85</td>
      <td>6058</td>
    </tr>
  </tbody>
</table>

- [Multi-Backend Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Multi-Backend-Summary-Table.csv)

#### Multi-Backend Cross-Sharing Summary Table

<table border="1" class="dataframe table-center">
  <thead>
    <tr style="text-align: center;">
      <th></th>
      <th colspan="8" halign="left">Fraction of TEKs in Backend (A) Available in Backend (B)</th>
    </tr>
    <tr style="text-align: center;">
      <th>Backend (A)</th>
      <th>CH</th>
      <th>DE</th>
      <th>DE@ES</th>
      <th>EE</th>
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
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <th>CH</th>
      <td>-</td>
      <td>2.1%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>96.1%</td>
      <td>-</td>
      <td>100.0%</td>
      <td></td>
      <td>88.6%</td>
      <td>69.2%</td>
      <td>0.4%</td>
      <td>65.7%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>26.0%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>22.2%</td>
      <td></td>
      <td>21.1%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EE</th>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES</th>
      <td></td>
      <td>12.5%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>12.0%</td>
      <td></td>
      <td>9.7%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>81.0%</td>
      <td>100.0%</td>
      <td></td>
      <td>100.0%</td>
      <td>-</td>
      <td>100.0%</td>
      <td>91.3%</td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.9%</td>
      <td>-</td>
      <td>1.9%</td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>74.4%</td>
      <td>91.9%</td>
      <td></td>
      <td>77.4%</td>
      <td>88.3%</td>
      <td>97.7%</td>
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
