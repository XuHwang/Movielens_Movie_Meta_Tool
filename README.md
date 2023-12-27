# Tool for MovieLens

This is a tool for crawling movie's meta information for MovieLens dataset in TMBD.

## Pre-Requisition

```bash
pip install beautifulsoup4
```

## How to use

```
python spider.py --start 0 --end -1 --output_file ./movies_meta.jsonl --existing_file ./movies_meta.jsonl --multiprocess 1
```

You may need to run the script multiple times to get more data, in case of the 403 forbidden by the server. (Because many requests in a short period would be detected and rejected by the server, aiming to defend the DDos attacks.)

Here, I support the multiprocessing to accelerate. 

```
python spider.py --start 0 --end -1 --output_file ./movies_meta.jsonl --existing_file ./movies_meta.jsonl --multiprocess 10
```

You can set the number of processes as you want if your computer cound stand. 😆

And to filter out duplicated movies, you could use the `filter_unique.py` to count the number of unique movie ids and save those movie ids not found in TMDB.