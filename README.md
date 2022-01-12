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

- [Report 2022-01-12@17](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2022-01-12</th>
      <th>ES</th>
      <td>134942</td>
      <td>305</td>
      <td>1252</td>
      <td>305</td>
      <td>380</td>
      <td>3.29</td>
      <td>0.28%</td>
      <td>134942</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-11</th>
      <th>ES</th>
      <td>115279</td>
      <td>1194</td>
      <td>2652</td>
      <td>814</td>
      <td>814</td>
      <td>3.26</td>
      <td>0.71%</td>
      <td>115279</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-10</th>
      <th>ES</th>
      <td>112827</td>
      <td>1327</td>
      <td>1941</td>
      <td>627</td>
      <td>627</td>
      <td>3.10</td>
      <td>0.56%</td>
      <td>112827</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2022-01-09</th>
      <th>ES</th>
      <td>124309</td>
      <td>1296</td>
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
      <td>1474</td>
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
      <td>1713</td>
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
      <td>1486</td>
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
      <td>2125</td>
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
      <td>2695</td>
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
      <td>2153</td>
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
      <td>1573</td>
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
      <td>1157</td>
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
    <tr>
      <th>2021-12-25</th>
      <th>ES</th>
      <td>37497</td>
      <td>626</td>
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
      <td>668</td>
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
      <td>680</td>
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
      <td>596</td>
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
      <td>542</td>
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
      <th>2022-01-12</th>
      <td>697</td>
      <td>0</td>
      <td>0</td>
      <td>27</td>
      <td>305</td>
      <td>0</td>
      <td>0</td>
      <td>5632</td>
    </tr>
    <tr>
      <th>2022-01-11</th>
      <td>1798</td>
      <td>24155</td>
      <td>0</td>
      <td>63</td>
      <td>1194</td>
      <td>0</td>
      <td>0</td>
      <td>6285</td>
    </tr>
    <tr>
      <th>2022-01-10</th>
      <td>2392</td>
      <td>35849</td>
      <td>0</td>
      <td>94</td>
      <td>1327</td>
      <td>0</td>
      <td>215</td>
      <td>6294</td>
    </tr>
    <tr>
      <th>2022-01-09</th>
      <td>2804</td>
      <td>39161</td>
      <td>0</td>
      <td>109</td>
      <td>1296</td>
      <td>0</td>
      <td>895</td>
      <td>6680</td>
    </tr>
    <tr>
      <th>2022-01-08</th>
      <td>3260</td>
      <td>50840</td>
      <td>0</td>
      <td>124</td>
      <td>1474</td>
      <td>0</td>
      <td>1320</td>
      <td>6655</td>
    </tr>
    <tr>
      <th>2022-01-07</th>
      <td>4024</td>
      <td>63758</td>
      <td>0</td>
      <td>128</td>
      <td>1713</td>
      <td>0</td>
      <td>1660</td>
      <td>6610</td>
    </tr>
    <tr>
      <th>2022-01-06</th>
      <td>4454</td>
      <td>72578</td>
      <td>127</td>
      <td>135</td>
      <td>1486</td>
      <td>0</td>
      <td>2243</td>
      <td>6620</td>
    </tr>
    <tr>
      <th>2022-01-05</th>
      <td>4942</td>
      <td>84795</td>
      <td>16022</td>
      <td>134</td>
      <td>2125</td>
      <td>582</td>
      <td>2703</td>
      <td>6607</td>
    </tr>
    <tr>
      <th>2022-01-04</th>
      <td>5077</td>
      <td>96499</td>
      <td>28797</td>
      <td>133</td>
      <td>2695</td>
      <td>22666</td>
      <td>3521</td>
      <td>6587</td>
    </tr>
    <tr>
      <th>2022-01-03</th>
      <td>4340</td>
      <td>96015</td>
      <td>30754</td>
      <td>132</td>
      <td>2153</td>
      <td>31545</td>
      <td>3928</td>
      <td>6567</td>
    </tr>
    <tr>
      <th>2022-01-02</th>
      <td>3547</td>
      <td>92850</td>
      <td>27976</td>
      <td>123</td>
      <td>1573</td>
      <td>31455</td>
      <td>4072</td>
      <td>6557</td>
    </tr>
    <tr>
      <th>2022-01-01</th>
      <td>2551</td>
      <td>92877</td>
      <td>25921</td>
      <td>103</td>
      <td>1157</td>
      <td>29241</td>
      <td>3972</td>
      <td>6545</td>
    </tr>
    <tr>
      <th>2021-12-31</th>
      <td>1494</td>
      <td>97898</td>
      <td>0</td>
      <td>93</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6528</td>
    </tr>
    <tr>
      <th>2021-12-30</th>
      <td>869</td>
      <td>104530</td>
      <td>0</td>
      <td>87</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6527</td>
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
      <td>4.0%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>89.9%</td>
      <td>-</td>
      <td>100.0%</td>
      <td></td>
      <td>81.5%</td>
      <td>75.3%</td>
      <td>0.5%</td>
      <td>1.8%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>13.6%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>61.8%</td>
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
      <td>1.6%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>4.4%</td>
      <td></td>
      <td>0.9%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>9.1%</td>
      <td>55.0%</td>
      <td>7.5%</td>
      <td>27.8%</td>
      <td>-</td>
      <td>12.6%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>2.7%</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>0.2%</td>
      <td></td>
      <td></td>
      <td>4.2%</td>
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
