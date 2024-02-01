# http x-forwarded-host redirection 

when your client isn't responding with the url you expect: (for example if the client thinks it's
name is `http://bar.com` but you want it to repsond with `http://foo.com`)

`client --> haproxy --> nginx ingress --> server `

`X-Forwarded-Host` is a standard header used in HTTP requests. It's part of the
`X-Forwarded-*` headers, which also include X-Forwarded-For, X-Forwarded-Proto,
and sometimes X-Forwarded-Port. These headers are used by proxies, load
balancers, and other network intermediaries to provide information about the
original request to the target server.

If the client is connecting to your http://foo.com  through a proxy, and 
the backend want to reply with http://bar.com  then you can use the 
`X-Forwarded-Host` header to tell the backend to reply back on http://foo.com and
not bar.com

In the above example, you would add a `http-request set-header X-Forwarded-Host http://foo.com` to
the haproxy configuration.  and then on the nginx ingress configmap you would add `use-forwarded-headers: "true"`

now when the client responds to the request it will respond using http://foo.com 



