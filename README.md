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

- [Report 2021-10-17@13](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-10-17</th>
      <th>ES</th>
      <td>1124</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1.00</td>
      <td>0.36%</td>
      <td>1124</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-10-16</th>
      <th>ES</th>
      <td>1538</td>
      <td>7</td>
      <td>23</td>
      <td>7</td>
      <td>7</td>
      <td>3.29</td>
      <td>0.46%</td>
      <td>1538</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-10-15</th>
      <th>ES</th>
      <td>1538</td>
      <td>17</td>
      <td>51</td>
      <td>14</td>
      <td>14</td>
      <td>3.64</td>
      <td>0.91%</td>
      <td>1538</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-10-14</th>
      <th>ES</th>
      <td>1547</td>
      <td>28</td>
      <td>34</td>
      <td>15</td>
      <td>15</td>
      <td>2.27</td>
      <td>0.97%</td>
      <td>1547</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-10-13</th>
      <th>ES</th>
      <td>1529</td>
      <td>24</td>
      <td>30</td>
      <td>8</td>
      <td>8</td>
      <td>3.75</td>
      <td>0.52%</td>
      <td>1529</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-10-12</th>
      <th>ES</th>
      <td>1464</td>
      <td>24</td>
      <td>10</td>
      <td>4</td>
      <td>4</td>
      <td>2.50</td>
      <td>0.27%</td>
      <td>1464</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-10-11</th>
      <th>ES</th>
      <td>1721</td>
      <td>25</td>
      <td>10</td>
      <td>4</td>
      <td>4</td>
      <td>2.50</td>
      <td>0.23%</td>
      <td>1721</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-10-10</th>
      <th>ES</th>
      <td>1784</td>
      <td>20</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1.00</td>
      <td>0.11%</td>
      <td>1784</td>
      <td>3758</td>
      <td>10</td>
      <td>0.56%</td>
    </tr>
    <tr>
      <th>2021-10-09</th>
      <th>ES</th>
      <td>1784</td>
      <td>12</td>
      <td>7</td>
      <td>5</td>
      <td>5</td>
      <td>1.40</td>
      <td>0.28%</td>
      <td>1784</td>
      <td>3758</td>
      <td>10</td>
      <td>0.56%</td>
    </tr>
    <tr>
      <th>2021-10-08</th>
      <th>ES</th>
      <td>1784</td>
      <td>23</td>
      <td>57</td>
      <td>18</td>
      <td>18</td>
      <td>3.17</td>
      <td>1.01%</td>
      <td>1784</td>
      <td>3758</td>
      <td>10</td>
      <td>0.56%</td>
    </tr>
    <tr>
      <th>2021-10-07</th>
      <th>ES</th>
      <td>1746</td>
      <td>17</td>
      <td>18</td>
      <td>9</td>
      <td>9</td>
      <td>2.00</td>
      <td>0.52%</td>
      <td>1746</td>
      <td>3758</td>
      <td>10</td>
      <td>0.57%</td>
    </tr>
    <tr>
      <th>2021-10-06</th>
      <th>ES</th>
      <td>1830</td>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>9</td>
      <td>2.89</td>
      <td>0.49%</td>
      <td>1830</td>
      <td>3758</td>
      <td>10</td>
      <td>0.55%</td>
    </tr>
    <tr>
      <th>2021-10-05</th>
      <th>ES</th>
      <td>1896</td>
      <td>9</td>
      <td>70</td>
      <td>17</td>
      <td>17</td>
      <td>4.12</td>
      <td>0.90%</td>
      <td>1896</td>
      <td>3758</td>
      <td>10</td>
      <td>0.53%</td>
    </tr>
    <tr>
      <th>2021-10-04</th>
      <th>ES</th>
      <td>1966</td>
      <td>5</td>
      <td>20</td>
      <td>12</td>
      <td>12</td>
      <td>1.67</td>
      <td>0.61%</td>
      <td>1966</td>
      <td>3758</td>
      <td>10</td>
      <td>0.51%</td>
    </tr>
    <tr>
      <th>2021-10-03</th>
      <th>ES</th>
      <td>2075</td>
      <td>6</td>
      <td>11</td>
      <td>5</td>
      <td>5</td>
      <td>2.20</td>
      <td>0.24%</td>
      <td>2075</td>
      <td>2169</td>
      <td>13</td>
      <td>0.63%</td>
    </tr>
    <tr>
      <th>2021-10-02</th>
      <th>ES</th>
      <td>2075</td>
      <td>7</td>
      <td>45</td>
      <td>9</td>
      <td>9</td>
      <td>5.00</td>
      <td>0.43%</td>
      <td>2075</td>
      <td>2169</td>
      <td>13</td>
      <td>0.63%</td>
    </tr>
    <tr>
      <th>2021-10-01</th>
      <th>ES</th>
      <td>2075</td>
      <td>10</td>
      <td>31</td>
      <td>14</td>
      <td>14</td>
      <td>2.21</td>
      <td>0.67%</td>
      <td>2075</td>
      <td>2169</td>
      <td>13</td>
      <td>0.63%</td>
    </tr>
    <tr>
      <th>2021-09-30</th>
      <th>ES</th>
      <td>2177</td>
      <td>7</td>
      <td>45</td>
      <td>23</td>
      <td>23</td>
      <td>1.96</td>
      <td>1.06%</td>
      <td>2177</td>
      <td>2169</td>
      <td>13</td>
      <td>0.60%</td>
    </tr>
    <tr>
      <th>2021-09-29</th>
      <th>ES</th>
      <td>2267</td>
      <td>4</td>
      <td>33</td>
      <td>10</td>
      <td>10</td>
      <td>3.30</td>
      <td>0.44%</td>
      <td>2267</td>
      <td>2169</td>
      <td>13</td>
      <td>0.57%</td>
    </tr>
    <tr>
      <th>2021-09-28</th>
      <th>ES</th>
      <td>2278</td>
      <td>9</td>
      <td>26</td>
      <td>17</td>
      <td>17</td>
      <td>1.53</td>
      <td>0.75%</td>
      <td>2278</td>
      <td>2169</td>
      <td>13</td>
      <td>0.57%</td>
    </tr>
    <tr>
      <th>2021-09-27</th>
      <th>ES</th>
      <td>2301</td>
      <td>11</td>
      <td>26</td>
      <td>12</td>
      <td>12</td>
      <td>2.17</td>
      <td>0.52%</td>
      <td>2301</td>
      <td>2169</td>
      <td>13</td>
      <td>0.56%</td>
    </tr>
    <tr>
      <th>2021-09-26</th>
      <th>ES</th>
      <td>2436</td>
      <td>11</td>
      <td>15</td>
      <td>8</td>
      <td>8</td>
      <td>1.88</td>
      <td>0.33%</td>
      <td>2436</td>
      <td>2278</td>
      <td>15</td>
      <td>0.62%</td>
    </tr>
    <tr>
      <th>2021-09-25</th>
      <th>ES</th>
      <td>2436</td>
      <td>12</td>
      <td>17</td>
      <td>7</td>
      <td>7</td>
      <td>2.43</td>
      <td>0.29%</td>
      <td>2436</td>
      <td>2278</td>
      <td>15</td>
      <td>0.62%</td>
    </tr>
    <tr>
      <th>2021-09-24</th>
      <th>ES</th>
      <td>2436</td>
      <td>8</td>
      <td>56</td>
      <td>14</td>
      <td>14</td>
      <td>4.00</td>
      <td>0.57%</td>
      <td>2436</td>
      <td>2278</td>
      <td>15</td>
      <td>0.62%</td>
    </tr>
    <tr>
      <th>2021-09-23</th>
      <th>ES</th>
      <td>2504</td>
      <td>7</td>
      <td>71</td>
      <td>18</td>
      <td>18</td>
      <td>3.94</td>
      <td>0.72%</td>
      <td>2504</td>
      <td>2278</td>
      <td>15</td>
      <td>0.60%</td>
    </tr>
    <tr>
      <th>2021-09-22</th>
      <th>ES</th>
      <td>2654</td>
      <td>7</td>
      <td>68</td>
      <td>22</td>
      <td>22</td>
      <td>3.09</td>
      <td>0.83%</td>
      <td>2654</td>
      <td>2278</td>
      <td>15</td>
      <td>0.57%</td>
    </tr>
    <tr>
      <th>2021-09-21</th>
      <th>ES</th>
      <td>2780</td>
      <td>2</td>
      <td>48</td>
      <td>14</td>
      <td>14</td>
      <td>3.43</td>
      <td>0.50%</td>
      <td>2780</td>
      <td>2278</td>
      <td>15</td>
      <td>0.54%</td>
    </tr>
    <tr>
      <th>2021-09-20</th>
      <th>ES</th>
      <td>2896</td>
      <td>7</td>
      <td>45</td>
      <td>18</td>
      <td>18</td>
      <td>2.50</td>
      <td>0.62%</td>
      <td>2896</td>
      <td>2278</td>
      <td>15</td>
      <td>0.52%</td>
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
      <th>2021-10-17</th>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>4</td>
      <td>6</td>
      <td>0</td>
      <td>96</td>
    </tr>
    <tr>
      <th>2021-10-16</th>
      <td>41</td>
      <td>1171</td>
      <td>1145</td>
      <td>31</td>
      <td>7</td>
      <td>1537</td>
      <td>0</td>
      <td>2062</td>
    </tr>
    <tr>
      <th>2021-10-15</th>
      <td>65</td>
      <td>3010</td>
      <td>2206</td>
      <td>55</td>
      <td>17</td>
      <td>3310</td>
      <td>14</td>
      <td>3765</td>
    </tr>
    <tr>
      <th>2021-10-14</th>
      <td>99</td>
      <td>4234</td>
      <td>2983</td>
      <td>76</td>
      <td>28</td>
      <td>4709</td>
      <td>31</td>
      <td>5102</td>
    </tr>
    <tr>
      <th>2021-10-13</th>
      <td>118</td>
      <td>5390</td>
      <td>3740</td>
      <td>87</td>
      <td>24</td>
      <td>5997</td>
      <td>43</td>
      <td>5200</td>
    </tr>
    <tr>
      <th>2021-10-12</th>
      <td>131</td>
      <td>6652</td>
      <td>4680</td>
      <td>98</td>
      <td>24</td>
      <td>7423</td>
      <td>59</td>
      <td>5197</td>
    </tr>
    <tr>
      <th>2021-10-11</th>
      <td>133</td>
      <td>6710</td>
      <td>4651</td>
      <td>95</td>
      <td>25</td>
      <td>7601</td>
      <td>72</td>
      <td>5357</td>
    </tr>
    <tr>
      <th>2021-10-10</th>
      <td>130</td>
      <td>6422</td>
      <td>4396</td>
      <td>90</td>
      <td>20</td>
      <td>7383</td>
      <td>80</td>
      <td>5478</td>
    </tr>
    <tr>
      <th>2021-10-09</th>
      <td>122</td>
      <td>7087</td>
      <td>5091</td>
      <td>92</td>
      <td>12</td>
      <td>8167</td>
      <td>75</td>
      <td>5607</td>
    </tr>
    <tr>
      <th>2021-10-08</th>
      <td>124</td>
      <td>8092</td>
      <td>6010</td>
      <td>81</td>
      <td>23</td>
      <td>9287</td>
      <td>78</td>
      <td>5743</td>
    </tr>
    <tr>
      <th>2021-10-07</th>
      <td>105</td>
      <td>8420</td>
      <td>6322</td>
      <td>81</td>
      <td>17</td>
      <td>9733</td>
      <td>81</td>
      <td>5852</td>
    </tr>
    <tr>
      <th>2021-10-06</th>
      <td>75</td>
      <td>9039</td>
      <td>5814</td>
      <td>67</td>
      <td>10</td>
      <td>9098</td>
      <td>84</td>
      <td>5919</td>
    </tr>
    <tr>
      <th>2021-10-05</th>
      <td>50</td>
      <td>9828</td>
      <td>5464</td>
      <td>61</td>
      <td>9</td>
      <td>8444</td>
      <td>70</td>
      <td>6034</td>
    </tr>
    <tr>
      <th>2021-10-04</th>
      <td>33</td>
      <td>9689</td>
      <td>5269</td>
      <td>51</td>
      <td>5</td>
      <td>8014</td>
      <td>56</td>
      <td>6069</td>
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
      <td>1.3%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>93.1%</td>
      <td>-</td>
      <td>99.9%</td>
      <td></td>
      <td>91.1%</td>
      <td>84.3%</td>
      <td>0.8%</td>
      <td>77.4%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>67.3%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>63.7%</td>
      <td></td>
      <td>60.2%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EE</th>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
      <td></td>
      <td>0.6%</td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES</th>
      <td></td>
      <td>0.2%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>0.2%</td>
      <td></td>
      <td>0.2%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>89.2%</td>
      <td>100.0%</td>
      <td>53.7%</td>
      <td>100.0%</td>
      <td>-</td>
      <td>100.0%</td>
      <td>92.2%</td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.8%</td>
      <td>-</td>
      <td>0.8%</td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>60.9%</td>
      <td>70.3%</td>
      <td></td>
      <td>58.2%</td>
      <td>68.6%</td>
      <td>69.0%</td>
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
