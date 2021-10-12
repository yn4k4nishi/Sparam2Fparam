# Sparam2Fparam
Convert S parameter to F parameter

# how to use
- create HFSS model and simulate
- create Data table and export CSV file.
    - header format : Freq[GHz], re(S(1,1)), im(S(1,1)), re(S(1,2)), ...
- `$ python3 s2f.py <exported csv file> >> <output csv file>`
