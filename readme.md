# British and Irish Mountain Mapping

This repository creates KML files of mountain locations in the United Kingdom and Ireland based upon data from the Database of British and Irish Hills (DoBIH). The KML files can then be loaded into popular mapping software such as Google Maps.

## Code

There are four main files:

 - `pull_data.py`: Download zipped data directed from DoBIH and extract to the data folder.
 - `etl.py`: Filter DoBIH data for required mountain types and add columns such as country and P600 mountain type.
 - `build_maps.py`: Convert the output of the ETL into KML files.
 - `build_figures_and_stats.py`: Calculates the number of mountain types by country and lists the tallest mountains.

Running `main.py` will run all of these files in the correct order.

## UK and Irish Mountains

The table below shows the mountains per country. Due to some mountains spanning national borders, different sources might have slightly different figures in the table. Our code has counted a mountain as being in a country based on the first county (which we mapped to countries) in the DoBIH row.

|Country|Marilyn|HuMP|Simm|P600
|---|---|---|---|---|
|Channel Islands|0|3|0|0|
|England|175|441|193|4|
|Isle of Man|5|11|1|1|
|Northern Ireland|65|114|19|1|
|Republic of Ireland|389|717|203|23|
|Scotland|1218|2161|2189|82|
|Wales|158|366|149|7|

Below are the highest mountains in the UK. All can be found in Scotland.

|Rank|Mountain|Height (m)|
|---|---|---|
|1|Ben Nevis|1344.53|
|2|Ben Macdui|1309|
|3|Braeriach|1296|
|4|Cairn Toul|1291|
|5|Carn na Criche|1265|
|6|Sgor an Lochain Uaine|1258|
|7|Cairn Gorm|1244|
|8|Aonach Beag|1234|
|9|Carn Dearg|1221|
|10|Aonach Mor|1220.40|