# RadarCOVID-Report

[![Report Update](https://github.com/pvieito/RadarCOVID-Report/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb)

Project to monitor and report the Temporary Exposure Keys (TEKs) from Spain's “Radar COVID” app Exposure Notification service.

## Links

- [Last Report](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb) 
- [Archived Reports](https://github.com/pvieito/RadarCOVID-Report/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/RadarCOVID-Report/tree/master/Data/TEKs)

## Last Results

- [Report 2020-09-17@20](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Hourly/RadarCOVID-Report-2020-09-17@20.ipynb)

### Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tek_count</th>
      <th>new_tek_count</th>
      <th>new_cases</th>
      <th>rolling_mean_new_cases</th>
      <th>tek_count_per_new_case</th>
      <th>new_tek_count_per_new_case</th>
      <th>new_tek_devices</th>
      <th>new_tek_devices_per_new_case</th>
      <th>new_tek_count_per_new_tek_device</th>
    </tr>
    <tr>
      <th>sample_date</th>
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
      <th>2020-09-17</th>
      <td>NaN</td>
      <td>30.0</td>
      <td>20280.285714</td>
      <td>20280.285714</td>
      <td>NaN</td>
      <td>0.001479</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-09-16</th>
      <td>NaN</td>
      <td>62.0</td>
      <td>22386.000000</td>
      <td>20280.285714</td>
      <td>NaN</td>
      <td>0.003057</td>
      <td>23.0</td>
      <td>0.001134</td>
      <td>2.695652</td>
    </tr>
    <tr>
      <th>2020-09-15</th>
      <td>32.0</td>
      <td>58.0</td>
      <td>18874.000000</td>
      <td>19615.428571</td>
      <td>0.001631</td>
      <td>0.002957</td>
      <td>23.0</td>
      <td>0.001173</td>
      <td>2.521739</td>
    </tr>
    <tr>
      <th>2020-09-14</th>
      <td>41.0</td>
      <td>61.0</td>
      <td>54808.000000</td>
      <td>19480.285714</td>
      <td>0.002105</td>
      <td>0.003131</td>
      <td>28.0</td>
      <td>0.001437</td>
      <td>2.178571</td>
    </tr>
    <tr>
      <th>2020-09-13</th>
      <td>55.0</td>
      <td>92.0</td>
      <td>0.000000</td>
      <td>19239.142857</td>
      <td>0.002859</td>
      <td>0.004782</td>
      <td>32.0</td>
      <td>0.001663</td>
      <td>2.875000</td>
    </tr>
    <tr>
      <th>2020-09-12</th>
      <td>66.0</td>
      <td>92.0</td>
      <td>0.000000</td>
      <td>19239.142857</td>
      <td>0.003431</td>
      <td>0.004782</td>
      <td>33.0</td>
      <td>0.001715</td>
      <td>2.787879</td>
    </tr>
    <tr>
      <th>2020-09-11</th>
      <td>75.0</td>
      <td>46.0</td>
      <td>24366.000000</td>
      <td>19239.142857</td>
      <td>0.003898</td>
      <td>0.002391</td>
      <td>19.0</td>
      <td>0.000988</td>
      <td>2.421053</td>
    </tr>
    <tr>
      <th>2020-09-10</th>
      <td>68.0</td>
      <td>45.0</td>
      <td>21528.000000</td>
      <td>18751.428571</td>
      <td>0.003626</td>
      <td>0.002400</td>
      <td>15.0</td>
      <td>0.000800</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2020-09-09</th>
      <td>60.0</td>
      <td>67.0</td>
      <td>17732.000000</td>
      <td>18235.714286</td>
      <td>0.003290</td>
      <td>0.003674</td>
      <td>21.0</td>
      <td>0.001152</td>
      <td>3.190476</td>
    </tr>
    <tr>
      <th>2020-09-08</th>
      <td>61.0</td>
      <td>44.0</td>
      <td>17928.000000</td>
      <td>18154.285714</td>
      <td>0.003360</td>
      <td>0.002424</td>
      <td>18.0</td>
      <td>0.000992</td>
      <td>2.444444</td>
    </tr>
    <tr>
      <th>2020-09-07</th>
      <td>58.0</td>
      <td>52.0</td>
      <td>53120.000000</td>
      <td>17911.714286</td>
      <td>0.003238</td>
      <td>0.002903</td>
      <td>22.0</td>
      <td>0.001228</td>
      <td>2.363636</td>
    </tr>
    <tr>
      <th>2020-09-06</th>
      <td>54.0</td>
      <td>60.0</td>
      <td>0.000000</td>
      <td>17058.000000</td>
      <td>0.003166</td>
      <td>0.003517</td>
      <td>24.0</td>
      <td>0.001407</td>
      <td>2.500000</td>
    </tr>
    <tr>
      <th>2020-09-05</th>
      <td>56.0</td>
      <td>40.0</td>
      <td>0.000000</td>
      <td>17058.000000</td>
      <td>0.003283</td>
      <td>0.002345</td>
      <td>17.0</td>
      <td>0.000997</td>
      <td>2.352941</td>
    </tr>
    <tr>
      <th>2020-09-04</th>
      <td>52.0</td>
      <td>NaN</td>
      <td>20952.000000</td>
      <td>17058.000000</td>
      <td>0.003048</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>0.001172</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Hourly Summary Plots

![RadarCOVID-Report-Hourly-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Hourly-Summary-Plots.png)
