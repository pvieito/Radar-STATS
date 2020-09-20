# RadarCOVID-Report

[![Report Update](https://github.com/pvieito/RadarCOVID-Report/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb)

Project to monitor and report the Temporary Exposure Keys (TEKs) from Spain's “Radar COVID” app Exposure Notification service.

## Links

- [Last Report](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Current/RadarCOVID-Report.ipynb) 
- [Archived Reports](https://github.com/pvieito/RadarCOVID-Report/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/RadarCOVID-Report/tree/master/Data/TEKs)
- [Twitter Bot](https://twitter.com/radarcovidstats)

## Last Results

- [Report 2020-09-20@20](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Hourly/RadarCOVID-Report-2020-09-20@20.ipynb)

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
      <th>2020-09-20</th>
      <td>21061.0</td>
      <td>NaN</td>
      <td>111.0</td>
      <td>44</td>
      <td>NaN</td>
      <td>0.005270</td>
      <td>0.002089</td>
      <td>2.522727</td>
    </tr>
    <tr>
      <th>2020-09-19</th>
      <td>21061.0</td>
      <td>46.0</td>
      <td>90.0</td>
      <td>39</td>
      <td>0.002184</td>
      <td>0.004273</td>
      <td>0.001852</td>
      <td>2.307692</td>
    </tr>
    <tr>
      <th>2020-09-18</th>
      <td>21061.0</td>
      <td>60.0</td>
      <td>138.0</td>
      <td>52</td>
      <td>0.002849</td>
      <td>0.006552</td>
      <td>0.002469</td>
      <td>2.653846</td>
    </tr>
    <tr>
      <th>2020-09-17</th>
      <td>20431.0</td>
      <td>80.0</td>
      <td>63.0</td>
      <td>29</td>
      <td>0.003916</td>
      <td>0.003084</td>
      <td>0.001419</td>
      <td>2.172414</td>
    </tr>
    <tr>
      <th>2020-09-16</th>
      <td>20280.0</td>
      <td>84.0</td>
      <td>62.0</td>
      <td>23</td>
      <td>0.004142</td>
      <td>0.003057</td>
      <td>0.001134</td>
      <td>2.695652</td>
    </tr>
    <tr>
      <th>2020-09-15</th>
      <td>19615.0</td>
      <td>81.0</td>
      <td>58.0</td>
      <td>23</td>
      <td>0.004129</td>
      <td>0.002957</td>
      <td>0.001173</td>
      <td>2.521739</td>
    </tr>
    <tr>
      <th>2020-09-14</th>
      <td>19480.0</td>
      <td>73.0</td>
      <td>61.0</td>
      <td>28</td>
      <td>0.003747</td>
      <td>0.003131</td>
      <td>0.001437</td>
      <td>2.178571</td>
    </tr>
    <tr>
      <th>2020-09-13</th>
      <td>19239.0</td>
      <td>75.0</td>
      <td>92.0</td>
      <td>32</td>
      <td>0.003898</td>
      <td>0.004782</td>
      <td>0.001663</td>
      <td>2.875000</td>
    </tr>
    <tr>
      <th>2020-09-12</th>
      <td>19239.0</td>
      <td>67.0</td>
      <td>92.0</td>
      <td>33</td>
      <td>0.003483</td>
      <td>0.004782</td>
      <td>0.001715</td>
      <td>2.787879</td>
    </tr>
    <tr>
      <th>2020-09-11</th>
      <td>19239.0</td>
      <td>75.0</td>
      <td>46.0</td>
      <td>19</td>
      <td>0.003898</td>
      <td>0.002391</td>
      <td>0.000988</td>
      <td>2.421053</td>
    </tr>
    <tr>
      <th>2020-09-10</th>
      <td>18751.0</td>
      <td>68.0</td>
      <td>45.0</td>
      <td>15</td>
      <td>0.003626</td>
      <td>0.002400</td>
      <td>0.000800</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2020-09-09</th>
      <td>18236.0</td>
      <td>60.0</td>
      <td>67.0</td>
      <td>21</td>
      <td>0.003290</td>
      <td>0.003674</td>
      <td>0.001152</td>
      <td>3.190476</td>
    </tr>
    <tr>
      <th>2020-09-08</th>
      <td>18154.0</td>
      <td>61.0</td>
      <td>44.0</td>
      <td>18</td>
      <td>0.003360</td>
      <td>0.002424</td>
      <td>0.000992</td>
      <td>2.444444</td>
    </tr>
    <tr>
      <th>2020-09-07</th>
      <td>17912.0</td>
      <td>58.0</td>
      <td>NaN</td>
      <td>22</td>
      <td>0.003238</td>
      <td>NaN</td>
      <td>0.001228</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Hourly Summary Plots

![RadarCOVID-Report-Hourly-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Hourly-Summary-Plots.png)

### Multi-Region Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>tek_count</th>
    </tr>
    <tr>
      <th>region</th>
      <th>ES</th>
    </tr>
    <tr>
      <th>sample_date_string</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-09-19</th>
      <td>46</td>
    </tr>
    <tr>
      <th>2020-09-18</th>
      <td>60</td>
    </tr>
    <tr>
      <th>2020-09-17</th>
      <td>80</td>
    </tr>
    <tr>
      <th>2020-09-16</th>
      <td>84</td>
    </tr>
    <tr>
      <th>2020-09-15</th>
      <td>81</td>
    </tr>
    <tr>
      <th>2020-09-14</th>
      <td>73</td>
    </tr>
    <tr>
      <th>2020-09-13</th>
      <td>75</td>
    </tr>
    <tr>
      <th>2020-09-12</th>
      <td>67</td>
    </tr>
    <tr>
      <th>2020-09-11</th>
      <td>75</td>
    </tr>
    <tr>
      <th>2020-09-10</th>
      <td>68</td>
    </tr>
    <tr>
      <th>2020-09-09</th>
      <td>60</td>
    </tr>
    <tr>
      <th>2020-09-08</th>
      <td>61</td>
    </tr>
    <tr>
      <th>2020-09-07</th>
      <td>58</td>
    </tr>
  </tbody>
</table>

- [Multi-Region Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Multi-Region-Summary-Table.csv)

## Related Links

- [Radar COVID Project](https://github.com/RadarCOVID)
- [DP3T Project](https://github.com/DP-3T)
- [Diagnosis Key Analysis for Corona-Warn-App](https://github.com/micb25/dka/blob/master/README.en.md)
- [Testing Apps for COVID-19 Tracing (TACT) - TEK Survey](https://down.dsg.cs.tcd.ie/tact/tek-counts/)
- [European Federation Gateway Service (EFGS) Project](https://github.com/eu-federation-gateway-service/efgs-federation-gateway)