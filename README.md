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

- [Report 2021-04-13@21](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-04-13</th>
      <th>ES</th>
      <td>22744</td>
      <td>144</td>
      <td>524</td>
      <td>144</td>
      <td>144</td>
      <td>3.64</td>
      <td>0.63%</td>
      <td>22744</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-12</th>
      <th>ES</th>
      <td>8419</td>
      <td>225</td>
      <td>427</td>
      <td>133</td>
      <td>133</td>
      <td>3.21</td>
      <td>1.58%</td>
      <td>8419</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-11</th>
      <th>ES</th>
      <td>6650</td>
      <td>258</td>
      <td>395</td>
      <td>100</td>
      <td>100</td>
      <td>3.95</td>
      <td>1.50%</td>
      <td>6650</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-10</th>
      <th>ES</th>
      <td>6650</td>
      <td>369</td>
      <td>595</td>
      <td>159</td>
      <td>159</td>
      <td>3.74</td>
      <td>2.39%</td>
      <td>6650</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-09</th>
      <th>ES</th>
      <td>8017</td>
      <td>452</td>
      <td>723</td>
      <td>197</td>
      <td>197</td>
      <td>3.67</td>
      <td>2.46%</td>
      <td>8017</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-08</th>
      <th>ES</th>
      <td>6463</td>
      <td>523</td>
      <td>706</td>
      <td>199</td>
      <td>199</td>
      <td>3.55</td>
      <td>3.08%</td>
      <td>6463</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-07</th>
      <th>ES</th>
      <td>6055</td>
      <td>586</td>
      <td>765</td>
      <td>197</td>
      <td>197</td>
      <td>3.88</td>
      <td>3.25%</td>
      <td>6055</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-06</th>
      <th>ES</th>
      <td>6018</td>
      <td>608</td>
      <td>624</td>
      <td>180</td>
      <td>180</td>
      <td>3.47</td>
      <td>2.99%</td>
      <td>6018</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-05</th>
      <th>ES</th>
      <td>5786</td>
      <td>608</td>
      <td>563</td>
      <td>157</td>
      <td>157</td>
      <td>3.59</td>
      <td>2.71%</td>
      <td>5786</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-04</th>
      <th>ES</th>
      <td>6520</td>
      <td>544</td>
      <td>325</td>
      <td>89</td>
      <td>89</td>
      <td>3.65</td>
      <td>1.37%</td>
      <td>6520</td>
      <td>3393</td>
      <td>126</td>
      <td>1.93%</td>
    </tr>
    <tr>
      <th>2021-04-03</th>
      <th>ES</th>
      <td>6520</td>
      <td>409</td>
      <td>298</td>
      <td>88</td>
      <td>88</td>
      <td>3.39</td>
      <td>1.35%</td>
      <td>6520</td>
      <td>3393</td>
      <td>126</td>
      <td>1.93%</td>
    </tr>
    <tr>
      <th>2021-04-02</th>
      <th>ES</th>
      <td>5153</td>
      <td>299</td>
      <td>299</td>
      <td>75</td>
      <td>75</td>
      <td>3.99</td>
      <td>1.46%</td>
      <td>5153</td>
      <td>3393</td>
      <td>126</td>
      <td>2.45%</td>
    </tr>
    <tr>
      <th>2021-04-01</th>
      <th>ES</th>
      <td>6237</td>
      <td>227</td>
      <td>567</td>
      <td>145</td>
      <td>145</td>
      <td>3.91</td>
      <td>2.32%</td>
      <td>6237</td>
      <td>3393</td>
      <td>126</td>
      <td>2.02%</td>
    </tr>
    <tr>
      <th>2021-03-31</th>
      <th>ES</th>
      <td>7148</td>
      <td>164</td>
      <td>715</td>
      <td>190</td>
      <td>190</td>
      <td>3.76</td>
      <td>2.66%</td>
      <td>7148</td>
      <td>3393</td>
      <td>126</td>
      <td>1.76%</td>
    </tr>
    <tr>
      <th>2021-03-30</th>
      <th>ES</th>
      <td>5929</td>
      <td>143</td>
      <td>537</td>
      <td>138</td>
      <td>138</td>
      <td>3.89</td>
      <td>2.33%</td>
      <td>5929</td>
      <td>3393</td>
      <td>126</td>
      <td>2.13%</td>
    </tr>
    <tr>
      <th>2021-03-29</th>
      <th>ES</th>
      <td>6003</td>
      <td>110</td>
      <td>447</td>
      <td>121</td>
      <td>121</td>
      <td>3.69</td>
      <td>2.02%</td>
      <td>6003</td>
      <td>3393</td>
      <td>126</td>
      <td>2.10%</td>
    </tr>
    <tr>
      <th>2021-03-28</th>
      <th>ES</th>
      <td>6142</td>
      <td>126</td>
      <td>323</td>
      <td>85</td>
      <td>85</td>
      <td>3.80</td>
      <td>1.38%</td>
      <td>6142</td>
      <td>3931</td>
      <td>144</td>
      <td>2.34%</td>
    </tr>
    <tr>
      <th>2021-03-27</th>
      <th>ES</th>
      <td>6142</td>
      <td>157</td>
      <td>411</td>
      <td>115</td>
      <td>115</td>
      <td>3.57</td>
      <td>1.87%</td>
      <td>6142</td>
      <td>3931</td>
      <td>144</td>
      <td>2.34%</td>
    </tr>
    <tr>
      <th>2021-03-26</th>
      <th>ES</th>
      <td>6142</td>
      <td>150</td>
      <td>643</td>
      <td>159</td>
      <td>159</td>
      <td>4.04</td>
      <td>2.59%</td>
      <td>6142</td>
      <td>3931</td>
      <td>144</td>
      <td>2.34%</td>
    </tr>
    <tr>
      <th>2021-03-25</th>
      <th>ES</th>
      <td>5058</td>
      <td>149</td>
      <td>570</td>
      <td>149</td>
      <td>149</td>
      <td>3.83</td>
      <td>2.95%</td>
      <td>5058</td>
      <td>3931</td>
      <td>144</td>
      <td>2.85%</td>
    </tr>
    <tr>
      <th>2021-03-24</th>
      <th>ES</th>
      <td>4029</td>
      <td>132</td>
      <td>588</td>
      <td>145</td>
      <td>145</td>
      <td>4.06</td>
      <td>3.60%</td>
      <td>4029</td>
      <td>3931</td>
      <td>144</td>
      <td>3.57%</td>
    </tr>
    <tr>
      <th>2021-03-23</th>
      <th>ES</th>
      <td>4899</td>
      <td>124</td>
      <td>630</td>
      <td>157</td>
      <td>157</td>
      <td>4.01</td>
      <td>3.20%</td>
      <td>4899</td>
      <td>3931</td>
      <td>144</td>
      <td>2.94%</td>
    </tr>
    <tr>
      <th>2021-03-22</th>
      <th>ES</th>
      <td>4820</td>
      <td>130</td>
      <td>351</td>
      <td>92</td>
      <td>92</td>
      <td>3.82</td>
      <td>1.91%</td>
      <td>4820</td>
      <td>3931</td>
      <td>144</td>
      <td>2.99%</td>
    </tr>
    <tr>
      <th>2021-03-21</th>
      <th>ES</th>
      <td>4090</td>
      <td>143</td>
      <td>249</td>
      <td>63</td>
      <td>63</td>
      <td>3.95</td>
      <td>1.54%</td>
      <td>4090</td>
      <td>3412</td>
      <td>99</td>
      <td>2.42%</td>
    </tr>
    <tr>
      <th>2021-03-20</th>
      <th>ES</th>
      <td>4090</td>
      <td>153</td>
      <td>365</td>
      <td>86</td>
      <td>86</td>
      <td>4.24</td>
      <td>2.10%</td>
      <td>4090</td>
      <td>3412</td>
      <td>99</td>
      <td>2.42%</td>
    </tr>
    <tr>
      <th>2021-03-19</th>
      <th>ES</th>
      <td>4090</td>
      <td>170</td>
      <td>441</td>
      <td>115</td>
      <td>115</td>
      <td>3.83</td>
      <td>2.81%</td>
      <td>4090</td>
      <td>3412</td>
      <td>99</td>
      <td>2.42%</td>
    </tr>
    <tr>
      <th>2021-03-18</th>
      <th>ES</th>
      <td>4854</td>
      <td>151</td>
      <td>475</td>
      <td>122</td>
      <td>122</td>
      <td>3.89</td>
      <td>2.51%</td>
      <td>4854</td>
      <td>3412</td>
      <td>99</td>
      <td>2.04%</td>
    </tr>
    <tr>
      <th>2021-03-17</th>
      <th>ES</th>
      <td>4859</td>
      <td>129</td>
      <td>347</td>
      <td>92</td>
      <td>92</td>
      <td>3.77</td>
      <td>1.89%</td>
      <td>4859</td>
      <td>3412</td>
      <td>99</td>
      <td>2.04%</td>
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
      <th>2021-04-13</th>
      <td>191</td>
      <td>0</td>
      <td>2571</td>
      <td>0</td>
      <td>144</td>
      <td>2766</td>
      <td>83</td>
      <td>0</td>
      <td>3747</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2021-04-12</th>
      <td>347</td>
      <td>2252</td>
      <td>4639</td>
      <td>17</td>
      <td>225</td>
      <td>6407</td>
      <td>2178</td>
      <td>49</td>
      <td>5509</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-11</th>
      <td>454</td>
      <td>4512</td>
      <td>4759</td>
      <td>27</td>
      <td>258</td>
      <td>7610</td>
      <td>1390</td>
      <td>105</td>
      <td>5477</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-10</th>
      <td>604</td>
      <td>8528</td>
      <td>7522</td>
      <td>42</td>
      <td>369</td>
      <td>11597</td>
      <td>1993</td>
      <td>176</td>
      <td>5389</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-09</th>
      <td>738</td>
      <td>13448</td>
      <td>11278</td>
      <td>53</td>
      <td>452</td>
      <td>16383</td>
      <td>2707</td>
      <td>250</td>
      <td>5420</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-08</th>
      <td>818</td>
      <td>16970</td>
      <td>13715</td>
      <td>76</td>
      <td>523</td>
      <td>19750</td>
      <td>3372</td>
      <td>322</td>
      <td>5587</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-07</th>
      <td>919</td>
      <td>20360</td>
      <td>16161</td>
      <td>85</td>
      <td>586</td>
      <td>23012</td>
      <td>4012</td>
      <td>351</td>
      <td>5758</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-06</th>
      <td>919</td>
      <td>21136</td>
      <td>16371</td>
      <td>100</td>
      <td>608</td>
      <td>23830</td>
      <td>4535</td>
      <td>362</td>
      <td>5887</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-05</th>
      <td>887</td>
      <td>20526</td>
      <td>15683</td>
      <td>101</td>
      <td>608</td>
      <td>23357</td>
      <td>5111</td>
      <td>352</td>
      <td>6094</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-04</th>
      <td>830</td>
      <td>21019</td>
      <td>16368</td>
      <td>100</td>
      <td>544</td>
      <td>23975</td>
      <td>5585</td>
      <td>335</td>
      <td>6231</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-03</th>
      <td>621</td>
      <td>22079</td>
      <td>16686</td>
      <td>97</td>
      <td>409</td>
      <td>23938</td>
      <td>6159</td>
      <td>330</td>
      <td>6324</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-02</th>
      <td>472</td>
      <td>24488</td>
      <td>15747</td>
      <td>96</td>
      <td>299</td>
      <td>22179</td>
      <td>6680</td>
      <td>302</td>
      <td>6353</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-01</th>
      <td>333</td>
      <td>27700</td>
      <td>15337</td>
      <td>98</td>
      <td>227</td>
      <td>20858</td>
      <td>7066</td>
      <td>272</td>
      <td>6407</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-31</th>
      <td>223</td>
      <td>30432</td>
      <td>14736</td>
      <td>112</td>
      <td>164</td>
      <td>19433</td>
      <td>7731</td>
      <td>223</td>
      <td>6433</td>
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
      <td>2.9%</td>
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
      <td>81.5%</td>
      <td>-</td>
      <td>85.5%</td>
      <td></td>
      <td>79.6%</td>
      <td>79.6%</td>
      <td></td>
      <td>0.3%</td>
      <td>40.9%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>62.8%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>70.0%</td>
      <td></td>
      <td></td>
      <td>63.1%</td>
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
      <td>1.8%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>2.2%</td>
      <td></td>
      <td></td>
      <td>1.1%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>83.6%</td>
      <td>100.0%</td>
      <td></td>
      <td>100.0%</td>
      <td>-</td>
      <td></td>
      <td>100.0%</td>
      <td>86.6%</td>
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
      <td>1.4%</td>
      <td></td>
      <td>-</td>
      <td>1.5%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>14.1%</td>
      <td>29.7%</td>
      <td></td>
      <td>16.5%</td>
      <td>28.5%</td>
      <td></td>
      <td>35.9%</td>
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
