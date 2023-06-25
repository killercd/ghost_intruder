#!/bin/bash
target=$1
ftpuser=anonymous
ftppass=pass@tellme.com
outdir=outscan
ftpoutdir=ftpfiles
whoisoutdir=whoisfiles

mkdir -p $outdir/$ftpoutdir
mkdir -p $outdir/$whoisoutdir
cat << EOF > batchftp
quote USER $ftpuser
quote PASS $ftppass
pwd
passive off
ls
quit
EOF

for ip in $(nmap -sT -P0 -T3 --open -oG - -p 21 $target | grep -i open | awk '{print $2}' | grep -iv nmap); do
  
  outscan=$(hydra -l $ftpuser -p $ftppass ftp://$ip | grep -i login | grep -i password)
  if [[ -n "$outscan" ]]; then
    whois $ip | tee "$outdir/$whoisoutdir/$ip"
    ftp -n $ip < batchftp | tee "$outdir/$ftpoutdir/$ip"
  fi
done