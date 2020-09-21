# RadarCOVID-Report

[![Report Update](https://github.com/pvieito/RadarCOVID-Report/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb)

Project to monitor and report hourly statistics about Spain's “Radar COVID” app Exposure Notification service.

## Links

- [Last Results](#last-results)
- [Documentation](#documentation)
- [Contributions](#contributions)
- [Related Links](#related-links)
- [Archived Reports](https://github.com/pvieito/RadarCOVID-Report/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/RadarCOVID-Report/tree/master/Data/TEKs)
- [Twitter Bot](https://twitter.com/radarcovidstats)

## Last Results

- [Report {extraction_date_with_hour}]({report_url_with_hour})

### Summary Table

{summary_table_html}

- [Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)

### Hourly Summary Plots

![RadarCOVID-Report-Hourly-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Hourly-Summary-Plots.png)

## Documentation

### Definitions

- **TEK** (Temporary Exposure Key): A random identifier generated on-device each day used by [Exposure Notification](https://developer.apple.com/documentation/exposurenotification) apps like Radar COVID to detect exposures and share positive diagnoses. When a user has a confirmed case of COVID-19, he can share the TEKs generated on-device from the last 14 days to the Radar COVID server through the app. Other devices then download the infected TEKs and check if they have detected them nearby via Bluetooth on the previous 14 days.

### Metrics

- **COVID-19 Cases** (`covid_cases`): Confirmed COVID-19 cases in Spain estimated with a 7-day rolling average.
- **Shared TEKs by Generation Date** (`shared_teks_by_generation_date`): TEKs uploaded to the Radar COVID server by the date they were generated on-device.
- **Shared TEKs by Upload Date** (`shared_teks_by_upload_date`): TEKs uploaded to the Radar COVID server by the date they were uploaded using the one-time code sent by the Health Authorities.
- **Shared Diagnoses** (`shared_diagnoses`): Estimation of the shared diagnoses via the Radar COVID app. The estimation is inferred from the number of TEKs uploaded each day which were generated on-device the previous day: typically each device sharing a positive diagnose should upload at least the TEK generated on-device the previous day.
- **Average Number of TEKs Uploaded per Shared Diagnose** (`teks_per_shared_diagnose`): The average number of TEKs upload with each shared diagnose. This number should ideally be around 13 TEKs uploaded for each shared diagnose.
- **Usage Ratio** (`shared_diagnoses_per_covid_case`): This is the ratio of shared diagnoses per COVID-19 case. Ideally it should be 100% (ie. all confirmed cases sharing their TEKs with Radar COVID). 

**NOTE**: TEKs on the Radar COVID server may be padded with artificial random TEKs to increase anonymization. Currently there is no known technique to detect such alterations, so metrics dependent on the number of uploaded TEKs (eg. shared diagnoses or usage ratio) may be lower than the estimated.

### Data Sources

- **COVID-19 Cases**: [Narrativa API](https://covid19tracking.narrativa.com)
- **TEKs**: [Radar COVID API](https://radarcovid.gob.es/)

## Contributions

Contributions to the **RadarCOVID-Report** are welcome, both as [Pull Requests](https://github.com/pvieito/RadarCOVID-Report/pulls) or [Issues](https://github.com/pvieito/RadarCOVID-Report/issues).

Only files on these directories should be modified as other files are generated automatically by the [Report Update GitHub Action](https://github.com/pvieito/RadarCOVID-Report/blob/master/.github/workflows/report-update.yml):

- `Data/Templates/`
- `Modules/`
- `Notebooks/*/Source/`

## Related Links

- [Radar COVID Website](https://radarcovid.gob.es/)
- [Radar COVID Project](https://github.com/RadarCOVID)
- [DP3T Project](https://github.com/DP-3T)
- [Diagnosis Key Analysis for Corona-Warn-App](https://github.com/micb25/dka/blob/master/README.en.md)
- [Testing Apps for COVID-19 Tracing (TACT) - TEK Survey](https://down.dsg.cs.tcd.ie/tact/tek-counts/)
- [European Federation Gateway Service (EFGS) Project](https://github.com/eu-federation-gateway-service/efgs-federation-gateway)