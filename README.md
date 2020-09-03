# RadarCOVID-Report

[![Report Update](https://github.com/pvieito/RadarCOVID-Report/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb)

Project to monitor and report the Temporary Exposure Keys (TEKs) from Spain's “Radar COVID” app Exposure Notification service.

## Links

- [Last Report](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb) 
- [Archived Reports](https://github.com/pvieito/RadarCOVID-Report/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/RadarCOVID-Report/tree/master/Data/TEKs)

## Last Results

- [Report 2020-09-03@12](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Hourly/RadarCOVID-Report-2020-09-03@12.ipynb)

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
      <th>2020-09-03</th>
      <td>NaN</td>
      <td>25.0</td>
      <td>17058.571429</td>
      <td>17058.571429</td>
      <td>NaN</td>
      <td>0.001466</td>
      <td>11.0</td>
      <td>0.000645</td>
      <td>2.272727</td>
    </tr>
    <tr>
      <th>2020-09-02</th>
      <td>11.0</td>
      <td>57.0</td>
      <td>17162.000000</td>
      <td>17058.571429</td>
      <td>0.000645</td>
      <td>0.003341</td>
      <td>14.0</td>
      <td>0.000821</td>
      <td>4.071429</td>
    </tr>
    <tr>
      <th>2020-09-01</th>
      <td>18.0</td>
      <td>39.0</td>
      <td>16230.000000</td>
      <td>16691.428571</td>
      <td>0.001078</td>
      <td>0.002337</td>
      <td>14.0</td>
      <td>0.000839</td>
      <td>2.785714</td>
    </tr>
    <tr>
      <th>2020-08-31</th>
      <td>29.0</td>
      <td>63.0</td>
      <td>47144.000000</td>
      <td>16406.285714</td>
      <td>0.001768</td>
      <td>0.003840</td>
      <td>25.0</td>
      <td>0.001524</td>
      <td>2.520000</td>
    </tr>
    <tr>
      <th>2020-08-30</th>
      <td>46.0</td>
      <td>29.0</td>
      <td>0.000000</td>
      <td>15209.142857</td>
      <td>0.003024</td>
      <td>0.001907</td>
      <td>16.0</td>
      <td>0.001052</td>
      <td>1.812500</td>
    </tr>
    <tr>
      <th>2020-08-29</th>
      <td>47.0</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>15209.142857</td>
      <td>0.003090</td>
      <td>NaN</td>
      <td>27.0</td>
      <td>0.001775</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-28</th>
      <td>59.0</td>
      <td>NaN</td>
      <td>19558.000000</td>
      <td>15209.142857</td>
      <td>0.003879</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-27</th>
      <td>72.0</td>
      <td>NaN</td>
      <td>19316.000000</td>
      <td>14743.142857</td>
      <td>0.004884</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-26</th>
      <td>75.0</td>
      <td>NaN</td>
      <td>14592.000000</td>
      <td>13994.857143</td>
      <td>0.005359</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-25</th>
      <td>58.0</td>
      <td>NaN</td>
      <td>14234.000000</td>
      <td>13816.285714</td>
      <td>0.004198</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-24</th>
      <td>48.0</td>
      <td>NaN</td>
      <td>38764.000000</td>
      <td>13244.000000</td>
      <td>0.003624</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-23</th>
      <td>28.0</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>12354.571429</td>
      <td>0.002266</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-22</th>
      <td>18.0</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>12354.571429</td>
      <td>0.001457</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-21</th>
      <td>11.0</td>
      <td>NaN</td>
      <td>16296.000000</td>
      <td>12354.571429</td>
      <td>0.000890</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Hourly Summary Plots

![RadarCOVID-Report-Hourly-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Hourly-Summary-Plots.png)
