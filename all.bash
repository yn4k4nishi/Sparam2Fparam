python3 s2f.py csv/s-param.csv > csv/f-param.csv 
python3 s2f.py csv/s-param-MSLonly.csv > csv/f-param-MSLonly.csv 
python3 calc_unit_f.py csv/f-param.csv csv/f-param-MSLonly.csv > csv/f-unit.csv 
python3 plot.py csv/f-unit.csv 