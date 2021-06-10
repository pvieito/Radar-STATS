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

- [Report 2021-06-10@23](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-06-10</th>
      <th>ES</th>
      <td>4427</td>
      <td>83</td>
      <td>189</td>
      <td>83</td>
      <td>83</td>
      <td>2.28</td>
      <td>1.87%</td>
      <td>4427</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-06-09</th>
      <th>ES</th>
      <td>3956</td>
      <td>96</td>
      <td>223</td>
      <td>65</td>
      <td>65</td>
      <td>3.43</td>
      <td>1.64%</td>
      <td>3956</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-06-08</th>
      <th>ES</th>
      <td>4036</td>
      <td>91</td>
      <td>146</td>
      <td>40</td>
      <td>40</td>
      <td>3.65</td>
      <td>0.99%</td>
      <td>4036</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-06-07</th>
      <th>ES</th>
      <td>4162</td>
      <td>101</td>
      <td>102</td>
      <td>33</td>
      <td>33</td>
      <td>3.09</td>
      <td>0.79%</td>
      <td>4162</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-06-06</th>
      <th>ES</th>
      <td>4189</td>
      <td>103</td>
      <td>71</td>
      <td>25</td>
      <td>25</td>
      <td>2.84</td>
      <td>0.60%</td>
      <td>4189</td>
      <td>2880</td>
      <td>51</td>
      <td>1.22%</td>
    </tr>
    <tr>
      <th>2021-06-05</th>
      <th>ES</th>
      <td>4189</td>
      <td>111</td>
      <td>137</td>
      <td>36</td>
      <td>36</td>
      <td>3.81</td>
      <td>0.86%</td>
      <td>4189</td>
      <td>2880</td>
      <td>51</td>
      <td>1.22%</td>
    </tr>
    <tr>
      <th>2021-06-04</th>
      <th>ES</th>
      <td>4189</td>
      <td>139</td>
      <td>178</td>
      <td>58</td>
      <td>58</td>
      <td>3.07</td>
      <td>1.38%</td>
      <td>4189</td>
      <td>2880</td>
      <td>51</td>
      <td>1.22%</td>
    </tr>
    <tr>
      <th>2021-06-03</th>
      <th>ES</th>
      <td>4262</td>
      <td>144</td>
      <td>168</td>
      <td>50</td>
      <td>50</td>
      <td>3.36</td>
      <td>1.17%</td>
      <td>4262</td>
      <td>2880</td>
      <td>51</td>
      <td>1.20%</td>
    </tr>
    <tr>
      <th>2021-06-02</th>
      <th>ES</th>
      <td>4268</td>
      <td>168</td>
      <td>210</td>
      <td>60</td>
      <td>60</td>
      <td>3.50</td>
      <td>1.41%</td>
      <td>4268</td>
      <td>2880</td>
      <td>51</td>
      <td>1.19%</td>
    </tr>
    <tr>
      <th>2021-06-01</th>
      <th>ES</th>
      <td>4271</td>
      <td>171</td>
      <td>258</td>
      <td>60</td>
      <td>60</td>
      <td>4.30</td>
      <td>1.40%</td>
      <td>4271</td>
      <td>2880</td>
      <td>51</td>
      <td>1.19%</td>
    </tr>
    <tr>
      <th>2021-05-31</th>
      <th>ES</th>
      <td>4410</td>
      <td>131</td>
      <td>128</td>
      <td>48</td>
      <td>48</td>
      <td>2.67</td>
      <td>1.09%</td>
      <td>4410</td>
      <td>2880</td>
      <td>51</td>
      <td>1.16%</td>
    </tr>
    <tr>
      <th>2021-05-30</th>
      <th>ES</th>
      <td>4601</td>
      <td>106</td>
      <td>152</td>
      <td>30</td>
      <td>30</td>
      <td>5.07</td>
      <td>0.65%</td>
      <td>4601</td>
      <td>2588</td>
      <td>75</td>
      <td>1.63%</td>
    </tr>
    <tr>
      <th>2021-05-29</th>
      <th>ES</th>
      <td>4601</td>
      <td>76</td>
      <td>233</td>
      <td>63</td>
      <td>63</td>
      <td>3.70</td>
      <td>1.37%</td>
      <td>4601</td>
      <td>2588</td>
      <td>75</td>
      <td>1.63%</td>
    </tr>
    <tr>
      <th>2021-05-28</th>
      <th>ES</th>
      <td>4601</td>
      <td>53</td>
      <td>360</td>
      <td>97</td>
      <td>97</td>
      <td>3.71</td>
      <td>2.11%</td>
      <td>4601</td>
      <td>2588</td>
      <td>75</td>
      <td>1.63%</td>
    </tr>
    <tr>
      <th>2021-05-27</th>
      <th>ES</th>
      <td>4502</td>
      <td>53</td>
      <td>237</td>
      <td>76</td>
      <td>76</td>
      <td>3.12</td>
      <td>1.69%</td>
      <td>4502</td>
      <td>2588</td>
      <td>75</td>
      <td>1.67%</td>
    </tr>
    <tr>
      <th>2021-05-26</th>
      <th>ES</th>
      <td>4565</td>
      <td>56</td>
      <td>280</td>
      <td>74</td>
      <td>74</td>
      <td>3.78</td>
      <td>1.62%</td>
      <td>4565</td>
      <td>2588</td>
      <td>75</td>
      <td>1.64%</td>
    </tr>
    <tr>
      <th>2021-05-25</th>
      <th>ES</th>
      <td>4719</td>
      <td>54</td>
      <td>305</td>
      <td>91</td>
      <td>91</td>
      <td>3.35</td>
      <td>1.93%</td>
      <td>4719</td>
      <td>2588</td>
      <td>75</td>
      <td>1.59%</td>
    </tr>
    <tr>
      <th>2021-05-24</th>
      <th>ES</th>
      <td>4523</td>
      <td>74</td>
      <td>231</td>
      <td>65</td>
      <td>65</td>
      <td>3.55</td>
      <td>1.44%</td>
      <td>4523</td>
      <td>2588</td>
      <td>75</td>
      <td>1.66%</td>
    </tr>
    <tr>
      <th>2021-05-23</th>
      <th>ES</th>
      <td>4522</td>
      <td>71</td>
      <td>203</td>
      <td>47</td>
      <td>47</td>
      <td>4.32</td>
      <td>1.04%</td>
      <td>4522</td>
      <td>3196</td>
      <td>84</td>
      <td>1.86%</td>
    </tr>
    <tr>
      <th>2021-05-22</th>
      <th>ES</th>
      <td>4522</td>
      <td>62</td>
      <td>199</td>
      <td>51</td>
      <td>51</td>
      <td>3.90</td>
      <td>1.13%</td>
      <td>4522</td>
      <td>3196</td>
      <td>84</td>
      <td>1.86%</td>
    </tr>
    <tr>
      <th>2021-05-21</th>
      <th>ES</th>
      <td>4522</td>
      <td>69</td>
      <td>384</td>
      <td>98</td>
      <td>98</td>
      <td>3.92</td>
      <td>2.17%</td>
      <td>4522</td>
      <td>3196</td>
      <td>84</td>
      <td>1.86%</td>
    </tr>
    <tr>
      <th>2021-05-20</th>
      <th>ES</th>
      <td>4744</td>
      <td>75</td>
      <td>350</td>
      <td>100</td>
      <td>100</td>
      <td>3.50</td>
      <td>2.11%</td>
      <td>4744</td>
      <td>3196</td>
      <td>84</td>
      <td>1.77%</td>
    </tr>
    <tr>
      <th>2021-05-19</th>
      <th>ES</th>
      <td>4740</td>
      <td>77</td>
      <td>339</td>
      <td>100</td>
      <td>100</td>
      <td>3.39</td>
      <td>2.11%</td>
      <td>4740</td>
      <td>3196</td>
      <td>84</td>
      <td>1.77%</td>
    </tr>
    <tr>
      <th>2021-05-18</th>
      <th>ES</th>
      <td>4788</td>
      <td>70</td>
      <td>387</td>
      <td>103</td>
      <td>103</td>
      <td>3.76</td>
      <td>2.15%</td>
      <td>4788</td>
      <td>3196</td>
      <td>84</td>
      <td>1.75%</td>
    </tr>
    <tr>
      <th>2021-05-17</th>
      <th>ES</th>
      <td>4924</td>
      <td>88</td>
      <td>195</td>
      <td>65</td>
      <td>65</td>
      <td>3.00</td>
      <td>1.32%</td>
      <td>4924</td>
      <td>3196</td>
      <td>84</td>
      <td>1.71%</td>
    </tr>
    <tr>
      <th>2021-05-16</th>
      <th>ES</th>
      <td>5342</td>
      <td>95</td>
      <td>205</td>
      <td>45</td>
      <td>45</td>
      <td>4.56</td>
      <td>0.84%</td>
      <td>5342</td>
      <td>3513</td>
      <td>85</td>
      <td>1.59%</td>
    </tr>
    <tr>
      <th>2021-05-15</th>
      <th>ES</th>
      <td>5342</td>
      <td>85</td>
      <td>232</td>
      <td>58</td>
      <td>58</td>
      <td>4.00</td>
      <td>1.09%</td>
      <td>5342</td>
      <td>3513</td>
      <td>85</td>
      <td>1.59%</td>
    </tr>
    <tr>
      <th>2021-05-14</th>
      <th>ES</th>
      <td>5342</td>
      <td>90</td>
      <td>261</td>
      <td>88</td>
      <td>88</td>
      <td>2.97</td>
      <td>1.65%</td>
      <td>5342</td>
      <td>3513</td>
      <td>85</td>
      <td>1.59%</td>
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
      <th colspan="9" halign="left">Shared TEKs by Generation Date (Source Countries)</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-06-10</th>
      <td>10</td>
      <td>0</td>
      <td>147</td>
      <td>1</td>
      <td>83</td>
      <td>239</td>
      <td>303</td>
      <td>0</td>
      <td>321</td>
    </tr>
    <tr>
      <th>2021-06-09</th>
      <td>35</td>
      <td>372</td>
      <td>468</td>
      <td>2</td>
      <td>96</td>
      <td>978</td>
      <td>1265</td>
      <td>3</td>
      <td>1290</td>
    </tr>
    <tr>
      <th>2021-06-08</th>
      <td>60</td>
      <td>1068</td>
      <td>784</td>
      <td>2</td>
      <td>91</td>
      <td>1657</td>
      <td>1809</td>
      <td>14</td>
      <td>1953</td>
    </tr>
    <tr>
      <th>2021-06-07</th>
      <td>76</td>
      <td>1363</td>
      <td>891</td>
      <td>3</td>
      <td>101</td>
      <td>2052</td>
      <td>2359</td>
      <td>19</td>
      <td>2332</td>
    </tr>
    <tr>
      <th>2021-06-06</th>
      <td>89</td>
      <td>1498</td>
      <td>822</td>
      <td>2</td>
      <td>103</td>
      <td>2270</td>
      <td>2571</td>
      <td>22</td>
      <td>2544</td>
    </tr>
    <tr>
      <th>2021-06-05</th>
      <td>103</td>
      <td>1890</td>
      <td>1062</td>
      <td>1</td>
      <td>111</td>
      <td>2741</td>
      <td>2584</td>
      <td>26</td>
      <td>2553</td>
    </tr>
    <tr>
      <th>2021-06-04</th>
      <td>104</td>
      <td>2409</td>
      <td>1301</td>
      <td>3</td>
      <td>139</td>
      <td>3405</td>
      <td>2771</td>
      <td>31</td>
      <td>2340</td>
    </tr>
    <tr>
      <th>2021-06-03</th>
      <td>121</td>
      <td>2519</td>
      <td>1468</td>
      <td>5</td>
      <td>144</td>
      <td>3909</td>
      <td>3030</td>
      <td>38</td>
      <td>2158</td>
    </tr>
    <tr>
      <th>2021-06-02</th>
      <td>125</td>
      <td>2847</td>
      <td>1899</td>
      <td>5</td>
      <td>168</td>
      <td>4687</td>
      <td>3353</td>
      <td>35</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2021-06-01</th>
      <td>139</td>
      <td>3132</td>
      <td>2294</td>
      <td>13</td>
      <td>171</td>
      <td>5471</td>
      <td>3565</td>
      <td>42</td>
      <td>1860</td>
    </tr>
    <tr>
      <th>2021-05-31</th>
      <td>113</td>
      <td>3043</td>
      <td>2356</td>
      <td>13</td>
      <td>131</td>
      <td>5809</td>
      <td>3906</td>
      <td>47</td>
      <td>1820</td>
    </tr>
    <tr>
      <th>2021-05-30</th>
      <td>95</td>
      <td>3129</td>
      <td>2081</td>
      <td>14</td>
      <td>106</td>
      <td>5513</td>
      <td>3757</td>
      <td>55</td>
      <td>2410</td>
    </tr>
    <tr>
      <th>2021-05-29</th>
      <td>74</td>
      <td>3904</td>
      <td>2020</td>
      <td>11</td>
      <td>76</td>
      <td>5165</td>
      <td>3984</td>
      <td>55</td>
      <td>3472</td>
    </tr>
    <tr>
      <th>2021-05-28</th>
      <td>51</td>
      <td>4787</td>
      <td>1962</td>
      <td>11</td>
      <td>53</td>
      <td>4826</td>
      <td>5468</td>
      <td>48</td>
      <td>4613</td>
    </tr>
  </tbody>
</table>

- [Multi-Backend Summary Table File](https://github.com/pvieito/Radar-STATS/blob/master/Data/Resources/Current/RadarCOVID-Report-Multi-Backend-Summary-Table.csv)

#### Multi-Backend Cross-Sharing Summary Table

<table border="1" class="dataframe table-center">
  <thead>
    <tr style="text-align: center;">
      <th></th>
      <th colspan="9" halign="left">Fraction of TEKs in Backend (A) Available in Backend (B)</th>
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
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <th>CH</th>
      <td>-</td>
      <td>3.4%</td>
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
      <td>90.1%</td>
      <td>-</td>
      <td>93.6%</td>
      <td></td>
      <td>47.4%</td>
      <td>52.2%</td>
      <td></td>
      <td></td>
      <td>51.1%</td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>57.3%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>40.1%</td>
      <td></td>
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
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES</th>
      <td></td>
      <td>2.3%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>3.2%</td>
      <td></td>
      <td></td>
      <td>2.1%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>79.6%</td>
      <td>100.0%</td>
      <td></td>
      <td>100.0%</td>
      <td>-</td>
      <td></td>
      <td>100.0%</td>
      <td>72.7%</td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES-PRE</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.7%</td>
      <td></td>
      <td>-</td>
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
      <td>0.9%</td>
      <td></td>
      <td>-</td>
      <td>0.7%</td>
    </tr>
    <tr style="text-align: center;">
      <th>MT</th>
      <td></td>
      <td>50.6%</td>
      <td>47.5%</td>
      <td></td>
      <td>42.3%</td>
      <td>47.3%</td>
      <td></td>
      <td>47.6%</td>
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
