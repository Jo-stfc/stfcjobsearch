x=1
rm -rf test*
while ((x>=1))
do
  google-chrome --enable-features=ConversionMeasurement,AttributionReportingCrossAppWeb --no-sandbox --headless --dump-dom --virtual-time-budget=10000 --timeout=10000 --run-all-compositor-stages-before-draw --disable-gpu --user-agent="Mozilla/5.0 (X11; Linux x86_64)" "https://careersportal.taleo.net/careersection/UKRI_INT/jobsearch.ftl?KEYWORD=Scientific%20Computing&page=${x}&lang=en#" > test${x}.html
  python3 printhtml.py
  if (( $?==1 ))
  then
	  x=-1
  fi
  ((x+=1))
  done
python3 parsehtml.py
