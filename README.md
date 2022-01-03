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

- [Report 2022-01-03@19](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2022-01-03</th>
      <th>ES</th>
      <td>161688</td>
      <td>327</td>
      <td>1087</td>
      <td>327</td>
      <td>327</td>
      <td>3.32</td>
      <td>0.20%</td>
      <td>161688</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-02</th>
      <th>ES</th>
      <td>161688</td>
      <td>609</td>
      <td>1238</td>
      <td>417</td>
      <td>417</td>
      <td>2.97</td>
      <td>0.26%</td>
      <td>161688</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-01</th>
      <th>ES</th>
      <td>161688</td>
      <td>732</td>
      <td>1279</td>
      <td>379</td>
      <td>379</td>
      <td>3.37</td>
      <td>0.23%</td>
      <td>161688</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-31</th>
      <th>ES</th>
      <td>161688</td>
      <td>958</td>
      <td>1898</td>
      <td>459</td>
      <td>682</td>
      <td>2.78</td>
      <td>0.42%</td>
      <td>161688</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-30</th>
      <th>ES</th>
      <td>82391</td>
      <td>1976</td>
      <td>3295</td>
      <td>909</td>
      <td>909</td>
      <td>3.62</td>
      <td>1.10%</td>
      <td>82391</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-29</th>
      <th>ES</th>
      <td>69709</td>
      <td>1977</td>
      <td>2624</td>
      <td>708</td>
      <td>720</td>
      <td>3.64</td>
      <td>1.03%</td>
      <td>69709</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-28</th>
      <th>ES</th>
      <td>63892</td>
      <td>2802</td>
      <td>3789</td>
      <td>1244</td>
      <td>1244</td>
      <td>3.05</td>
      <td>1.95%</td>
      <td>63892</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-27</th>
      <th>ES</th>
      <td>56771</td>
      <td>2566</td>
      <td>2484</td>
      <td>819</td>
      <td>819</td>
      <td>3.03</td>
      <td>1.44%</td>
      <td>56771</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-26</th>
      <th>ES</th>
      <td>37497</td>
      <td>2247</td>
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
    <tr>
      <th>2021-12-25</th>
      <th>ES</th>
      <td>37497</td>
      <td>2215</td>
      <td>1742</td>
      <td>599</td>
      <td>599</td>
      <td>2.91</td>
      <td>1.60%</td>
      <td>37497</td>
      <td>9995</td>
      <td>946</td>
      <td>2.52%</td>
    </tr>
    <tr>
      <th>2021-12-24</th>
      <th>ES</th>
      <td>37497</td>
      <td>1601</td>
      <td>2681</td>
      <td>785</td>
      <td>785</td>
      <td>3.42</td>
      <td>2.09%</td>
      <td>37497</td>
      <td>9995</td>
      <td>946</td>
      <td>2.52%</td>
    </tr>
    <tr>
      <th>2021-12-23</th>
      <th>ES</th>
      <td>42263</td>
      <td>1092</td>
      <td>3208</td>
      <td>971</td>
      <td>971</td>
      <td>3.30</td>
      <td>2.30%</td>
      <td>42263</td>
      <td>9995</td>
      <td>946</td>
      <td>2.24%</td>
    </tr>
    <tr>
      <th>2021-12-22</th>
      <th>ES</th>
      <td>35975</td>
      <td>810</td>
      <td>2673</td>
      <td>820</td>
      <td>820</td>
      <td>3.26</td>
      <td>2.28%</td>
      <td>35975</td>
      <td>9995</td>
      <td>946</td>
      <td>2.63%</td>
    </tr>
    <tr>
      <th>2021-12-21</th>
      <th>ES</th>
      <td>31275</td>
      <td>561</td>
      <td>2348</td>
      <td>752</td>
      <td>752</td>
      <td>3.12</td>
      <td>2.40%</td>
      <td>31275</td>
      <td>9995</td>
      <td>946</td>
      <td>3.02%</td>
    </tr>
    <tr>
      <th>2021-12-20</th>
      <th>ES</th>
      <td>27891</td>
      <td>562</td>
      <td>1635</td>
      <td>562</td>
      <td>562</td>
      <td>2.91</td>
      <td>2.01%</td>
      <td>27891</td>
      <td>9995</td>
      <td>946</td>
      <td>3.39%</td>
    </tr>
    <tr>
      <th>2021-12-19</th>
      <th>ES</th>
      <td>23620</td>
      <td>669</td>
      <td>859</td>
      <td>301</td>
      <td>301</td>
      <td>2.85</td>
      <td>1.27%</td>
      <td>23620</td>
      <td>5441</td>
      <td>451</td>
      <td>1.91%</td>
    </tr>
    <tr>
      <th>2021-12-18</th>
      <th>ES</th>
      <td>23620</td>
      <td>603</td>
      <td>1242</td>
      <td>401</td>
      <td>401</td>
      <td>3.10</td>
      <td>1.70%</td>
      <td>23620</td>
      <td>5441</td>
      <td>451</td>
      <td>1.91%</td>
    </tr>
    <tr>
      <th>2021-12-17</th>
      <th>ES</th>
      <td>23620</td>
      <td>511</td>
      <td>1575</td>
      <td>476</td>
      <td>476</td>
      <td>3.31</td>
      <td>2.02%</td>
      <td>23620</td>
      <td>5441</td>
      <td>451</td>
      <td>1.91%</td>
    </tr>
    <tr>
      <th>2021-12-16</th>
      <th>ES</th>
      <td>21296</td>
      <td>466</td>
      <td>1279</td>
      <td>347</td>
      <td>347</td>
      <td>3.69</td>
      <td>1.63%</td>
      <td>21296</td>
      <td>5441</td>
      <td>451</td>
      <td>2.12%</td>
    </tr>
    <tr>
      <th>2021-12-15</th>
      <th>ES</th>
      <td>20941</td>
      <td>366</td>
      <td>1260</td>
      <td>365</td>
      <td>365</td>
      <td>3.45</td>
      <td>1.74%</td>
      <td>20941</td>
      <td>5441</td>
      <td>451</td>
      <td>2.15%</td>
    </tr>
    <tr>
      <th>2021-12-14</th>
      <th>ES</th>
      <td>17064</td>
      <td>327</td>
      <td>998</td>
      <td>277</td>
      <td>283</td>
      <td>3.53</td>
      <td>1.66%</td>
      <td>17064</td>
      <td>5441</td>
      <td>451</td>
      <td>2.64%</td>
    </tr>
    <tr>
      <th>2021-12-13</th>
      <th>ES</th>
      <td>19588</td>
      <td>340</td>
      <td>824</td>
      <td>225</td>
      <td>225</td>
      <td>3.66</td>
      <td>1.15%</td>
      <td>19588</td>
      <td>5441</td>
      <td>451</td>
      <td>2.30%</td>
    </tr>
    <tr>
      <th>2021-12-12</th>
      <th>ES</th>
      <td>12474</td>
      <td>345</td>
      <td>471</td>
      <td>145</td>
      <td>145</td>
      <td>3.25</td>
      <td>1.16%</td>
      <td>12474</td>
      <td>4643</td>
      <td>204</td>
      <td>1.64%</td>
    </tr>
    <tr>
      <th>2021-12-11</th>
      <th>ES</th>
      <td>12474</td>
      <td>343</td>
      <td>674</td>
      <td>207</td>
      <td>207</td>
      <td>3.26</td>
      <td>1.66%</td>
      <td>12474</td>
      <td>4643</td>
      <td>204</td>
      <td>1.64%</td>
    </tr>
    <tr>
      <th>2021-12-10</th>
      <th>ES</th>
      <td>12474</td>
      <td>264</td>
      <td>1045</td>
      <td>279</td>
      <td>279</td>
      <td>3.75</td>
      <td>2.24%</td>
      <td>12474</td>
      <td>4643</td>
      <td>204</td>
      <td>1.64%</td>
    </tr>
    <tr>
      <th>2021-12-09</th>
      <th>ES</th>
      <td>11994</td>
      <td>252</td>
      <td>677</td>
      <td>159</td>
      <td>159</td>
      <td>4.26</td>
      <td>1.33%</td>
      <td>11994</td>
      <td>4643</td>
      <td>204</td>
      <td>1.70%</td>
    </tr>
    <tr>
      <th>2021-12-08</th>
      <th>ES</th>
      <td>10292</td>
      <td>215</td>
      <td>488</td>
      <td>141</td>
      <td>141</td>
      <td>3.46</td>
      <td>1.37%</td>
      <td>10292</td>
      <td>4643</td>
      <td>204</td>
      <td>1.98%</td>
    </tr>
    <tr>
      <th>2021-12-07</th>
      <th>ES</th>
      <td>11797</td>
      <td>196</td>
      <td>389</td>
      <td>123</td>
      <td>123</td>
      <td>3.16</td>
      <td>1.04%</td>
      <td>11797</td>
      <td>4643</td>
      <td>204</td>
      <td>1.73%</td>
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
      <th>2022-01-03</th>
      <td>79</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>327</td>
      <td>0</td>
      <td>0</td>
      <td>5081</td>
    </tr>
    <tr>
      <th>2022-01-02</th>
      <td>164</td>
      <td>4927</td>
      <td>0</td>
      <td>23</td>
      <td>609</td>
      <td>0</td>
      <td>238</td>
      <td>7463</td>
    </tr>
    <tr>
      <th>2022-01-01</th>
      <td>217</td>
      <td>9355</td>
      <td>0</td>
      <td>31</td>
      <td>732</td>
      <td>0</td>
      <td>819</td>
      <td>8261</td>
    </tr>
    <tr>
      <th>2021-12-31</th>
      <td>352</td>
      <td>17813</td>
      <td>0</td>
      <td>47</td>
      <td>958</td>
      <td>0</td>
      <td>1279</td>
      <td>8238</td>
    </tr>
    <tr>
      <th>2021-12-30</th>
      <td>631</td>
      <td>27476</td>
      <td>0</td>
      <td>60</td>
      <td>1976</td>
      <td>0</td>
      <td>1914</td>
      <td>8530</td>
    </tr>
    <tr>
      <th>2021-12-29</th>
      <td>1058</td>
      <td>33775</td>
      <td>0</td>
      <td>72</td>
      <td>1977</td>
      <td>0</td>
      <td>2488</td>
      <td>8671</td>
    </tr>
    <tr>
      <th>2021-12-28</th>
      <td>1552</td>
      <td>41192</td>
      <td>4661</td>
      <td>80</td>
      <td>2802</td>
      <td>0</td>
      <td>2957</td>
      <td>8926</td>
    </tr>
    <tr>
      <th>2021-12-27</th>
      <td>1830</td>
      <td>42390</td>
      <td>9091</td>
      <td>78</td>
      <td>2566</td>
      <td>470</td>
      <td>3140</td>
      <td>9134</td>
    </tr>
    <tr>
      <th>2021-12-26</th>
      <td>2090</td>
      <td>41805</td>
      <td>9296</td>
      <td>74</td>
      <td>2247</td>
      <td>6278</td>
      <td>3287</td>
      <td>9446</td>
    </tr>
    <tr>
      <th>2021-12-25</th>
      <td>2372</td>
      <td>43195</td>
      <td>10774</td>
      <td>71</td>
      <td>2215</td>
      <td>11355</td>
      <td>3008</td>
      <td>9519</td>
    </tr>
    <tr>
      <th>2021-12-24</th>
      <td>1803</td>
      <td>46888</td>
      <td>11762</td>
      <td>65</td>
      <td>1601</td>
      <td>13327</td>
      <td>2645</td>
      <td>9431</td>
    </tr>
    <tr>
      <th>2021-12-23</th>
      <td>1350</td>
      <td>52409</td>
      <td>10417</td>
      <td>66</td>
      <td>1092</td>
      <td>11805</td>
      <td>2263</td>
      <td>9495</td>
    </tr>
    <tr>
      <th>2021-12-22</th>
      <td>961</td>
      <td>56474</td>
      <td>9945</td>
      <td>70</td>
      <td>810</td>
      <td>11015</td>
      <td>1856</td>
      <td>9426</td>
    </tr>
    <tr>
      <th>2021-12-21</th>
      <td>624</td>
      <td>61609</td>
      <td>9632</td>
      <td>65</td>
      <td>561</td>
      <td>10207</td>
      <td>1363</td>
      <td>9436</td>
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
      <td>3.0%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>95.8%</td>
      <td>-</td>
      <td>100.0%</td>
      <td></td>
      <td>84.9%</td>
      <td>53.7%</td>
      <td>0.5%</td>
      <td>22.2%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>15.8%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>36.0%</td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>EE</th>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
      <td></td>
      <td>0.1%</td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES</th>
      <td></td>
      <td>3.6%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>6.9%</td>
      <td></td>
      <td>1.3%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>7.2%</td>
      <td>30.7%</td>
      <td>10.8%</td>
      <td>21.6%</td>
      <td>-</td>
      <td>8.9%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>3.8%</td>
      <td>-</td>
      <td>3.8%</td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>5.6%</td>
      <td></td>
      <td></td>
      <td>7.6%</td>
      <td></td>
      <td>17.0%</td>
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
