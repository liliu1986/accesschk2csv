# accesschk2csv

This utility is aimed to help user to collect permission stats for windows file system
It utilized the official accesschk from MS and covert the output to a csv file

# Usage

## Collects data

Currently, we take inputs from following command, for future improvement, we mignt need to combine all the steps

```bash
$ AccessChk/accesschk64.exe -d -s [Target Folder Path] > folder.data
```

## Create csv file
```bash
$ python convert2csv.py folder.data
```
The output file is out.csv

# License

MIT
