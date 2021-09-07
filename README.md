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

- [Report 2021-09-07@12](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-09-07</th>
      <th>ES</th>
      <td>9357</td>
      <td>14</td>
      <td>48</td>
      <td>14</td>
      <td>14</td>
      <td>3.43</td>
      <td>0.15%</td>
      <td>9357</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-09-06</th>
      <th>ES</th>
      <td>5688</td>
      <td>26</td>
      <td>66</td>
      <td>18</td>
      <td>18</td>
      <td>3.67</td>
      <td>0.32%</td>
      <td>5688</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-09-05</th>
      <th>ES</th>
      <td>6564</td>
      <td>30</td>
      <td>49</td>
      <td>13</td>
      <td>13</td>
      <td>3.77</td>
      <td>0.20%</td>
      <td>6564</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-09-04</th>
      <th>ES</th>
      <td>6564</td>
      <td>53</td>
      <td>72</td>
      <td>27</td>
      <td>27</td>
      <td>2.67</td>
      <td>0.41%</td>
      <td>6564</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-09-03</th>
      <th>ES</th>
      <td>6564</td>
      <td>57</td>
      <td>80</td>
      <td>22</td>
      <td>22</td>
      <td>3.64</td>
      <td>0.34%</td>
      <td>6564</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-09-02</th>
      <th>ES</th>
      <td>7018</td>
      <td>72</td>
      <td>91</td>
      <td>28</td>
      <td>28</td>
      <td>3.25</td>
      <td>0.40%</td>
      <td>7018</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-09-01</th>
      <th>ES</th>
      <td>6668</td>
      <td>76</td>
      <td>127</td>
      <td>33</td>
      <td>33</td>
      <td>3.85</td>
      <td>0.49%</td>
      <td>6668</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-31</th>
      <th>ES</th>
      <td>7234</td>
      <td>94</td>
      <td>122</td>
      <td>40</td>
      <td>40</td>
      <td>3.05</td>
      <td>0.55%</td>
      <td>7234</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-30</th>
      <th>ES</th>
      <td>7564</td>
      <td>97</td>
      <td>109</td>
      <td>41</td>
      <td>41</td>
      <td>2.66</td>
      <td>0.54%</td>
      <td>7564</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-08-29</th>
      <th>ES</th>
      <td>8765</td>
      <td>87</td>
      <td>79</td>
      <td>22</td>
      <td>22</td>
      <td>3.59</td>
      <td>0.25%</td>
      <td>8765</td>
      <td>18096</td>
      <td>57</td>
      <td>0.65%</td>
    </tr>
    <tr>
      <th>2021-08-28</th>
      <th>ES</th>
      <td>8765</td>
      <td>82</td>
      <td>114</td>
      <td>33</td>
      <td>33</td>
      <td>3.45</td>
      <td>0.38%</td>
      <td>8765</td>
      <td>18096</td>
      <td>57</td>
      <td>0.65%</td>
    </tr>
    <tr>
      <th>2021-08-27</th>
      <th>ES</th>
      <td>8765</td>
      <td>58</td>
      <td>236</td>
      <td>71</td>
      <td>71</td>
      <td>3.32</td>
      <td>0.81%</td>
      <td>8765</td>
      <td>18096</td>
      <td>57</td>
      <td>0.65%</td>
    </tr>
    <tr>
      <th>2021-08-26</th>
      <th>ES</th>
      <td>9188</td>
      <td>47</td>
      <td>116</td>
      <td>45</td>
      <td>45</td>
      <td>2.58</td>
      <td>0.49%</td>
      <td>9188</td>
      <td>18096</td>
      <td>57</td>
      <td>0.62%</td>
    </tr>
    <tr>
      <th>2021-08-25</th>
      <th>ES</th>
      <td>9950</td>
      <td>40</td>
      <td>215</td>
      <td>79</td>
      <td>79</td>
      <td>2.72</td>
      <td>0.79%</td>
      <td>9950</td>
      <td>18096</td>
      <td>57</td>
      <td>0.57%</td>
    </tr>
    <tr>
      <th>2021-08-24</th>
      <th>ES</th>
      <td>10117</td>
      <td>31</td>
      <td>169</td>
      <td>66</td>
      <td>66</td>
      <td>2.56</td>
      <td>0.65%</td>
      <td>10117</td>
      <td>18096</td>
      <td>57</td>
      <td>0.56%</td>
    </tr>
    <tr>
      <th>2021-08-23</th>
      <th>ES</th>
      <td>10727</td>
      <td>40</td>
      <td>181</td>
      <td>61</td>
      <td>61</td>
      <td>2.97</td>
      <td>0.57%</td>
      <td>10727</td>
      <td>18096</td>
      <td>57</td>
      <td>0.53%</td>
    </tr>
    <tr>
      <th>2021-08-22</th>
      <th>ES</th>
      <td>10988</td>
      <td>38</td>
      <td>77</td>
      <td>35</td>
      <td>35</td>
      <td>2.20</td>
      <td>0.32%</td>
      <td>10988</td>
      <td>2436</td>
      <td>66</td>
      <td>0.60%</td>
    </tr>
    <tr>
      <th>2021-08-21</th>
      <th>ES</th>
      <td>10988</td>
      <td>47</td>
      <td>144</td>
      <td>47</td>
      <td>47</td>
      <td>3.06</td>
      <td>0.43%</td>
      <td>10988</td>
      <td>2436</td>
      <td>66</td>
      <td>0.60%</td>
    </tr>
    <tr>
      <th>2021-08-20</th>
      <th>ES</th>
      <td>10988</td>
      <td>48</td>
      <td>194</td>
      <td>64</td>
      <td>64</td>
      <td>3.03</td>
      <td>0.58%</td>
      <td>10988</td>
      <td>2436</td>
      <td>66</td>
      <td>0.60%</td>
    </tr>
    <tr>
      <th>2021-08-19</th>
      <th>ES</th>
      <td>11446</td>
      <td>49</td>
      <td>199</td>
      <td>76</td>
      <td>76</td>
      <td>2.62</td>
      <td>0.66%</td>
      <td>11446</td>
      <td>2436</td>
      <td>66</td>
      <td>0.58%</td>
    </tr>
    <tr>
      <th>2021-08-18</th>
      <th>ES</th>
      <td>12155</td>
      <td>35</td>
      <td>215</td>
      <td>76</td>
      <td>76</td>
      <td>2.83</td>
      <td>0.63%</td>
      <td>12155</td>
      <td>2436</td>
      <td>66</td>
      <td>0.54%</td>
    </tr>
    <tr>
      <th>2021-08-17</th>
      <th>ES</th>
      <td>12879</td>
      <td>40</td>
      <td>135</td>
      <td>63</td>
      <td>63</td>
      <td>2.14</td>
      <td>0.49%</td>
      <td>12879</td>
      <td>2436</td>
      <td>66</td>
      <td>0.51%</td>
    </tr>
    <tr>
      <th>2021-08-16</th>
      <th>ES</th>
      <td>13071</td>
      <td>43</td>
      <td>181</td>
      <td>60</td>
      <td>60</td>
      <td>3.02</td>
      <td>0.46%</td>
      <td>13071</td>
      <td>2436</td>
      <td>66</td>
      <td>0.50%</td>
    </tr>
    <tr>
      <th>2021-08-15</th>
      <th>ES</th>
      <td>15058</td>
      <td>41</td>
      <td>134</td>
      <td>49</td>
      <td>49</td>
      <td>2.73</td>
      <td>0.33%</td>
      <td>15058</td>
      <td>2944</td>
      <td>94</td>
      <td>0.62%</td>
    </tr>
    <tr>
      <th>2021-08-14</th>
      <th>ES</th>
      <td>15058</td>
      <td>43</td>
      <td>132</td>
      <td>49</td>
      <td>49</td>
      <td>2.69</td>
      <td>0.33%</td>
      <td>15058</td>
      <td>2944</td>
      <td>94</td>
      <td>0.62%</td>
    </tr>
    <tr>
      <th>2021-08-13</th>
      <th>ES</th>
      <td>15058</td>
      <td>34</td>
      <td>240</td>
      <td>93</td>
      <td>93</td>
      <td>2.58</td>
      <td>0.62%</td>
      <td>15058</td>
      <td>2944</td>
      <td>94</td>
      <td>0.62%</td>
    </tr>
    <tr>
      <th>2021-08-12</th>
      <th>ES</th>
      <td>15902</td>
      <td>46</td>
      <td>328</td>
      <td>108</td>
      <td>108</td>
      <td>3.04</td>
      <td>0.68%</td>
      <td>15902</td>
      <td>2944</td>
      <td>94</td>
      <td>0.59%</td>
    </tr>
    <tr>
      <th>2021-08-11</th>
      <th>ES</th>
      <td>16470</td>
      <td>44</td>
      <td>279</td>
      <td>94</td>
      <td>94</td>
      <td>2.97</td>
      <td>0.57%</td>
      <td>16470</td>
      <td>2944</td>
      <td>94</td>
      <td>0.57%</td>
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
      <th>2021-09-07</th>
      <td>41</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>14</td>
      <td>16</td>
      <td>0</td>
      <td>461</td>
    </tr>
    <tr>
      <th>2021-09-06</th>
      <td>124</td>
      <td>692</td>
      <td>619</td>
      <td>6</td>
      <td>26</td>
      <td>852</td>
      <td>0</td>
      <td>1790</td>
    </tr>
    <tr>
      <th>2021-09-05</th>
      <td>173</td>
      <td>1297</td>
      <td>868</td>
      <td>5</td>
      <td>30</td>
      <td>1457</td>
      <td>16</td>
      <td>2110</td>
    </tr>
    <tr>
      <th>2021-09-04</th>
      <td>249</td>
      <td>2519</td>
      <td>1782</td>
      <td>9</td>
      <td>53</td>
      <td>2711</td>
      <td>41</td>
      <td>3344</td>
    </tr>
    <tr>
      <th>2021-09-03</th>
      <td>328</td>
      <td>3985</td>
      <td>2956</td>
      <td>11</td>
      <td>57</td>
      <td>4215</td>
      <td>70</td>
      <td>4813</td>
    </tr>
    <tr>
      <th>2021-09-02</th>
      <td>381</td>
      <td>4657</td>
      <td>3372</td>
      <td>16</td>
      <td>72</td>
      <td>5045</td>
      <td>119</td>
      <td>5589</td>
    </tr>
    <tr>
      <th>2021-09-01</th>
      <td>392</td>
      <td>5508</td>
      <td>4101</td>
      <td>25</td>
      <td>76</td>
      <td>6022</td>
      <td>139</td>
      <td>5754</td>
    </tr>
    <tr>
      <th>2021-08-31</th>
      <td>401</td>
      <td>6328</td>
      <td>4789</td>
      <td>28</td>
      <td>94</td>
      <td>6984</td>
      <td>159</td>
      <td>5861</td>
    </tr>
    <tr>
      <th>2021-08-30</th>
      <td>372</td>
      <td>6278</td>
      <td>4660</td>
      <td>29</td>
      <td>97</td>
      <td>7148</td>
      <td>201</td>
      <td>5963</td>
    </tr>
    <tr>
      <th>2021-08-29</th>
      <td>325</td>
      <td>5692</td>
      <td>4144</td>
      <td>28</td>
      <td>87</td>
      <td>6717</td>
      <td>212</td>
      <td>6096</td>
    </tr>
    <tr>
      <th>2021-08-28</th>
      <td>280</td>
      <td>6454</td>
      <td>4878</td>
      <td>23</td>
      <td>82</td>
      <td>7587</td>
      <td>215</td>
      <td>6163</td>
    </tr>
    <tr>
      <th>2021-08-27</th>
      <td>223</td>
      <td>7178</td>
      <td>4441</td>
      <td>19</td>
      <td>58</td>
      <td>7058</td>
      <td>231</td>
      <td>6334</td>
    </tr>
    <tr>
      <th>2021-08-26</th>
      <td>173</td>
      <td>7559</td>
      <td>4062</td>
      <td>23</td>
      <td>47</td>
      <td>6467</td>
      <td>205</td>
      <td>6423</td>
    </tr>
    <tr>
      <th>2021-08-25</th>
      <td>112</td>
      <td>8100</td>
      <td>3884</td>
      <td>23</td>
      <td>40</td>
      <td>6116</td>
      <td>174</td>
      <td>6518</td>
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
      <td>4.8%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>88.7%</td>
      <td>-</td>
      <td>99.9%</td>
      <td></td>
      <td>81.4%</td>
      <td>79.4%</td>
      <td>0.8%</td>
      <td>70.0%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>67.2%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>65.1%</td>
      <td></td>
      <td>57.8%</td>
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
      <td>1.0%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>1.2%</td>
      <td></td>
      <td>0.9%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>82.0%</td>
      <td>100.0%</td>
      <td>53.6%</td>
      <td>100.0%</td>
      <td>-</td>
      <td>100.0%</td>
      <td>88.1%</td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>2.6%</td>
      <td>-</td>
      <td>2.4%</td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>71.0%</td>
      <td>87.2%</td>
      <td></td>
      <td>71.8%</td>
      <td>86.6%</td>
      <td>92.4%</td>
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
