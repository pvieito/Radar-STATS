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

- [Report 2021-08-11@03](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-08-11</th>
      <th>ES</th>
      <td>39638</td>
      <td></td>
      <td>8</td>
      <td></td>
      <td>8</td>
      <td>1.00</td>
      <td>0.02%</td>
      <td>39638</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-10</th>
      <th>ES</th>
      <td>39638</td>
      <td>143</td>
      <td>335</td>
      <td>135</td>
      <td>135</td>
      <td>2.48</td>
      <td>0.34%</td>
      <td>39638</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-09</th>
      <th>ES</th>
      <td>17827</td>
      <td>131</td>
      <td>271</td>
      <td>83</td>
      <td>83</td>
      <td>3.27</td>
      <td>0.47%</td>
      <td>17827</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-08</th>
      <th>ES</th>
      <td>20155</td>
      <td>144</td>
      <td>189</td>
      <td>59</td>
      <td>59</td>
      <td>3.20</td>
      <td>0.29%</td>
      <td>20155</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-07</th>
      <th>ES</th>
      <td>20155</td>
      <td>185</td>
      <td>223</td>
      <td>85</td>
      <td>85</td>
      <td>2.62</td>
      <td>0.42%</td>
      <td>20155</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-06</th>
      <th>ES</th>
      <td>20155</td>
      <td>258</td>
      <td>455</td>
      <td>142</td>
      <td>142</td>
      <td>3.20</td>
      <td>0.70%</td>
      <td>20155</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-05</th>
      <th>ES</th>
      <td>20611</td>
      <td>309</td>
      <td>389</td>
      <td>138</td>
      <td>138</td>
      <td>2.82</td>
      <td>0.67%</td>
      <td>20611</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-04</th>
      <th>ES</th>
      <td>21369</td>
      <td>343</td>
      <td>535</td>
      <td>156</td>
      <td>156</td>
      <td>3.43</td>
      <td>0.73%</td>
      <td>21369</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-03</th>
      <th>ES</th>
      <td>22122</td>
      <td>399</td>
      <td>540</td>
      <td>149</td>
      <td>149</td>
      <td>3.62</td>
      <td>0.67%</td>
      <td>22122</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-02</th>
      <th>ES</th>
      <td>22990</td>
      <td>398</td>
      <td>356</td>
      <td>128</td>
      <td>128</td>
      <td>2.78</td>
      <td>0.56%</td>
      <td>22990</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-01</th>
      <th>ES</th>
      <td>23802</td>
      <td>359</td>
      <td>245</td>
      <td>95</td>
      <td>95</td>
      <td>2.58</td>
      <td>0.40%</td>
      <td>23802</td>
      <td>3923</td>
      <td>211</td>
      <td>0.89%</td>
    </tr>
    <tr>
      <th>2021-07-31</th>
      <th>ES</th>
      <td>23802</td>
      <td>248</td>
      <td>379</td>
      <td>131</td>
      <td>131</td>
      <td>2.89</td>
      <td>0.55%</td>
      <td>23802</td>
      <td>3923</td>
      <td>211</td>
      <td>0.89%</td>
    </tr>
    <tr>
      <th>2021-07-30</th>
      <th>ES</th>
      <td>23802</td>
      <td>192</td>
      <td>629</td>
      <td>209</td>
      <td>209</td>
      <td>3.01</td>
      <td>0.88%</td>
      <td>23802</td>
      <td>3923</td>
      <td>211</td>
      <td>0.89%</td>
    </tr>
    <tr>
      <th>2021-07-29</th>
      <th>ES</th>
      <td>24719</td>
      <td>152</td>
      <td>659</td>
      <td>213</td>
      <td>213</td>
      <td>3.09</td>
      <td>0.86%</td>
      <td>24719</td>
      <td>3923</td>
      <td>211</td>
      <td>0.85%</td>
    </tr>
    <tr>
      <th>2021-07-28</th>
      <th>ES</th>
      <td>25126</td>
      <td>107</td>
      <td>650</td>
      <td>203</td>
      <td>203</td>
      <td>3.20</td>
      <td>0.81%</td>
      <td>25126</td>
      <td>3923</td>
      <td>211</td>
      <td>0.84%</td>
    </tr>
    <tr>
      <th>2021-07-27</th>
      <th>ES</th>
      <td>25617</td>
      <td>103</td>
      <td>963</td>
      <td>318</td>
      <td>318</td>
      <td>3.03</td>
      <td>1.24%</td>
      <td>25617</td>
      <td>3923</td>
      <td>211</td>
      <td>0.82%</td>
    </tr>
    <tr>
      <th>2021-07-26</th>
      <th>ES</th>
      <td>25743</td>
      <td>124</td>
      <td>588</td>
      <td>201</td>
      <td>201</td>
      <td>2.93</td>
      <td>0.78%</td>
      <td>25743</td>
      <td>3923</td>
      <td>211</td>
      <td>0.82%</td>
    </tr>
    <tr>
      <th>2021-07-25</th>
      <th>ES</th>
      <td>25744</td>
      <td>147</td>
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
      <td>166</td>
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
      <td>197</td>
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
      <td>198</td>
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
      <td>194</td>
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
      <td>174</td>
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
      <td>198</td>
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
      <td>213</td>
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
      <td>253</td>
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
      <td>244</td>
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
      <th>2021-08-10</th>
      <td>46</td>
      <td>725</td>
      <td>303</td>
      <td>3</td>
      <td>143</td>
      <td>537</td>
      <td>0</td>
      <td>930</td>
    </tr>
    <tr>
      <th>2021-08-09</th>
      <td>72</td>
      <td>1215</td>
      <td>585</td>
      <td>10</td>
      <td>131</td>
      <td>1279</td>
      <td>32</td>
      <td>1673</td>
    </tr>
    <tr>
      <th>2021-08-08</th>
      <td>95</td>
      <td>1311</td>
      <td>489</td>
      <td>13</td>
      <td>144</td>
      <td>1577</td>
      <td>60</td>
      <td>1919</td>
    </tr>
    <tr>
      <th>2021-08-07</th>
      <td>128</td>
      <td>1830</td>
      <td>756</td>
      <td>17</td>
      <td>185</td>
      <td>2236</td>
      <td>100</td>
      <td>2564</td>
    </tr>
    <tr>
      <th>2021-08-06</th>
      <td>151</td>
      <td>2420</td>
      <td>1106</td>
      <td>21</td>
      <td>258</td>
      <td>3005</td>
      <td>122</td>
      <td>3307</td>
    </tr>
    <tr>
      <th>2021-08-05</th>
      <td>170</td>
      <td>2770</td>
      <td>1220</td>
      <td>21</td>
      <td>309</td>
      <td>3573</td>
      <td>154</td>
      <td>3858</td>
    </tr>
    <tr>
      <th>2021-08-04</th>
      <td>180</td>
      <td>3127</td>
      <td>1378</td>
      <td>19</td>
      <td>343</td>
      <td>4104</td>
      <td>165</td>
      <td>4380</td>
    </tr>
    <tr>
      <th>2021-08-03</th>
      <td>183</td>
      <td>3548</td>
      <td>1656</td>
      <td>14</td>
      <td>399</td>
      <td>4684</td>
      <td>172</td>
      <td>4948</td>
    </tr>
    <tr>
      <th>2021-08-02</th>
      <td>178</td>
      <td>3610</td>
      <td>1672</td>
      <td>12</td>
      <td>398</td>
      <td>4896</td>
      <td>176</td>
      <td>5154</td>
    </tr>
    <tr>
      <th>2021-08-01</th>
      <td>172</td>
      <td>3445</td>
      <td>1568</td>
      <td>8</td>
      <td>359</td>
      <td>4871</td>
      <td>185</td>
      <td>5129</td>
    </tr>
    <tr>
      <th>2021-07-31</th>
      <td>129</td>
      <td>3756</td>
      <td>1588</td>
      <td>4</td>
      <td>248</td>
      <td>4724</td>
      <td>170</td>
      <td>5605</td>
    </tr>
    <tr>
      <th>2021-07-30</th>
      <td>88</td>
      <td>4068</td>
      <td>1495</td>
      <td>2</td>
      <td>192</td>
      <td>4328</td>
      <td>148</td>
      <td>6109</td>
    </tr>
    <tr>
      <th>2021-07-29</th>
      <td>61</td>
      <td>4241</td>
      <td>1421</td>
      <td>1</td>
      <td>152</td>
      <td>3973</td>
      <td>129</td>
      <td>6494</td>
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
      <td>4.5%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>97.6%</td>
      <td>-</td>
      <td>100.0%</td>
      <td></td>
      <td>89.3%</td>
      <td>64.8%</td>
      <td>0.1%</td>
      <td>62.9%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>42.2%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>34.8%</td>
      <td></td>
      <td>29.3%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EE</th>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
      <td></td>
      <td>0.2%</td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES</th>
      <td></td>
      <td>8.1%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>7.4%</td>
      <td></td>
      <td>5.6%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>78.7%</td>
      <td>100.0%</td>
      <td>55.9%</td>
      <td>100.0%</td>
      <td>-</td>
      <td>100.0%</td>
      <td>82.5%</td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>3.7%</td>
      <td>-</td>
      <td>3.1%</td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>90.7%</td>
      <td>100.0%</td>
      <td></td>
      <td>89.3%</td>
      <td>98.1%</td>
      <td>100.0%</td>
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
