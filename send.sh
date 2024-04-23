echo "<html><body><p>${1}</p><a href="https://careersportal.taleo.net${2}">https://careersportal.taleo.net${2}</a></body></html>" > mailbody.html
#You can add more text to the mailbody.html file, but in html format
MAILFROM=fur43467@host-172-16-102-148.nubes.stfc.ac.uk
MAILTO=scdjobupdates@stfc365.onmicrosoft.com
SUBJECT="${1}"

( cat <<HERE; cat mailbody.html ) | sendmail -oi -t
From: ${MAILFROM}
To: ${MAILTO}
Subject: ${SUBJECT}
Content-Type: text/html

HERE
