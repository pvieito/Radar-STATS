# RadarCOVID-Report

[![Report Update](https://github.com/pvieito/RadarCOVID-Report/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb)

Project to monitor and report the Temporary Exposure Keys (TEKs) from Spain's “Radar COVID” app Exposure Notification service.

## Links

- [Last Report](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb) 
- [Archived Reports](https://github.com/pvieito/RadarCOVID-Report/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/RadarCOVID-Report/tree/master/Data/TEKs)

## Last Results

- [Report 2020-09-09@02](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Hourly/RadarCOVID-Report-2020-09-09@02.ipynb)

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
      <th>2020-09-09</th>
      <td>NaN</td>
      <td>4.0</td>
      <td>18154.285714</td>
      <td>18154.285714</td>
      <td>NaN</td>
      <td>0.000220</td>
      <td>3.0</td>
      <td>0.000165</td>
      <td>1.333333</td>
    </tr>
    <tr>
      <th>2020-09-08</th>
      <td>3.0</td>
      <td>44.0</td>
      <td>17928.000000</td>
      <td>18154.285714</td>
      <td>0.000165</td>
      <td>0.002424</td>
      <td>18.0</td>
      <td>0.000992</td>
      <td>2.444444</td>
    </tr>
    <tr>
      <th>2020-09-07</th>
      <td>18.0</td>
      <td>52.0</td>
      <td>53120.000000</td>
      <td>17911.714286</td>
      <td>0.001005</td>
      <td>0.002903</td>
      <td>22.0</td>
      <td>0.001228</td>
      <td>2.363636</td>
    </tr>
    <tr>
      <th>2020-09-06</th>
      <td>30.0</td>
      <td>60.0</td>
      <td>0.000000</td>
      <td>17058.000000</td>
      <td>0.001759</td>
      <td>0.003517</td>
      <td>24.0</td>
      <td>0.001407</td>
      <td>2.500000</td>
    </tr>
    <tr>
      <th>2020-09-05</th>
      <td>37.0</td>
      <td>40.0</td>
      <td>0.000000</td>
      <td>17058.000000</td>
      <td>0.002169</td>
      <td>0.002345</td>
      <td>17.0</td>
      <td>0.000997</td>
      <td>2.352941</td>
    </tr>
    <tr>
      <th>2020-09-04</th>
      <td>41.0</td>
      <td>58.0</td>
      <td>20952.000000</td>
      <td>17058.000000</td>
      <td>0.002404</td>
      <td>0.003400</td>
      <td>20.0</td>
      <td>0.001172</td>
      <td>2.900000</td>
    </tr>
    <tr>
      <th>2020-09-03</th>
      <td>51.0</td>
      <td>49.0</td>
      <td>17918.000000</td>
      <td>16858.857143</td>
      <td>0.003025</td>
      <td>0.002906</td>
      <td>19.0</td>
      <td>0.001127</td>
      <td>2.578947</td>
    </tr>
    <tr>
      <th>2020-09-02</th>
      <td>52.0</td>
      <td>57.0</td>
      <td>17162.000000</td>
      <td>17058.571429</td>
      <td>0.003048</td>
      <td>0.003341</td>
      <td>14.0</td>
      <td>0.000821</td>
      <td>4.071429</td>
    </tr>
    <tr>
      <th>2020-09-01</th>
      <td>46.0</td>
      <td>39.0</td>
      <td>16230.000000</td>
      <td>16691.428571</td>
      <td>0.002756</td>
      <td>0.002337</td>
      <td>14.0</td>
      <td>0.000839</td>
      <td>2.785714</td>
    </tr>
    <tr>
      <th>2020-08-31</th>
      <td>47.0</td>
      <td>63.0</td>
      <td>47144.000000</td>
      <td>16406.285714</td>
      <td>0.002865</td>
      <td>0.003840</td>
      <td>25.0</td>
      <td>0.001524</td>
      <td>2.520000</td>
    </tr>
    <tr>
      <th>2020-08-30</th>
      <td>59.0</td>
      <td>29.0</td>
      <td>0.000000</td>
      <td>15209.142857</td>
      <td>0.003879</td>
      <td>0.001907</td>
      <td>16.0</td>
      <td>0.001052</td>
      <td>1.812500</td>
    </tr>
    <tr>
      <th>2020-08-29</th>
      <td>49.0</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>15209.142857</td>
      <td>0.003222</td>
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
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Hourly Summary Plots

![RadarCOVID-Report-Hourly-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Hourly-Summary-Plots.png)
