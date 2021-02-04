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

- [Report 2021-02-04@23](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-02-04</th>
      <th>ES,AT,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>69063</td>
      <td>1134</td>
      <td>24588</td>
      <td>1134</td>
      <td>3026</td>
      <td>8.13</td>
      <td>4.38%</td>
      <td>30480</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-02-03</th>
      <th>ES,AT,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>69063</td>
      <td>4220</td>
      <td>22807</td>
      <td>1194</td>
      <td>3095</td>
      <td>7.37</td>
      <td>4.48%</td>
      <td>30480</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-02-02</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>69875</td>
      <td>6752</td>
      <td>20350</td>
      <td>1163</td>
      <td>2642</td>
      <td>7.70</td>
      <td>3.78%</td>
      <td>31722</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-02-01</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>71430</td>
      <td>7896</td>
      <td>13680</td>
      <td>577</td>
      <td>1749</td>
      <td>7.82</td>
      <td>2.45%</td>
      <td>32775</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-01-31</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>73744</td>
      <td>8622</td>
      <td>13100</td>
      <td>521</td>
      <td>1966</td>
      <td>6.66</td>
      <td>2.67%</td>
      <td>34794</td>
      <td>15753</td>
      <td>606</td>
      <td>1.74%</td>
    </tr>
    <tr>
      <th>2021-01-30</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>75266</td>
      <td>10589</td>
      <td>24205</td>
      <td>1272</td>
      <td>3229</td>
      <td>7.50</td>
      <td>4.29%</td>
      <td>34794</td>
      <td>15753</td>
      <td>606</td>
      <td>1.74%</td>
    </tr>
    <tr>
      <th>2021-01-29</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>75018</td>
      <td>12720</td>
      <td>25008</td>
      <td>1323</td>
      <td>3210</td>
      <td>7.79</td>
      <td>4.28%</td>
      <td>34794</td>
      <td>15753</td>
      <td>606</td>
      <td>1.74%</td>
    </tr>
    <tr>
      <th>2021-01-28</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>76804</td>
      <td>14448</td>
      <td>26004</td>
      <td>1370</td>
      <td>3344</td>
      <td>7.78</td>
      <td>4.35%</td>
      <td>35475</td>
      <td>15753</td>
      <td>606</td>
      <td>1.71%</td>
    </tr>
    <tr>
      <th>2021-01-27</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>77319</td>
      <td>16263</td>
      <td>27750</td>
      <td>1435</td>
      <td>3533</td>
      <td>7.85</td>
      <td>4.57%</td>
      <td>36826</td>
      <td>15753</td>
      <td>606</td>
      <td>1.65%</td>
    </tr>
    <tr>
      <th>2021-01-26</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>79518</td>
      <td>18329</td>
      <td>26988</td>
      <td>1532</td>
      <td>3241</td>
      <td>8.33</td>
      <td>4.08%</td>
      <td>37011</td>
      <td>15753</td>
      <td>606</td>
      <td>1.64%</td>
    </tr>
    <tr>
      <th>2021-01-25</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>79831</td>
      <td>18021</td>
      <td>14799</td>
      <td>824</td>
      <td>2017</td>
      <td>7.34</td>
      <td>2.53%</td>
      <td>36704</td>
      <td>15753</td>
      <td>606</td>
      <td>1.65%</td>
    </tr>
    <tr>
      <th>2021-01-24</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>79147</td>
      <td>16485</td>
      <td>16650</td>
      <td>717</td>
      <td>2427</td>
      <td>6.86</td>
      <td>3.07%</td>
      <td>35342</td>
      <td>14654</td>
      <td>731</td>
      <td>2.07%</td>
    </tr>
    <tr>
      <th>2021-01-23</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>80008</td>
      <td>15134</td>
      <td>25192</td>
      <td>1502</td>
      <td>3521</td>
      <td>7.15</td>
      <td>4.40%</td>
      <td>35342</td>
      <td>14654</td>
      <td>731</td>
      <td>2.07%</td>
    </tr>
    <tr>
      <th>2021-01-22</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>81009</td>
      <td>14238</td>
      <td>29420</td>
      <td>1622</td>
      <td>3887</td>
      <td>7.57</td>
      <td>4.80%</td>
      <td>35342</td>
      <td>14654</td>
      <td>731</td>
      <td>2.07%</td>
    </tr>
    <tr>
      <th>2021-01-21</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>80456</td>
      <td>13562</td>
      <td>29346</td>
      <td>1595</td>
      <td>4027</td>
      <td>7.29</td>
      <td>5.01%</td>
      <td>34958</td>
      <td>14654</td>
      <td>731</td>
      <td>2.09%</td>
    </tr>
    <tr>
      <th>2021-01-20</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>82125</td>
      <td>13021</td>
      <td>32857</td>
      <td>1753</td>
      <td>4339</td>
      <td>7.57</td>
      <td>5.28%</td>
      <td>33747</td>
      <td>14654</td>
      <td>731</td>
      <td>2.17%</td>
    </tr>
    <tr>
      <th>2021-01-19</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>82207</td>
      <td>13308</td>
      <td>29236</td>
      <td>1796</td>
      <td>3620</td>
      <td>8.08</td>
      <td>4.40%</td>
      <td>33360</td>
      <td>14654</td>
      <td>731</td>
      <td>2.19%</td>
    </tr>
    <tr>
      <th>2021-01-18</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>84112</td>
      <td>14258</td>
      <td>16986</td>
      <td>881</td>
      <td>2070</td>
      <td>8.21</td>
      <td>2.46%</td>
      <td>32096</td>
      <td>14654</td>
      <td>731</td>
      <td>2.28%</td>
    </tr>
    <tr>
      <th>2021-01-17</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>82532</td>
      <td>15392</td>
      <td>16559</td>
      <td>701</td>
      <td>2569</td>
      <td>6.45</td>
      <td>3.11%</td>
      <td>28829</td>
      <td>19146</td>
      <td>679</td>
      <td>2.36%</td>
    </tr>
    <tr>
      <th>2021-01-16</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>83137</td>
      <td>15911</td>
      <td>28691</td>
      <td>1449</td>
      <td>3952</td>
      <td>7.26</td>
      <td>4.75%</td>
      <td>28829</td>
      <td>19146</td>
      <td>679</td>
      <td>2.36%</td>
    </tr>
    <tr>
      <th>2021-01-15</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>86057</td>
      <td>16100</td>
      <td>31917</td>
      <td>1695</td>
      <td>4220</td>
      <td>7.56</td>
      <td>4.90%</td>
      <td>28829</td>
      <td>19146</td>
      <td>679</td>
      <td>2.36%</td>
    </tr>
    <tr>
      <th>2021-01-14</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>86729</td>
      <td>15523</td>
      <td>32816</td>
      <td>1728</td>
      <td>4408</td>
      <td>7.44</td>
      <td>5.08%</td>
      <td>26723</td>
      <td>19146</td>
      <td>679</td>
      <td>2.54%</td>
    </tr>
    <tr>
      <th>2021-01-13</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>92754</td>
      <td>14518</td>
      <td>36514</td>
      <td>1900</td>
      <td>4873</td>
      <td>7.49</td>
      <td>5.25%</td>
      <td>27649</td>
      <td>19146</td>
      <td>679</td>
      <td>2.46%</td>
    </tr>
    <tr>
      <th>2021-01-12</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>89737</td>
      <td>14531</td>
      <td>31624</td>
      <td>1727</td>
      <td>3909</td>
      <td>8.09</td>
      <td>4.36%</td>
      <td>22097</td>
      <td>19146</td>
      <td>679</td>
      <td>3.07%</td>
    </tr>
    <tr>
      <th>2021-01-11</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>89386</td>
      <td>15602</td>
      <td>19085</td>
      <td>890</td>
      <td>2407</td>
      <td>7.93</td>
      <td>2.69%</td>
      <td>21848</td>
      <td>19146</td>
      <td>679</td>
      <td>3.11%</td>
    </tr>
    <tr>
      <th>2021-01-10</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>85245</td>
      <td>16687</td>
      <td>21062</td>
      <td>596</td>
      <td>3146</td>
      <td>6.69</td>
      <td>3.69%</td>
      <td>17442</td>
      <td>22487</td>
      <td>452</td>
      <td>2.59%</td>
    </tr>
    <tr>
      <th>2021-01-09</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>85206</td>
      <td>17696</td>
      <td>37590</td>
      <td>1666</td>
      <td>5036</td>
      <td>7.46</td>
      <td>5.91%</td>
      <td>17442</td>
      <td>22487</td>
      <td>452</td>
      <td>2.59%</td>
    </tr>
    <tr>
      <th>2021-01-08</th>
      <th>ES,BE,DE,DK,FI,HR,IE,IT,LV,NL,PL</th>
      <td>81295</td>
      <td>17905</td>
      <td>43317</td>
      <td>2105</td>
      <td>5566</td>
      <td>7.78</td>
      <td>6.85%</td>
      <td>17442</td>
      <td>22487</td>
      <td>452</td>
      <td>2.59%</td>
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
      <th>EE</th>
      <th>ES</th>
      <th>ES@PRE</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-02-04</th>
      <td>145</td>
      <td>0</td>
      <td>0</td>
      <td>1134</td>
      <td>26</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2021-02-03</th>
      <td>323</td>
      <td>1764</td>
      <td>52</td>
      <td>4220</td>
      <td>659</td>
      <td>102</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2021-02-02</th>
      <td>464</td>
      <td>4366</td>
      <td>77</td>
      <td>6752</td>
      <td>1402</td>
      <td>102</td>
      <td>29</td>
    </tr>
    <tr>
      <th>2021-02-01</th>
      <td>587</td>
      <td>5276</td>
      <td>99</td>
      <td>7896</td>
      <td>2065</td>
      <td>103</td>
      <td>36</td>
    </tr>
    <tr>
      <th>2021-01-31</th>
      <td>635</td>
      <td>5711</td>
      <td>108</td>
      <td>8622</td>
      <td>2713</td>
      <td>104</td>
      <td>38</td>
    </tr>
    <tr>
      <th>2021-01-30</th>
      <td>711</td>
      <td>7583</td>
      <td>101</td>
      <td>10589</td>
      <td>3180</td>
      <td>104</td>
      <td>42</td>
    </tr>
    <tr>
      <th>2021-01-29</th>
      <td>770</td>
      <td>9492</td>
      <td>96</td>
      <td>12720</td>
      <td>3781</td>
      <td>102</td>
      <td>54</td>
    </tr>
    <tr>
      <th>2021-01-28</th>
      <td>847</td>
      <td>10918</td>
      <td>92</td>
      <td>14448</td>
      <td>4459</td>
      <td>106</td>
      <td>59</td>
    </tr>
    <tr>
      <th>2021-01-27</th>
      <td>924</td>
      <td>12415</td>
      <td>109</td>
      <td>16263</td>
      <td>5132</td>
      <td>106</td>
      <td>68</td>
    </tr>
    <tr>
      <th>2021-01-26</th>
      <td>961</td>
      <td>14065</td>
      <td>119</td>
      <td>18329</td>
      <td>5840</td>
      <td>109</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2021-01-25</th>
      <td>785</td>
      <td>14326</td>
      <td>113</td>
      <td>18021</td>
      <td>6119</td>
      <td>108</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2021-01-24</th>
      <td>601</td>
      <td>14111</td>
      <td>116</td>
      <td>16485</td>
      <td>6657</td>
      <td>109</td>
      <td>97</td>
    </tr>
    <tr>
      <th>2021-01-23</th>
      <td>426</td>
      <td>15659</td>
      <td>106</td>
      <td>15134</td>
      <td>7186</td>
      <td>108</td>
      <td>102</td>
    </tr>
    <tr>
      <th>2021-01-22</th>
      <td>284</td>
      <td>17510</td>
      <td>101</td>
      <td>14238</td>
      <td>7699</td>
      <td>109</td>
      <td>114</td>
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
      <th>EE</th>
      <th>ES</th>
      <th>ES@PRE</th>
      <th>MT</th>
      <th>PT</th>
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
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td></td>
      <td>-</td>
      <td></td>
      <td>70.9%</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>EE</th>
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
      <td>87.7%</td>
      <td></td>
      <td>-</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES@PRE</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>PT</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
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
- **Source Countries**: Countries with an Exposure Notification app that can share TEKs with the Radar COVID server directly or through the EFGS (see the notes below for more information). Currently the following countries are considered source countries: ES, AT, BE, DE, DK, FI, HR, IE, IT, LV, NL, PL.

### Metrics

- **COVID-19 Cases in Source Countries** (`covid_cases`): Confirmed new COVID-19 cases in applicable source countries estimated with a 7-day rolling average (see the notes below for more information).
- **Shared TEKs by Generation Date** (`shared_teks_by_generation_date`): TEKs published on the Radar COVID server by the date they were generated on-device.
- **Shared TEKs by Upload Date** (`shared_teks_by_upload_date`): TEKs published on the Radar COVID server by the date they were added to the server. Typically this is the date when the user shares the positive diagnosis using the app with the one-time code sent by the Health Authorities or when TEKs from other countries backends are loaded from the EFGS.
- **Shared TEKs Uploaded on Generation Date** (`shared_teks_uploaded_on_generation_date`): TEKs uploaded to the Radar COVID server on the same date they were generated on-device. This metric measures the number of diagnoses shared by devices which already support the new Exposure Notification API version with early TEK release (ie. the current date TEK is released along previous days TEKs), see the notes below for more information.
- **Shared Diagnoses** (`shared_diagnoses`): Estimation of the number of diagnoses shared via Exposure Notification apps published on the Radar COVID server. The estimation is inferred from the maximum number of TEKs uploaded each date that were generated on-device on a unique date, as each device can only upload 1 TEK per generation date.
- **TEKs Uploaded per Shared Diagnosis** (`teks_per_shared_diagnosis`): Estimation of the average number of TEKs uploaded with each shared diagnosis. This number should ideally be around 14 TEKs uploaded per shared diagnosis.
- **Usage Ratio** (`shared_diagnoses_per_covid_case`): Estimation of the fraction of COVID-19 cases in applicable source countries which shared their diagnosis via an Exposure Notification app (see the notes below for more information). Ideally it should be 100% (ie. all confirmed cases sharing their TEKs with an Exposure Notification app).

#### Important Notes

- As Radar COVID is [integrated](https://twitter.com/eu_commission/status/1318152800887558144?s=21) with the [EU Federation Gateway Service (EFGS)](https://github.com/eu-federation-gateway-service/efgs-federation-gateway) project, the server may publish TEKs from multiple source countries. Those EU-wide TEKs are published merged with TEKs shared directly from the Radar COVID app and they cannot be distinguished. To compute a valid usage ratio, we take in account COVID-19 cases from all applicable source countries [integrated with the EFGS](https://ec.europa.eu/info/live-work-travel-eu/health/coronavirus-response/travel-during-coronavirus-pandemic/mobile-contact-tracing-apps-eu-member-states_en), currently the following countries are considered source countries: ES, AT, BE, DE, DK, FI, HR, IE, IT, LV, NL, PL.
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
