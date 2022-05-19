# openssl inspect cert

## local cert
`openssl x509 -in certificate.crt -text -noout`

## remote cert
`openssl s_client -showcerts -connect rally1.rallydev.com:443 | openssl x509 -noout -text`

or 

`curl -vIk https://rally1.rallydev.com`
