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

- [Report 2021-05-17@20](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-05-17</th>
      <th>ES</th>
      <td>2116</td>
      <td>59</td>
      <td>183</td>
      <td>59</td>
      <td>59</td>
      <td>3.10</td>
      <td>2.79%</td>
      <td>2116</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-05-16</th>
      <th>ES</th>
      <td>5342</td>
      <td>77</td>
      <td>205</td>
      <td>45</td>
      <td>45</td>
      <td>4.56</td>
      <td>0.84%</td>
      <td>5342</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-05-15</th>
      <th>ES</th>
      <td>5342</td>
      <td>122</td>
      <td>232</td>
      <td>58</td>
      <td>58</td>
      <td>4.00</td>
      <td>1.09%</td>
      <td>5342</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-05-14</th>
      <th>ES</th>
      <td>5342</td>
      <td>185</td>
      <td>261</td>
      <td>88</td>
      <td>88</td>
      <td>2.97</td>
      <td>1.65%</td>
      <td>5342</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-05-13</th>
      <th>ES</th>
      <td>5604</td>
      <td>218</td>
      <td>313</td>
      <td>93</td>
      <td>93</td>
      <td>3.37</td>
      <td>1.66%</td>
      <td>5604</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-05-12</th>
      <th>ES</th>
      <td>5927</td>
      <td>239</td>
      <td>340</td>
      <td>90</td>
      <td>90</td>
      <td>3.78</td>
      <td>1.52%</td>
      <td>5927</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-05-11</th>
      <th>ES</th>
      <td>5913</td>
      <td>282</td>
      <td>394</td>
      <td>111</td>
      <td>111</td>
      <td>3.55</td>
      <td>1.88%</td>
      <td>5913</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-05-10</th>
      <th>ES</th>
      <td>5852</td>
      <td>274</td>
      <td>277</td>
      <td>79</td>
      <td>79</td>
      <td>3.51</td>
      <td>1.35%</td>
      <td>5852</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-05-09</th>
      <th>ES</th>
      <td>6190</td>
      <td>248</td>
      <td>126</td>
      <td>43</td>
      <td>43</td>
      <td>2.93</td>
      <td>0.69%</td>
      <td>6190</td>
      <td>3457</td>
      <td>96</td>
      <td>1.55%</td>
    </tr>
    <tr>
      <th>2021-05-08</th>
      <th>ES</th>
      <td>6190</td>
      <td>272</td>
      <td>249</td>
      <td>80</td>
      <td>80</td>
      <td>3.11</td>
      <td>1.29%</td>
      <td>6190</td>
      <td>3457</td>
      <td>96</td>
      <td>1.55%</td>
    </tr>
    <tr>
      <th>2021-05-07</th>
      <th>ES</th>
      <td>6190</td>
      <td>181</td>
      <td>486</td>
      <td>131</td>
      <td>131</td>
      <td>3.71</td>
      <td>2.12%</td>
      <td>6190</td>
      <td>3457</td>
      <td>96</td>
      <td>1.55%</td>
    </tr>
    <tr>
      <th>2021-05-06</th>
      <th>ES</th>
      <td>6326</td>
      <td>145</td>
      <td>422</td>
      <td>109</td>
      <td>109</td>
      <td>3.87</td>
      <td>1.72%</td>
      <td>6326</td>
      <td>3457</td>
      <td>96</td>
      <td>1.52%</td>
    </tr>
    <tr>
      <th>2021-05-05</th>
      <th>ES</th>
      <td>6638</td>
      <td>106</td>
      <td>406</td>
      <td>111</td>
      <td>111</td>
      <td>3.66</td>
      <td>1.67%</td>
      <td>6638</td>
      <td>3457</td>
      <td>96</td>
      <td>1.45%</td>
    </tr>
    <tr>
      <th>2021-05-04</th>
      <th>ES</th>
      <td>6973</td>
      <td>74</td>
      <td>414</td>
      <td>93</td>
      <td>93</td>
      <td>4.45</td>
      <td>1.33%</td>
      <td>6973</td>
      <td>3457</td>
      <td>96</td>
      <td>1.38%</td>
    </tr>
    <tr>
      <th>2021-05-03</th>
      <th>ES</th>
      <td>7423</td>
      <td>95</td>
      <td>288</td>
      <td>69</td>
      <td>69</td>
      <td>4.17</td>
      <td>0.93%</td>
      <td>7423</td>
      <td>3457</td>
      <td>96</td>
      <td>1.29%</td>
    </tr>
    <tr>
      <th>2021-05-02</th>
      <th>ES</th>
      <td>7923</td>
      <td>107</td>
      <td>260</td>
      <td>79</td>
      <td>79</td>
      <td>3.29</td>
      <td>1.00%</td>
      <td>7923</td>
      <td>3364</td>
      <td>143</td>
      <td>1.80%</td>
    </tr>
    <tr>
      <th>2021-05-01</th>
      <th>ES</th>
      <td>7923</td>
      <td>106</td>
      <td>405</td>
      <td>119</td>
      <td>119</td>
      <td>3.40</td>
      <td>1.50%</td>
      <td>7923</td>
      <td>3364</td>
      <td>143</td>
      <td>1.80%</td>
    </tr>
    <tr>
      <th>2021-04-30</th>
      <th>ES</th>
      <td>7923</td>
      <td>114</td>
      <td>534</td>
      <td>141</td>
      <td>141</td>
      <td>3.79</td>
      <td>1.78%</td>
      <td>7923</td>
      <td>3364</td>
      <td>143</td>
      <td>1.80%</td>
    </tr>
    <tr>
      <th>2021-04-29</th>
      <th>ES</th>
      <td>8294</td>
      <td>115</td>
      <td>649</td>
      <td>142</td>
      <td>142</td>
      <td>4.57</td>
      <td>1.71%</td>
      <td>8294</td>
      <td>3364</td>
      <td>143</td>
      <td>1.72%</td>
    </tr>
    <tr>
      <th>2021-04-28</th>
      <th>ES</th>
      <td>8390</td>
      <td>103</td>
      <td>530</td>
      <td>159</td>
      <td>159</td>
      <td>3.33</td>
      <td>1.90%</td>
      <td>8390</td>
      <td>3364</td>
      <td>143</td>
      <td>1.70%</td>
    </tr>
    <tr>
      <th>2021-04-27</th>
      <th>ES</th>
      <td>9683</td>
      <td>103</td>
      <td>605</td>
      <td>172</td>
      <td>172</td>
      <td>3.52</td>
      <td>1.78%</td>
      <td>9683</td>
      <td>3364</td>
      <td>143</td>
      <td>1.48%</td>
    </tr>
    <tr>
      <th>2021-04-26</th>
      <th>ES</th>
      <td>8588</td>
      <td>125</td>
      <td>456</td>
      <td>130</td>
      <td>130</td>
      <td>3.51</td>
      <td>1.51%</td>
      <td>8588</td>
      <td>3364</td>
      <td>143</td>
      <td>1.67%</td>
    </tr>
    <tr>
      <th>2021-04-25</th>
      <th>ES</th>
      <td>8762</td>
      <td>141</td>
      <td>450</td>
      <td>115</td>
      <td>115</td>
      <td>3.91</td>
      <td>1.31%</td>
      <td>8762</td>
      <td>3216</td>
      <td>176</td>
      <td>2.01%</td>
    </tr>
    <tr>
      <th>2021-04-24</th>
      <th>ES</th>
      <td>8762</td>
      <td>140</td>
      <td>550</td>
      <td>148</td>
      <td>148</td>
      <td>3.72</td>
      <td>1.69%</td>
      <td>8762</td>
      <td>3216</td>
      <td>176</td>
      <td>2.01%</td>
    </tr>
    <tr>
      <th>2021-04-23</th>
      <th>ES</th>
      <td>8762</td>
      <td>154</td>
      <td>637</td>
      <td>190</td>
      <td>190</td>
      <td>3.35</td>
      <td>2.17%</td>
      <td>8762</td>
      <td>3216</td>
      <td>176</td>
      <td>2.01%</td>
    </tr>
    <tr>
      <th>2021-04-22</th>
      <th>ES</th>
      <td>8600</td>
      <td>158</td>
      <td>669</td>
      <td>190</td>
      <td>190</td>
      <td>3.52</td>
      <td>2.21%</td>
      <td>8600</td>
      <td>3216</td>
      <td>176</td>
      <td>2.05%</td>
    </tr>
    <tr>
      <th>2021-04-21</th>
      <th>ES</th>
      <td>8436</td>
      <td>148</td>
      <td>739</td>
      <td>206</td>
      <td>206</td>
      <td>3.59</td>
      <td>2.44%</td>
      <td>8436</td>
      <td>3216</td>
      <td>176</td>
      <td>2.09%</td>
    </tr>
    <tr>
      <th>2021-04-20</th>
      <th>ES</th>
      <td>7401</td>
      <td>150</td>
      <td>578</td>
      <td>195</td>
      <td>195</td>
      <td>2.96</td>
      <td>2.63%</td>
      <td>7401</td>
      <td>3216</td>
      <td>176</td>
      <td>2.38%</td>
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
      <th colspan="10" halign="left">Shared TEKs by Generation Date (Source Countries)</th>
    </tr>
    <tr>
      <th>Backend</th>
      <th>CH</th>
      <th>DE</th>
      <th>DE@ES</th>
      <th>EE</th>
      <th>ES</th>
      <th>EU@ES</th>
      <th>EU@ES-PRE</th>
      <th>IT@ES</th>
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
      <th>2021-05-17</th>
      <td>40</td>
      <td>0</td>
      <td>337</td>
      <td>0</td>
      <td>59</td>
      <td>411</td>
      <td>1</td>
      <td>0</td>
      <td>622</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2021-05-16</th>
      <td>98</td>
      <td>639</td>
      <td>930</td>
      <td>3</td>
      <td>77</td>
      <td>1637</td>
      <td>1</td>
      <td>10</td>
      <td>2153</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-15</th>
      <td>169</td>
      <td>2377</td>
      <td>2002</td>
      <td>7</td>
      <td>122</td>
      <td>3414</td>
      <td>1</td>
      <td>28</td>
      <td>3895</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-14</th>
      <td>230</td>
      <td>4053</td>
      <td>3022</td>
      <td>13</td>
      <td>185</td>
      <td>5226</td>
      <td>0</td>
      <td>50</td>
      <td>5428</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-13</th>
      <td>308</td>
      <td>5495</td>
      <td>3736</td>
      <td>20</td>
      <td>218</td>
      <td>6719</td>
      <td>30</td>
      <td>67</td>
      <td>5541</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-12</th>
      <td>357</td>
      <td>7914</td>
      <td>5480</td>
      <td>26</td>
      <td>239</td>
      <td>9276</td>
      <td>199</td>
      <td>88</td>
      <td>5669</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-11</th>
      <td>423</td>
      <td>10340</td>
      <td>7288</td>
      <td>30</td>
      <td>282</td>
      <td>11926</td>
      <td>810</td>
      <td>129</td>
      <td>5715</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-10</th>
      <td>459</td>
      <td>10970</td>
      <td>7448</td>
      <td>27</td>
      <td>274</td>
      <td>12783</td>
      <td>1474</td>
      <td>154</td>
      <td>5814</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-09</th>
      <td>465</td>
      <td>10830</td>
      <td>7138</td>
      <td>27</td>
      <td>248</td>
      <td>12824</td>
      <td>1958</td>
      <td>161</td>
      <td>6096</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-08</th>
      <td>474</td>
      <td>12554</td>
      <td>8724</td>
      <td>27</td>
      <td>272</td>
      <td>14711</td>
      <td>2457</td>
      <td>168</td>
      <td>6291</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-07</th>
      <td>388</td>
      <td>14645</td>
      <td>9258</td>
      <td>30</td>
      <td>181</td>
      <td>15330</td>
      <td>2950</td>
      <td>177</td>
      <td>6561</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-06</th>
      <td>304</td>
      <td>16041</td>
      <td>8039</td>
      <td>32</td>
      <td>145</td>
      <td>13515</td>
      <td>7569</td>
      <td>177</td>
      <td>6744</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-05</th>
      <td>229</td>
      <td>17983</td>
      <td>7625</td>
      <td>32</td>
      <td>106</td>
      <td>12374</td>
      <td>8732</td>
      <td>148</td>
      <td>6880</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-05-04</th>
      <td>162</td>
      <td>20360</td>
      <td>7337</td>
      <td>33</td>
      <td>74</td>
      <td>11358</td>
      <td>9175</td>
      <td>126</td>
      <td>6986</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

- [Multi-Backend Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Multi-Backend-Summary-Table.csv)

#### Multi-Backend Cross-Sharing Summary Table

<table border="1" class="dataframe table-center">
  <thead>
    <tr style="text-align: center;">
      <th></th>
      <th colspan="10" halign="left">Fraction of TEKs in Backend (A) Available in Backend (B)</th>
    </tr>
    <tr style="text-align: center;">
      <th>Backend (A)</th>
      <th>CH</th>
      <th>DE</th>
      <th>DE@ES</th>
      <th>EE</th>
      <th>ES</th>
      <th>EU@ES</th>
      <th>EU@ES-PRE</th>
      <th>IT@ES</th>
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
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <th>CH</th>
      <td>-</td>
      <td>2.8%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE</th>
      <td>90.6%</td>
      <td>-</td>
      <td>95.2%</td>
      <td></td>
      <td>83.5%</td>
      <td>78.8%</td>
      <td></td>
      <td></td>
      <td>65.0%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>55.6%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>59.6%</td>
      <td></td>
      <td></td>
      <td>54.0%</td>
      <td></td>
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
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES</th>
      <td></td>
      <td>1.5%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>1.9%</td>
      <td></td>
      <td></td>
      <td>1.5%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>77.2%</td>
      <td>100.0%</td>
      <td></td>
      <td>100.0%</td>
      <td>-</td>
      <td></td>
      <td>100.0%</td>
      <td>91.9%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES-PRE</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>IT@ES</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.1%</td>
      <td></td>
      <td>-</td>
      <td>1.1%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>36.0%</td>
      <td>51.3%</td>
      <td></td>
      <td>46.0%</td>
      <td>52.0%</td>
      <td></td>
      <td>54.6%</td>
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
