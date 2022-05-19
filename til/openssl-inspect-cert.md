# openssl inspect cert

## local cert
`openssl x509 -in certificate.crt -text -noout`

## remote cert
`openssl s_client -showcerts -connect rally1.rallydev.com:443 | openssl x509 -noout -text`

or 

`curl -vvI --resolve actual-hostname:443:localhost  https://actual-hostname`


## Compare certs
`diff <(openssl x509 -in cert1.pem -modulus -fingerprint) <(openssl x509 -in cert2.pem -modulus -fingerprint)`

Things to compare:
```
-serial -subject_hash -issuer_hash -hash -subject -issuer -email -startdate -enddate -purpose -dates -modulus -pubkey -fingerprint -alias -noout -nocert -ocspid -ocsp_uri -trustout -clrtrust -clrext -addtrust -addreject -setalias -days -checkend
```
