# Kellogg Foundation

This is for the Donations List Website: https://github.com/vipulnaik/donations

Specific issue: https://github.com/vipulnaik/donations/issues/67

## Getting data and generating SQL file

NOTE: before running `scrape.py`, go to https://www.wkkf.org/grants#pp=100
(make sure 100 grants are displayed per page) and scroll to the bottom and click
"LAST". Then find out the page number for the last page (shown at the bottom and
in the URL after `p=`). Then modify the `LAST_PAGE` variable in `scrape.py`.

`scrape.py` requires selenium and the chrome driver, so install that before
running the script.

```bash
today=$(date -Idate)

# Make new directory for data
mkdir data-retrieved-$today

# Download data
./scrape.py data-retrieved-$today

# Use the HTML files to generate the SQL file containing insert statements
./proc.py data-retrieved-$today > out-$today.sql
```

## License

CC0 for the code and readme.
