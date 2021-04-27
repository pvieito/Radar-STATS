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

- [Report 2021-04-27@23](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-04-27</th>
      <th>ES</th>
      <td>19852</td>
      <td>172</td>
      <td>605</td>
      <td>172</td>
      <td>172</td>
      <td>3.52</td>
      <td>0.87%</td>
      <td>19852</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-26</th>
      <th>ES</th>
      <td>8588</td>
      <td>230</td>
      <td>456</td>
      <td>130</td>
      <td>130</td>
      <td>3.51</td>
      <td>1.51%</td>
      <td>8588</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-25</th>
      <th>ES</th>
      <td>8762</td>
      <td>281</td>
      <td>450</td>
      <td>115</td>
      <td>115</td>
      <td>3.91</td>
      <td>1.31%</td>
      <td>8762</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-24</th>
      <th>ES</th>
      <td>8762</td>
      <td>372</td>
      <td>550</td>
      <td>148</td>
      <td>148</td>
      <td>3.72</td>
      <td>1.69%</td>
      <td>8762</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-23</th>
      <th>ES</th>
      <td>8762</td>
      <td>468</td>
      <td>637</td>
      <td>190</td>
      <td>190</td>
      <td>3.35</td>
      <td>2.17%</td>
      <td>8762</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-22</th>
      <th>ES</th>
      <td>8600</td>
      <td>537</td>
      <td>669</td>
      <td>190</td>
      <td>190</td>
      <td>3.52</td>
      <td>2.21%</td>
      <td>8600</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-21</th>
      <th>ES</th>
      <td>8436</td>
      <td>601</td>
      <td>739</td>
      <td>206</td>
      <td>206</td>
      <td>3.59</td>
      <td>2.44%</td>
      <td>8436</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-20</th>
      <th>ES</th>
      <td>7401</td>
      <td>626</td>
      <td>578</td>
      <td>195</td>
      <td>195</td>
      <td>2.96</td>
      <td>2.63%</td>
      <td>7401</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-19</th>
      <th>ES</th>
      <td>8300</td>
      <td>544</td>
      <td>410</td>
      <td>122</td>
      <td>122</td>
      <td>3.36</td>
      <td>1.47%</td>
      <td>8300</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-04-18</th>
      <th>ES</th>
      <td>8539</td>
      <td>484</td>
      <td>287</td>
      <td>79</td>
      <td>79</td>
      <td>3.63</td>
      <td>0.93%</td>
      <td>8539</td>
      <td>3544</td>
      <td>168</td>
      <td>1.97%</td>
    </tr>
    <tr>
      <th>2021-04-17</th>
      <th>ES</th>
      <td>8539</td>
      <td>352</td>
      <td>583</td>
      <td>152</td>
      <td>152</td>
      <td>3.84</td>
      <td>1.78%</td>
      <td>8539</td>
      <td>3544</td>
      <td>168</td>
      <td>1.97%</td>
    </tr>
    <tr>
      <th>2021-04-16</th>
      <th>ES</th>
      <td>8539</td>
      <td>245</td>
      <td>810</td>
      <td>208</td>
      <td>208</td>
      <td>3.89</td>
      <td>2.44%</td>
      <td>8539</td>
      <td>3544</td>
      <td>168</td>
      <td>1.97%</td>
    </tr>
    <tr>
      <th>2021-04-15</th>
      <th>ES</th>
      <td>8578</td>
      <td>169</td>
      <td>705</td>
      <td>189</td>
      <td>189</td>
      <td>3.73</td>
      <td>2.20%</td>
      <td>8578</td>
      <td>3544</td>
      <td>168</td>
      <td>1.96%</td>
    </tr>
    <tr>
      <th>2021-04-14</th>
      <th>ES</th>
      <td>8612</td>
      <td>115</td>
      <td>596</td>
      <td>183</td>
      <td>183</td>
      <td>3.26</td>
      <td>2.12%</td>
      <td>8612</td>
      <td>3544</td>
      <td>168</td>
      <td>1.95%</td>
    </tr>
    <tr>
      <th>2021-04-13</th>
      <th>ES</th>
      <td>8371</td>
      <td>136</td>
      <td>556</td>
      <td>170</td>
      <td>170</td>
      <td>3.27</td>
      <td>2.03%</td>
      <td>8371</td>
      <td>3544</td>
      <td>168</td>
      <td>2.01%</td>
    </tr>
    <tr>
      <th>2021-04-12</th>
      <th>ES</th>
      <td>8419</td>
      <td>167</td>
      <td>427</td>
      <td>133</td>
      <td>133</td>
      <td>3.21</td>
      <td>1.58%</td>
      <td>8419</td>
      <td>3544</td>
      <td>168</td>
      <td>2.00%</td>
    </tr>
    <tr>
      <th>2021-04-11</th>
      <th>ES</th>
      <td>6650</td>
      <td>178</td>
      <td>395</td>
      <td>100</td>
      <td>100</td>
      <td>3.95</td>
      <td>1.50%</td>
      <td>6650</td>
      <td>3659</td>
      <td>182</td>
      <td>2.74%</td>
    </tr>
    <tr>
      <th>2021-04-10</th>
      <th>ES</th>
      <td>6650</td>
      <td>162</td>
      <td>595</td>
      <td>159</td>
      <td>159</td>
      <td>3.74</td>
      <td>2.39%</td>
      <td>6650</td>
      <td>3659</td>
      <td>182</td>
      <td>2.74%</td>
    </tr>
    <tr>
      <th>2021-04-09</th>
      <th>ES</th>
      <td>8017</td>
      <td>159</td>
      <td>723</td>
      <td>197</td>
      <td>197</td>
      <td>3.67</td>
      <td>2.46%</td>
      <td>8017</td>
      <td>3659</td>
      <td>182</td>
      <td>2.27%</td>
    </tr>
    <tr>
      <th>2021-04-08</th>
      <th>ES</th>
      <td>6463</td>
      <td>151</td>
      <td>706</td>
      <td>199</td>
      <td>199</td>
      <td>3.55</td>
      <td>3.08%</td>
      <td>6463</td>
      <td>3659</td>
      <td>182</td>
      <td>2.82%</td>
    </tr>
    <tr>
      <th>2021-04-07</th>
      <th>ES</th>
      <td>6055</td>
      <td>143</td>
      <td>765</td>
      <td>197</td>
      <td>197</td>
      <td>3.88</td>
      <td>3.25%</td>
      <td>6055</td>
      <td>3659</td>
      <td>182</td>
      <td>3.01%</td>
    </tr>
    <tr>
      <th>2021-04-06</th>
      <th>ES</th>
      <td>6018</td>
      <td>138</td>
      <td>624</td>
      <td>180</td>
      <td>180</td>
      <td>3.47</td>
      <td>2.99%</td>
      <td>6018</td>
      <td>3659</td>
      <td>182</td>
      <td>3.02%</td>
    </tr>
    <tr>
      <th>2021-04-05</th>
      <th>ES</th>
      <td>5786</td>
      <td>164</td>
      <td>563</td>
      <td>157</td>
      <td>157</td>
      <td>3.59</td>
      <td>2.71%</td>
      <td>5786</td>
      <td>3659</td>
      <td>182</td>
      <td>3.15%</td>
    </tr>
    <tr>
      <th>2021-04-04</th>
      <th>ES</th>
      <td>6520</td>
      <td>174</td>
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
      <td>195</td>
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
      <td>186</td>
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
      <td>188</td>
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
      <td>163</td>
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
      <th>2021-04-27</th>
      <td>170</td>
      <td>0</td>
      <td>2225</td>
      <td>0</td>
      <td>172</td>
      <td>2425</td>
      <td>148</td>
      <td>0</td>
      <td>3665</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2021-04-26</th>
      <td>303</td>
      <td>1905</td>
      <td>3996</td>
      <td>9</td>
      <td>230</td>
      <td>5596</td>
      <td>570</td>
      <td>35</td>
      <td>5378</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-25</th>
      <td>387</td>
      <td>3885</td>
      <td>4020</td>
      <td>19</td>
      <td>281</td>
      <td>6654</td>
      <td>1065</td>
      <td>91</td>
      <td>5234</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-24</th>
      <td>555</td>
      <td>7559</td>
      <td>6522</td>
      <td>25</td>
      <td>372</td>
      <td>10272</td>
      <td>1535</td>
      <td>147</td>
      <td>5207</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-23</th>
      <td>690</td>
      <td>12105</td>
      <td>9814</td>
      <td>31</td>
      <td>468</td>
      <td>14655</td>
      <td>2072</td>
      <td>205</td>
      <td>5293</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-22</th>
      <td>745</td>
      <td>15159</td>
      <td>11821</td>
      <td>38</td>
      <td>537</td>
      <td>17592</td>
      <td>2636</td>
      <td>279</td>
      <td>5407</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-21</th>
      <td>854</td>
      <td>19258</td>
      <td>15054</td>
      <td>44</td>
      <td>601</td>
      <td>21574</td>
      <td>3309</td>
      <td>301</td>
      <td>5474</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-20</th>
      <td>918</td>
      <td>22742</td>
      <td>17979</td>
      <td>53</td>
      <td>626</td>
      <td>25030</td>
      <td>3114</td>
      <td>332</td>
      <td>5791</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-19</th>
      <td>894</td>
      <td>22854</td>
      <td>17819</td>
      <td>52</td>
      <td>544</td>
      <td>25182</td>
      <td>3308</td>
      <td>337</td>
      <td>5911</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-18</th>
      <td>841</td>
      <td>21846</td>
      <td>16736</td>
      <td>52</td>
      <td>484</td>
      <td>24368</td>
      <td>3668</td>
      <td>365</td>
      <td>5990</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-17</th>
      <td>675</td>
      <td>24382</td>
      <td>17308</td>
      <td>57</td>
      <td>352</td>
      <td>24662</td>
      <td>4125</td>
      <td>366</td>
      <td>6132</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-16</th>
      <td>509</td>
      <td>27427</td>
      <td>16227</td>
      <td>62</td>
      <td>245</td>
      <td>22611</td>
      <td>4749</td>
      <td>326</td>
      <td>6171</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-15</th>
      <td>353</td>
      <td>29185</td>
      <td>15445</td>
      <td>57</td>
      <td>169</td>
      <td>20782</td>
      <td>5317</td>
      <td>295</td>
      <td>6231</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-04-14</th>
      <td>204</td>
      <td>31783</td>
      <td>14927</td>
      <td>51</td>
      <td>115</td>
      <td>19386</td>
      <td>5993</td>
      <td>254</td>
      <td>6258</td>
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
      <td>84.1%</td>
      <td>-</td>
      <td>87.5%</td>
      <td></td>
      <td>76.2%</td>
      <td>81.5%</td>
      <td></td>
      <td>0.7%</td>
      <td>43.8%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>61.9%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>70.6%</td>
      <td></td>
      <td></td>
      <td>61.5%</td>
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
      <td>1.6%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>2.2%</td>
      <td></td>
      <td></td>
      <td>1.3%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>81.8%</td>
      <td>100.0%</td>
      <td></td>
      <td>100.0%</td>
      <td>-</td>
      <td></td>
      <td>100.0%</td>
      <td>85.4%</td>
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
      <td>1.4%</td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>14.3%</td>
      <td>28.3%</td>
      <td></td>
      <td>19.6%</td>
      <td>27.7%</td>
      <td></td>
      <td>32.2%</td>
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
