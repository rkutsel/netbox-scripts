echo "127.0.0.1" > fping_hosts
fping=`cat fping_prefixes` 
for i in $fping; do
   sudo fping -c 1 -r 0 -i 1 -a -g "$i" >> fping_hosts 
done
