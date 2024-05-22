# Cloudflare DDNS
Dynamic DNS helper for [Cloudflare's Update DNS Record endpoint](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-patch-dns-record).

## Configuration
Requires: Bearer token, see: https://dash.cloudflare.com/profile/api-tokens. Does not support Global API key.

1. Create a copy of the config.yml template
`$ cp config.yml.template config.yml`
2. Edit BEARER_TOKEN, ZONE_ID, and A_RECORD_ID.


## Installing
1. Add files to `~/ddns`
2. Change permissions (rwx) to owner only 
    - `$ chmod 700 config.yml`
    - `$ chmod 700 ddns.py`
3. Add to crontab
    - `$ crontab -e`
    - Add `*/5 * * * * ~/ddns/ddns.py >/dev/null 2>&1` to crontab. Runs every five minutes.
6. Run `$ ./ddns.py` to test.
