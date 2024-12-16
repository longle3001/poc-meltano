quy trình run 

```
meltano init
meltano add --custom extractor tap-jsonplaceholder
-->
namespace: tap-jsonplaceholder
pip_url: -e ../tap-jsonplaceholder

meltano add loader target-jsonl
meltano run tap-jsonplaceholder target-jsonl

chekc result
head -n 5 output/comments.jsonl
```