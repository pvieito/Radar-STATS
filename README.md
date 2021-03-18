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

- [Report 2021-03-18@08](https://github.com/pvieito/Radar-STATS/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb)

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
      <th>2021-03-18</th>
      <th>ES</th>
      <td>6092</td>
      <td></td>
      <td>44</td>
      <td></td>
      <td>16</td>
      <td>2.75</td>
      <td>0.26%</td>
      <td>6092</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-03-17</th>
      <th>ES</th>
      <td>4859</td>
      <td>108</td>
      <td>347</td>
      <td>92</td>
      <td>92</td>
      <td>3.77</td>
      <td>1.89%</td>
      <td>4859</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-03-16</th>
      <th>ES</th>
      <td>5006</td>
      <td>143</td>
      <td>303</td>
      <td>76</td>
      <td>76</td>
      <td>3.99</td>
      <td>1.52%</td>
      <td>5006</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-03-15</th>
      <th>ES</th>
      <td>4870</td>
      <td>173</td>
      <td>305</td>
      <td>69</td>
      <td>69</td>
      <td>4.42</td>
      <td>1.42%</td>
      <td>4870</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2021-03-14</th>
      <th>ES</th>
      <td>4956</td>
      <td>217</td>
      <td>304</td>
      <td>69</td>
      <td>69</td>
      <td>4.41</td>
      <td>1.39%</td>
      <td>4956</td>
      <td>3285</td>
      <td>104</td>
      <td>2.10%</td>
    </tr>
    <tr>
      <th>2021-03-13</th>
      <th>ES</th>
      <td>4956</td>
      <td>257</td>
      <td>302</td>
      <td>84</td>
      <td>84</td>
      <td>3.60</td>
      <td>1.69%</td>
      <td>4956</td>
      <td>3285</td>
      <td>104</td>
      <td>2.10%</td>
    </tr>
    <tr>
      <th>2021-03-12</th>
      <th>ES</th>
      <td>4956</td>
      <td>304</td>
      <td>368</td>
      <td>101</td>
      <td>101</td>
      <td>3.64</td>
      <td>2.04%</td>
      <td>4956</td>
      <td>3285</td>
      <td>104</td>
      <td>2.10%</td>
    </tr>
    <tr>
      <th>2021-03-11</th>
      <th>ES</th>
      <td>5143</td>
      <td>345</td>
      <td>515</td>
      <td>122</td>
      <td>122</td>
      <td>4.22</td>
      <td>2.37%</td>
      <td>5143</td>
      <td>3285</td>
      <td>104</td>
      <td>2.02%</td>
    </tr>
    <tr>
      <th>2021-03-10</th>
      <th>ES</th>
      <td>5111</td>
      <td>379</td>
      <td>410</td>
      <td>109</td>
      <td>109</td>
      <td>3.76</td>
      <td>2.13%</td>
      <td>5111</td>
      <td>3285</td>
      <td>104</td>
      <td>2.03%</td>
    </tr>
    <tr>
      <th>2021-03-09</th>
      <th>ES</th>
      <td>4971</td>
      <td>379</td>
      <td>366</td>
      <td>96</td>
      <td>96</td>
      <td>3.81</td>
      <td>1.93%</td>
      <td>4971</td>
      <td>3285</td>
      <td>104</td>
      <td>2.09%</td>
    </tr>
    <tr>
      <th>2021-03-08</th>
      <th>ES</th>
      <td>4398</td>
      <td>368</td>
      <td>354</td>
      <td>78</td>
      <td>78</td>
      <td>4.54</td>
      <td>1.77%</td>
      <td>4398</td>
      <td>3285</td>
      <td>104</td>
      <td>2.36%</td>
    </tr>
    <tr>
      <th>2021-03-07</th>
      <th>ES</th>
      <td>4972</td>
      <td>273</td>
      <td>235</td>
      <td>49</td>
      <td>49</td>
      <td>4.80</td>
      <td>0.99%</td>
      <td>4972</td>
      <td>3686</td>
      <td>99</td>
      <td>1.99%</td>
    </tr>
    <tr>
      <th>2021-03-06</th>
      <th>ES</th>
      <td>4972</td>
      <td>204</td>
      <td>380</td>
      <td>85</td>
      <td>85</td>
      <td>4.47</td>
      <td>1.71%</td>
      <td>4972</td>
      <td>3686</td>
      <td>99</td>
      <td>1.99%</td>
    </tr>
    <tr>
      <th>2021-03-05</th>
      <th>ES</th>
      <td>4972</td>
      <td>145</td>
      <td>419</td>
      <td>89</td>
      <td>89</td>
      <td>4.71</td>
      <td>1.79%</td>
      <td>4972</td>
      <td>3686</td>
      <td>99</td>
      <td>1.99%</td>
    </tr>
    <tr>
      <th>2021-03-04</th>
      <th>ES</th>
      <td>5213</td>
      <td>120</td>
      <td>470</td>
      <td>104</td>
      <td>104</td>
      <td>4.52</td>
      <td>2.00%</td>
      <td>5213</td>
      <td>3686</td>
      <td>99</td>
      <td>1.90%</td>
    </tr>
    <tr>
      <th>2021-03-03</th>
      <th>ES</th>
      <td>5718</td>
      <td>96</td>
      <td>521</td>
      <td>112</td>
      <td>112</td>
      <td>4.65</td>
      <td>1.96%</td>
      <td>5718</td>
      <td>3686</td>
      <td>99</td>
      <td>1.73%</td>
    </tr>
    <tr>
      <th>2021-03-02</th>
      <th>ES</th>
      <td>6157</td>
      <td>104</td>
      <td>385</td>
      <td>88</td>
      <td>88</td>
      <td>4.38</td>
      <td>1.43%</td>
      <td>6157</td>
      <td>3686</td>
      <td>99</td>
      <td>1.61%</td>
    </tr>
    <tr>
      <th>2021-03-01</th>
      <th>ES</th>
      <td>7223</td>
      <td>110</td>
      <td>270</td>
      <td>71</td>
      <td>71</td>
      <td>3.80</td>
      <td>0.98%</td>
      <td>7223</td>
      <td>3686</td>
      <td>99</td>
      <td>1.37%</td>
    </tr>
    <tr>
      <th>2021-02-28</th>
      <th>ES</th>
      <td>7919</td>
      <td>127</td>
      <td>279</td>
      <td>68</td>
      <td>68</td>
      <td>4.10</td>
      <td>0.86%</td>
      <td>7919</td>
      <td>3820</td>
      <td>124</td>
      <td>1.57%</td>
    </tr>
    <tr>
      <th>2021-02-27</th>
      <th>ES</th>
      <td>7919</td>
      <td>133</td>
      <td>371</td>
      <td>94</td>
      <td>94</td>
      <td>3.95</td>
      <td>1.19%</td>
      <td>7919</td>
      <td>3820</td>
      <td>124</td>
      <td>1.57%</td>
    </tr>
    <tr>
      <th>2021-02-26</th>
      <th>ES</th>
      <td>7919</td>
      <td>127</td>
      <td>541</td>
      <td>130</td>
      <td>130</td>
      <td>4.16</td>
      <td>1.64%</td>
      <td>7919</td>
      <td>3820</td>
      <td>124</td>
      <td>1.57%</td>
    </tr>
    <tr>
      <th>2021-02-25</th>
      <th>ES</th>
      <td>8361</td>
      <td>116</td>
      <td>365</td>
      <td>101</td>
      <td>101</td>
      <td>3.61</td>
      <td>1.21%</td>
      <td>8361</td>
      <td>3820</td>
      <td>124</td>
      <td>1.48%</td>
    </tr>
    <tr>
      <th>2021-02-24</th>
      <th>ES</th>
      <td>9067</td>
      <td>110</td>
      <td>582</td>
      <td>149</td>
      <td>149</td>
      <td>3.91</td>
      <td>1.64%</td>
      <td>9067</td>
      <td>3820</td>
      <td>124</td>
      <td>1.37%</td>
    </tr>
    <tr>
      <th>2021-02-23</th>
      <th>ES</th>
      <td>9298</td>
      <td>114</td>
      <td>519</td>
      <td>131</td>
      <td>131</td>
      <td>3.96</td>
      <td>1.41%</td>
      <td>9298</td>
      <td>3820</td>
      <td>124</td>
      <td>1.33%</td>
    </tr>
    <tr>
      <th>2021-02-22</th>
      <th>ES</th>
      <td>9669</td>
      <td>134</td>
      <td>394</td>
      <td>102</td>
      <td>102</td>
      <td>3.86</td>
      <td>1.05%</td>
      <td>9669</td>
      <td>3820</td>
      <td>124</td>
      <td>1.28%</td>
    </tr>
    <tr>
      <th>2021-02-21</th>
      <th>ES</th>
      <td>11012</td>
      <td>132</td>
      <td>429</td>
      <td>96</td>
      <td>96</td>
      <td>4.47</td>
      <td>0.87%</td>
      <td>11012</td>
      <td>5865</td>
      <td>168</td>
      <td>1.53%</td>
    </tr>
    <tr>
      <th>2021-02-20</th>
      <th>ES</th>
      <td>11012</td>
      <td>126</td>
      <td>538</td>
      <td>132</td>
      <td>132</td>
      <td>4.08</td>
      <td>1.20%</td>
      <td>11012</td>
      <td>5865</td>
      <td>168</td>
      <td>1.53%</td>
    </tr>
    <tr>
      <th>2021-02-19</th>
      <th>ES,AT,BE,DE,DK,FI,HR,IE,IT,LV,NL,NO,PL,SI</th>
      <td>47784</td>
      <td>139</td>
      <td>18484</td>
      <td>822</td>
      <td>2453</td>
      <td>7.54</td>
      <td>5.13%</td>
      <td>11012</td>
      <td>5865</td>
      <td>168</td>
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
      <th>2021-03-18</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2021-03-17</th>
      <td>179</td>
      <td>2819</td>
      <td>2917</td>
      <td>67</td>
      <td>108</td>
      <td>3321</td>
      <td>331</td>
      <td>0</td>
      <td>100</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2021-03-16</th>
      <td>333</td>
      <td>6501</td>
      <td>5257</td>
      <td>142</td>
      <td>143</td>
      <td>7079</td>
      <td>8374</td>
      <td>135</td>
      <td>103</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-15</th>
      <td>472</td>
      <td>7457</td>
      <td>5478</td>
      <td>204</td>
      <td>173</td>
      <td>8382</td>
      <td>9120</td>
      <td>214</td>
      <td>103</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-14</th>
      <td>529</td>
      <td>7775</td>
      <td>5084</td>
      <td>254</td>
      <td>217</td>
      <td>8986</td>
      <td>9754</td>
      <td>303</td>
      <td>105</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-13</th>
      <td>580</td>
      <td>9887</td>
      <td>6643</td>
      <td>309</td>
      <td>257</td>
      <td>11326</td>
      <td>10470</td>
      <td>333</td>
      <td>110</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-12</th>
      <td>591</td>
      <td>12191</td>
      <td>8522</td>
      <td>333</td>
      <td>304</td>
      <td>13886</td>
      <td>11154</td>
      <td>372</td>
      <td>109</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-11</th>
      <td>651</td>
      <td>13508</td>
      <td>9529</td>
      <td>370</td>
      <td>345</td>
      <td>15438</td>
      <td>11837</td>
      <td>449</td>
      <td>114</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-10</th>
      <td>628</td>
      <td>14688</td>
      <td>10571</td>
      <td>408</td>
      <td>379</td>
      <td>16860</td>
      <td>17503</td>
      <td>502</td>
      <td>114</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-09</th>
      <td>614</td>
      <td>15833</td>
      <td>11660</td>
      <td>404</td>
      <td>379</td>
      <td>18319</td>
      <td>23205</td>
      <td>558</td>
      <td>113</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-08</th>
      <td>624</td>
      <td>15617</td>
      <td>11457</td>
      <td>418</td>
      <td>368</td>
      <td>18290</td>
      <td>28712</td>
      <td>561</td>
      <td>117</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2021-03-07</th>
      <td>465</td>
      <td>15057</td>
      <td>10615</td>
      <td>414</td>
      <td>273</td>
      <td>17171</td>
      <td>34140</td>
      <td>611</td>
      <td>118</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-06</th>
      <td>346</td>
      <td>15985</td>
      <td>10451</td>
      <td>429</td>
      <td>204</td>
      <td>16084</td>
      <td>39417</td>
      <td>539</td>
      <td>121</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2021-03-05</th>
      <td>233</td>
      <td>16994</td>
      <td>10238</td>
      <td>446</td>
      <td>145</td>
      <td>15084</td>
      <td>44884</td>
      <td>456</td>
      <td>122</td>
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
      <td></td>
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
      <td></td>
      <td>-</td>
      <td>99.7%</td>
      <td></td>
      <td>88.9%</td>
      <td>86.0%</td>
      <td></td>
      <td>0.2%</td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>DE@ES</th>
      <td></td>
      <td>70.1%</td>
      <td>-</td>
      <td></td>
      <td></td>
      <td>63.7%</td>
      <td></td>
      <td></td>
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
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>ES</th>
      <td></td>
      <td>1.9%</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>1.9%</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr style="text-align: center;">
      <th>EU@ES</th>
      <td></td>
      <td>94.8%</td>
      <td>100.0%</td>
      <td></td>
      <td>100.0%</td>
      <td>-</td>
      <td></td>
      <td>100.0%</td>
      <td></td>
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
      <td>3.0%</td>
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
