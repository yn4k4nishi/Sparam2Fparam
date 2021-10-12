# Sparam2Fparam
Convert S parameter to F parameter

# how to use
## s2f.py
- create HFSS model and simulate
- create Data table and export S parameter as CSV file.
    - header format : Freq[GHz], re(S(1,1)), im(S(1,1)), re(S(1,2)), ...
- `$ python3 s2f.py <exported csv file> >> <output csv file>`

## calc_unit_f.py
- prepare entire f parameter and only port one as csv file.
- edit calc_unit_f.py (`N=5` : unit cell number is 5)
- `$ python3 calc_unit_f.py <entire f param csv> <only port csv> >> <output file>`


