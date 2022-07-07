# Udemy Cryptogoraphy Course

This repo contains notes/excercises and projects undertaken as part of [this udemy course](https://www.udemy.com/course/learn-modern-security-and-cryptography-by-coding-in-python/?utm_source=adwords&utm_medium=udemyads&utm_campaign=DSA_Search_la.EN_cc.AU_PP&utm_term=_._ag_137987504316_._ad_606065560203_._kw__._de_c_._dm__._pl__._ti_dsa-1676636533399_._li_9069116_._pd__._&matchtype=&gclid=EAIaIQobChMI8c-Y-dfj-AIV6Z1LBR2ncQAPEAAYASAAEgJW7vD_BwE).


## [Ceaser Cypher](Ceaser-Cipher/CeaserCipher.py)
The [Ceaser Cypher](https://en.wikipedia.org/wiki/Caesar_cipher) is a pretty basic algorithm that uses a mapping of a character to a character **n** spaces away. There are a few ways to implement using different sets of characters etc. For the example Implementation I've just used the uppercase character set.

### Kerckhoff's Principle
[Kerckhoff's Principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle) is a key principle to consider when applying any cryptographic algorithm. The idea behind it appears to be that for any type of algorithm/cypher it should not be possible to break the algorithm with the knowledge of the algorithm itself. As long as the key is secure the algorithm is secure. For example the Ceaser Cypher goes against this principle. If you are aware of the algorithm, and have an idea on the character set you can simply try to generate a few keys until you find an appropriate message (most will be garbage).
