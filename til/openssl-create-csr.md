# Openssl create signing cert (csr)

To craete a CSR for an existing key using openssl:

`openssl req -new -out ~/my.csr -key my.key -nodes -subj "/C=US/ST=CA/L=Santa Clara/O=My Company/OU=/CN=*.mydomain.com"`
