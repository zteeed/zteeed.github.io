---
title: EN - Zip cracking with cracker-ng (w/o fcrackzip/john)
---

> This article might help you to retrieve plaintext passwords from zip
> encrypted files. I disclaim any liability if you use this article for illegal actions.
> If you want to train, you can download the files given in this article.

# Some information about the context

Some weeks ago, I took part in a cybersecurity competition (<a href="https://tracs.viarezo.fr/gallery">Tracs</a>).<br>
My team T35H lost the first place because of a failing implementation of `fcrackzip` and `zip2john`/`john` 

## The challenge

<a href="/images/posts/ZipCracking/problem.png">problem.png</a>
<img class="img_posts" src="/images/posts/ZipCracking/problem.png">


We had to find a password from this picture, the password found is able to decrypt the following encrypted zip file: <a href="/images/posts/ZipCracking/mail.zip">mail.zip</a><br>

So, we generated all the possibilities inside a wordlist that is going to be used to crack the encrypted zip file using a dictionary attack.
Here is the wordlist generator script:

```python
import itertools
import string

alpha = string.ascii_lowercase + string.ascii_uppercase + string.digits
flag = '{}{}Vz8u{}{}6BJ5TA1zJnxsw@#$%^yhgfdabbaaaabab'
flags = [ flag.format(*candidate).encode() for candidate in list(itertools.product(alpha, repeat=4))]

with open('./wordlist.txt', 'wb') as f:
    f.write(b'\n'.join(flags))
```

Then we execute this python code in order to get `wordlist.txt`


## The failing implementations

### fcrackzip

```bash
SECONDS=0 && \
fcrackzip -D -u -v -p ./wordlist.txt ./mail.zip && \
duration=$SECONDS && \
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
```

Result:
```bash
found file 'mail.txt', (size cp/uc    112/   110, flags 9, chk 7de0)
2 minutes and 2 seconds elapsed.
```

`fcrackzip` is slow and did not find the result.

### john / zip2john

```bash
SECONDS=0 && \
zip2john mail.zip > hash.john && \
john --wordlist=wordlist.txt hash.john && \
john hash.john --show && \
duration=$SECONDS && \
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
```

Result:
```bash
ver 2.0 efh 5455 efh 7875 mail.zip/mail.txt PKZIP Encr: 2b chk, TS_chk, cmplen=112, decmplen=110, crc=F3A9E94B
      Regenerating: 1 file(s) changed at 2019-12-29 05:43:58
                    _posts/hash.john
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
                    ...done in 0.233391323 seconds.
                    
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:00 DONE (2019-12-29 05:43) 0g/s 0p/s 0c/s 0C/s
Session completed
0 password hashes cracked, 1 left
0 minutes and 1 seconds elapsed.
```

`john` is really fast but it did not find any result as well.


## What you need to use now


I was looking on <a href="https://github.com/search?l=C%2B%2B&q=zip+cracker&type=Repositories">github</a> for an other compiled tool in order to crack zip files as fast as possible.<br>
I found <a href="https://github.com/BoboTiG/cracker-ng">this project</a> that is a really good one.

Let's try:
```bash
git clone https://github.com/BoboTiG/cracker-ng.git && \
cd cracker-ng && \
make && \
make modules && \
cd .. && \
SECONDS=0 && \
./cracker-ng/bin/zipcracker-ng -f mail.zip -w wordlist.txt && \
duration=$SECONDS && \
echo && \
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
```

Result:
```bash

 ~ ZIP Cracker-ng v2015.02-03 ~
 - File......: mail.zip
 * Chosen one: mail.txt (110 bytes)
 - Encryption: standard (traditional PKWARE)
 - Method....: deflated
 - Generator.: wordlist.txt
 . Worked at ~ 2955K pwd/sec for ~ 14M tries.
 + Password found: QPVz8ubP6BJ5TA1zJnxsw@#$%^yhgfdabbaaaabab
   HEXA[ 51 50 56 7A 38 75 62 50 36 42 4A 35 54 41 31 7A 4A 6E 78 73 77 40 23 24 25 5E 79 68 67 66 64 61 62 62 61 61 61 61 62 61 62 ]
 ^ Ex(c)iting.

0 minutes and 5 seconds elapsed.
```

It works and much faster than `fcrackzip`.<br>
We can unzip the encrypted zip file using the password found:

```bash
unzip -P "QPVz8ubP6BJ5TA1zJnxsw@#\$%^yhgfdabbaaaabab" mail.zip
```

## Conclusion


I have no idea why `fcrackzip` or `john` did not work in that case, you just know that you cannot trust these tools anymore.
