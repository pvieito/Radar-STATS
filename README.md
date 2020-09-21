# RadarCOVID-Report

[![Report Update](https://github.com/pvieito/RadarCOVID-Report/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb)

Project to monitor and report the Temporary Exposure Keys (TEKs) from Spain's “Radar COVID” app Exposure Notification service.

## Links

- [Last Report](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb) 
- [Archived Reports](https://github.com/pvieito/RadarCOVID-Report/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/RadarCOVID-Report/tree/master/Data/TEKs)
- [Twitter Bot](https://twitter.com/radarcovidstats)

## Last Results

- [Report 2020-09-21@08](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Hourly/RadarCOVID-Report-2020-09-21@08.ipynb)

### Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rolling_mean_new_cases</th>
      <th>tek_count</th>
      <th>new_tek_count</th>
      <th>new_tek_devices</th>
      <th>tek_count_per_new_case</th>
      <th>new_tek_count_per_new_case</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-09-21</th>
      <td>10531.0</td>
      <td>NaN</td>
      <td>38.0</td>
      <td>8</td>
      <td>NaN</td>
      <td>0.003608</td>
      <td>0.000760</td>
      <td>4.750000</td>
    </tr>
    <tr>
      <th>2020-09-20</th>
      <td>10531.0</td>
      <td>8.0</td>
      <td>116.0</td>
      <td>45</td>
      <td>0.000760</td>
      <td>0.011015</td>
      <td>0.004273</td>
      <td>2.577778</td>
    </tr>
    <tr>
      <th>2020-09-19</th>
      <td>10531.0</td>
      <td>55.0</td>
      <td>90.0</td>
      <td>39</td>
      <td>0.005223</td>
      <td>0.008546</td>
      <td>0.003703</td>
      <td>2.307692</td>
    </tr>
    <tr>
      <th>2020-09-18</th>
      <td>10531.0</td>
      <td>69.0</td>
      <td>138.0</td>
      <td>52</td>
      <td>0.006552</td>
      <td>0.013104</td>
      <td>0.004938</td>
      <td>2.653846</td>
    </tr>
    <tr>
      <th>2020-09-17</th>
      <td>10215.0</td>
      <td>88.0</td>
      <td>63.0</td>
      <td>29</td>
      <td>0.008615</td>
      <td>0.006167</td>
      <td>0.002839</td>
      <td>2.172414</td>
    </tr>
    <tr>
      <th>2020-09-16</th>
      <td>10140.0</td>
      <td>92.0</td>
      <td>62.0</td>
      <td>23</td>
      <td>0.009073</td>
      <td>0.006114</td>
      <td>0.002268</td>
      <td>2.695652</td>
    </tr>
    <tr>
      <th>2020-09-15</th>
      <td>9808.0</td>
      <td>82.0</td>
      <td>58.0</td>
      <td>23</td>
      <td>0.008361</td>
      <td>0.005914</td>
      <td>0.002345</td>
      <td>2.521739</td>
    </tr>
    <tr>
      <th>2020-09-14</th>
      <td>9740.0</td>
      <td>73.0</td>
      <td>61.0</td>
      <td>28</td>
      <td>0.007495</td>
      <td>0.006263</td>
      <td>0.002875</td>
      <td>2.178571</td>
    </tr>
    <tr>
      <th>2020-09-13</th>
      <td>9620.0</td>
      <td>75.0</td>
      <td>92.0</td>
      <td>32</td>
      <td>0.007796</td>
      <td>0.009563</td>
      <td>0.003326</td>
      <td>2.875000</td>
    </tr>
    <tr>
      <th>2020-09-12</th>
      <td>9620.0</td>
      <td>67.0</td>
      <td>92.0</td>
      <td>33</td>
      <td>0.006965</td>
      <td>0.009563</td>
      <td>0.003430</td>
      <td>2.787879</td>
    </tr>
    <tr>
      <th>2020-09-11</th>
      <td>9620.0</td>
      <td>75.0</td>
      <td>46.0</td>
      <td>19</td>
      <td>0.007796</td>
      <td>0.004782</td>
      <td>0.001975</td>
      <td>2.421053</td>
    </tr>
    <tr>
      <th>2020-09-10</th>
      <td>9376.0</td>
      <td>68.0</td>
      <td>45.0</td>
      <td>15</td>
      <td>0.007253</td>
      <td>0.004799</td>
      <td>0.001600</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2020-09-09</th>
      <td>9118.0</td>
      <td>60.0</td>
      <td>67.0</td>
      <td>21</td>
      <td>0.006580</td>
      <td>0.007348</td>
      <td>0.002303</td>
      <td>3.190476</td>
    </tr>
    <tr>
      <th>2020-09-08</th>
      <td>9077.0</td>
      <td>61.0</td>
      <td>44.0</td>
      <td>18</td>
      <td>0.006720</td>
      <td>0.004847</td>
      <td>0.001983</td>
      <td>2.444444</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Hourly Summary Plots

![RadarCOVID-Report-Hourly-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Hourly-Summary-Plots.png)

## Related Links

- [Radar COVID Project](https://github.com/RadarCOVID)
- [DP3T Project](https://github.com/DP-3T)
- [Diagnosis Key Analysis for Corona-Warn-App](https://github.com/micb25/dka/blob/master/README.en.md)
- [Testing Apps for COVID-19 Tracing (TACT) - TEK Survey](https://down.dsg.cs.tcd.ie/tact/tek-counts/)
- [European Federation Gateway Service (EFGS) Project](https://github.com/eu-federation-gateway-service/efgs-federation-gateway)