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

- [Report 2021-12-06@05](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-12-06</th>
      <th>ES</th>
      <td>4579</td>
      <td>1</td>
      <td>12</td>
      <td>1</td>
      <td>9</td>
      <td>1.33</td>
      <td>0.20%</td>
      <td>4579</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-05</th>
      <th>ES</th>
      <td>10278</td>
      <td>104</td>
      <td>288</td>
      <td>95</td>
      <td>95</td>
      <td>3.03</td>
      <td>0.92%</td>
      <td>10278</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-04</th>
      <th>ES</th>
      <td>10278</td>
      <td>171</td>
      <td>421</td>
      <td>121</td>
      <td>121</td>
      <td>3.48</td>
      <td>1.18%</td>
      <td>10278</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-03</th>
      <th>ES</th>
      <td>10278</td>
      <td>270</td>
      <td>472</td>
      <td>141</td>
      <td>141</td>
      <td>3.35</td>
      <td>1.37%</td>
      <td>10278</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-02</th>
      <th>ES</th>
      <td>9731</td>
      <td>353</td>
      <td>538</td>
      <td>158</td>
      <td>158</td>
      <td>3.41</td>
      <td>1.62%</td>
      <td>9731</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-12-01</th>
      <th>ES</th>
      <td>8983</td>
      <td>385</td>
      <td>514</td>
      <td>151</td>
      <td>151</td>
      <td>3.40</td>
      <td>1.68%</td>
      <td>8983</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-11-30</th>
      <th>ES</th>
      <td>8696</td>
      <td>387</td>
      <td>423</td>
      <td>104</td>
      <td>108</td>
      <td>3.92</td>
      <td>1.24%</td>
      <td>8696</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-11-29</th>
      <th>ES</th>
      <td>8198</td>
      <td>439</td>
      <td>418</td>
      <td>113</td>
      <td>113</td>
      <td>3.70</td>
      <td>1.38%</td>
      <td>8198</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-11-28</th>
      <th>ES</th>
      <td>7193</td>
      <td>332</td>
      <td>132</td>
      <td>43</td>
      <td>43</td>
      <td>3.07</td>
      <td>0.60%</td>
      <td>7193</td>
      <td>4007</td>
      <td>82</td>
      <td>1.14%</td>
    </tr>
    <tr>
      <th>2021-11-27</th>
      <th>ES</th>
      <td>7193</td>
      <td>295</td>
      <td>181</td>
      <td>59</td>
      <td>59</td>
      <td>3.07</td>
      <td>0.82%</td>
      <td>7193</td>
      <td>4007</td>
      <td>82</td>
      <td>1.14%</td>
    </tr>
    <tr>
      <th>2021-11-26</th>
      <th>ES</th>
      <td>7193</td>
      <td>293</td>
      <td>287</td>
      <td>85</td>
      <td>85</td>
      <td>3.38</td>
      <td>1.18%</td>
      <td>7193</td>
      <td>4007</td>
      <td>82</td>
      <td>1.14%</td>
    </tr>
    <tr>
      <th>2021-11-25</th>
      <th>ES</th>
      <td>6725</td>
      <td>185</td>
      <td>288</td>
      <td>108</td>
      <td>108</td>
      <td>2.67</td>
      <td>1.61%</td>
      <td>6725</td>
      <td>4007</td>
      <td>82</td>
      <td>1.22%</td>
    </tr>
    <tr>
      <th>2021-11-24</th>
      <th>ES</th>
      <td>6304</td>
      <td>153</td>
      <td>219</td>
      <td>88</td>
      <td>88</td>
      <td>2.49</td>
      <td>1.40%</td>
      <td>6304</td>
      <td>4007</td>
      <td>82</td>
      <td>1.30%</td>
    </tr>
    <tr>
      <th>2021-11-23</th>
      <th>ES</th>
      <td>6039</td>
      <td>120</td>
      <td>209</td>
      <td>76</td>
      <td>76</td>
      <td>2.75</td>
      <td>1.26%</td>
      <td>6039</td>
      <td>4007</td>
      <td>82</td>
      <td>1.36%</td>
    </tr>
    <tr>
      <th>2021-11-22</th>
      <th>ES</th>
      <td>5655</td>
      <td>89</td>
      <td>151</td>
      <td>60</td>
      <td>60</td>
      <td>2.52</td>
      <td>1.06%</td>
      <td>5655</td>
      <td>4007</td>
      <td>82</td>
      <td>1.45%</td>
    </tr>
    <tr>
      <th>2021-11-21</th>
      <th>ES</th>
      <td>4787</td>
      <td>86</td>
      <td>184</td>
      <td>49</td>
      <td>49</td>
      <td>3.76</td>
      <td>1.02%</td>
      <td>4787</td>
      <td>2694</td>
      <td>57</td>
      <td>1.19%</td>
    </tr>
    <tr>
      <th>2021-11-20</th>
      <th>ES</th>
      <td>4787</td>
      <td>59</td>
      <td>143</td>
      <td>46</td>
      <td>46</td>
      <td>3.11</td>
      <td>0.96%</td>
      <td>4787</td>
      <td>2694</td>
      <td>57</td>
      <td>1.19%</td>
    </tr>
    <tr>
      <th>2021-11-19</th>
      <th>ES</th>
      <td>4787</td>
      <td>40</td>
      <td>148</td>
      <td>55</td>
      <td>55</td>
      <td>2.69</td>
      <td>1.15%</td>
      <td>4787</td>
      <td>2694</td>
      <td>57</td>
      <td>1.19%</td>
    </tr>
    <tr>
      <th>2021-11-18</th>
      <th>ES</th>
      <td>4461</td>
      <td>35</td>
      <td>194</td>
      <td>65</td>
      <td>65</td>
      <td>2.98</td>
      <td>1.46%</td>
      <td>4461</td>
      <td>2694</td>
      <td>57</td>
      <td>1.28%</td>
    </tr>
    <tr>
      <th>2021-11-17</th>
      <th>ES</th>
      <td>4171</td>
      <td>13</td>
      <td>219</td>
      <td>47</td>
      <td>47</td>
      <td>4.66</td>
      <td>1.13%</td>
      <td>4171</td>
      <td>2694</td>
      <td>57</td>
      <td>1.37%</td>
    </tr>
    <tr>
      <th>2021-11-16</th>
      <th>ES</th>
      <td>4141</td>
      <td>7</td>
      <td>204</td>
      <td>52</td>
      <td>52</td>
      <td>3.92</td>
      <td>1.26%</td>
      <td>4141</td>
      <td>2694</td>
      <td>57</td>
      <td>1.38%</td>
    </tr>
    <tr>
      <th>2021-11-15</th>
      <th>ES</th>
      <td>3557</td>
      <td>3</td>
      <td>125</td>
      <td>42</td>
      <td>42</td>
      <td>2.98</td>
      <td>1.18%</td>
      <td>3557</td>
      <td>2694</td>
      <td>57</td>
      <td>1.60%</td>
    </tr>
    <tr>
      <th>2021-11-14</th>
      <th>ES</th>
      <td>3074</td>
      <td>2</td>
      <td>58</td>
      <td>20</td>
      <td>20</td>
      <td>2.90</td>
      <td>0.65%</td>
      <td>3074</td>
      <td>2922</td>
      <td>33</td>
      <td>1.07%</td>
    </tr>
    <tr>
      <th>2021-11-13</th>
      <th>ES</th>
      <td>3074</td>
      <td>1</td>
      <td>80</td>
      <td>24</td>
      <td>24</td>
      <td>3.33</td>
      <td>0.78%</td>
      <td>3074</td>
      <td>2922</td>
      <td>33</td>
      <td>1.07%</td>
    </tr>
    <tr>
      <th>2021-11-12</th>
      <th>ES</th>
      <td>3074</td>
      <td>4</td>
      <td>183</td>
      <td>48</td>
      <td>48</td>
      <td>3.81</td>
      <td>1.56%</td>
      <td>3074</td>
      <td>2922</td>
      <td>33</td>
      <td>1.07%</td>
    </tr>
    <tr>
      <th>2021-11-11</th>
      <th>ES</th>
      <td>2894</td>
      <td>6</td>
      <td>89</td>
      <td>34</td>
      <td>34</td>
      <td>2.62</td>
      <td>1.17%</td>
      <td>2894</td>
      <td>2922</td>
      <td>33</td>
      <td>1.14%</td>
    </tr>
    <tr>
      <th>2021-11-10</th>
      <th>ES</th>
      <td>2752</td>
      <td>5</td>
      <td>151</td>
      <td>42</td>
      <td>42</td>
      <td>3.60</td>
      <td>1.53%</td>
      <td>2752</td>
      <td>2922</td>
      <td>33</td>
      <td>1.20%</td>
    </tr>
    <tr>
      <th>2021-11-09</th>
      <th>ES</th>
      <td>2155</td>
      <td>1</td>
      <td>78</td>
      <td>21</td>
      <td>21</td>
      <td>3.71</td>
      <td>0.97%</td>
      <td>2155</td>
      <td>2922</td>
      <td>33</td>
      <td>1.53%</td>
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
      <th>2021-12-06</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2021-12-05</th>
      <td>295</td>
      <td>4176</td>
      <td>1331</td>
      <td>4</td>
      <td>104</td>
      <td>2115</td>
      <td>0</td>
      <td>4719</td>
    </tr>
    <tr>
      <th>2021-12-04</th>
      <td>581</td>
      <td>13576</td>
      <td>9467</td>
      <td>8</td>
      <td>171</td>
      <td>12140</td>
      <td>41</td>
      <td>5504</td>
    </tr>
    <tr>
      <th>2021-12-03</th>
      <td>908</td>
      <td>23975</td>
      <td>18233</td>
      <td>12</td>
      <td>270</td>
      <td>22986</td>
      <td>156</td>
      <td>5534</td>
    </tr>
    <tr>
      <th>2021-12-02</th>
      <td>1133</td>
      <td>32040</td>
      <td>24682</td>
      <td>21</td>
      <td>353</td>
      <td>31690</td>
      <td>270</td>
      <td>5554</td>
    </tr>
    <tr>
      <th>2021-12-01</th>
      <td>1331</td>
      <td>40609</td>
      <td>31888</td>
      <td>25</td>
      <td>385</td>
      <td>40771</td>
      <td>338</td>
      <td>5748</td>
    </tr>
    <tr>
      <th>2021-11-30</th>
      <td>1523</td>
      <td>49342</td>
      <td>39378</td>
      <td>33</td>
      <td>387</td>
      <td>49894</td>
      <td>387</td>
      <td>5928</td>
    </tr>
    <tr>
      <th>2021-11-29</th>
      <td>1553</td>
      <td>49749</td>
      <td>39026</td>
      <td>35</td>
      <td>439</td>
      <td>50716</td>
      <td>401</td>
      <td>6047</td>
    </tr>
    <tr>
      <th>2021-11-28</th>
      <td>1536</td>
      <td>48585</td>
      <td>37657</td>
      <td>27</td>
      <td>332</td>
      <td>50080</td>
      <td>410</td>
      <td>6288</td>
    </tr>
    <tr>
      <th>2021-11-27</th>
      <td>1425</td>
      <td>56509</td>
      <td>45235</td>
      <td>29</td>
      <td>295</td>
      <td>58432</td>
      <td>417</td>
      <td>6355</td>
    </tr>
    <tr>
      <th>2021-11-26</th>
      <td>1365</td>
      <td>64351</td>
      <td>52672</td>
      <td>28</td>
      <td>293</td>
      <td>66606</td>
      <td>416</td>
      <td>6496</td>
    </tr>
    <tr>
      <th>2021-11-25</th>
      <td>1080</td>
      <td>69974</td>
      <td>46982</td>
      <td>32</td>
      <td>185</td>
      <td>60446</td>
      <td>441</td>
      <td>6497</td>
    </tr>
    <tr>
      <th>2021-11-24</th>
      <td>868</td>
      <td>76365</td>
      <td>43884</td>
      <td>35</td>
      <td>153</td>
      <td>56014</td>
      <td>391</td>
      <td>6546</td>
    </tr>
    <tr>
      <th>2021-11-23</th>
      <td>654</td>
      <td>82964</td>
      <td>42031</td>
      <td>30</td>
      <td>120</td>
      <td>52728</td>
      <td>329</td>
      <td>6611</td>
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
      <td>2.3%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>99.1%</td>
      <td>-</td>
      <td>100.0%</td>
      <td></td>
      <td>88.1%</td>
      <td>90.0%</td>
      <td>0.9%</td>
      <td>78.2%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>70.6%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>78.0%</td>
      <td></td>
      <td>53.3%</td>
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
      <td>0.5%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>0.6%</td>
      <td></td>
      <td>0.6%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>81.5%</td>
      <td>100.0%</td>
      <td>68.3%</td>
      <td>100.0%</td>
      <td>-</td>
      <td>100.0%</td>
      <td>73.6%</td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.7%</td>
      <td>-</td>
      <td>0.8%</td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>9.9%</td>
      <td>9.6%</td>
      <td></td>
      <td>13.0%</td>
      <td>10.3%</td>
      <td>15.7%</td>
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
