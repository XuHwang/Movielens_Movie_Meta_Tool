import json
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--link_file", type=str)
parser.add_argument("--meta_file", type=str)
parser.add_argument("--unique_meta_file", type=str)
parser.add_argument("--not_found_file", type=str)
args = parser.parse_args()

movie_id_df = pd.read_csv(args.link_file, header=0)[['movieId', 'tmdbId']]
movie_id_df = movie_id_df.fillna(-1)
movie_id_df = movie_id_df.astype(int)

all_id = set(movie_id_df['movieId'].tolist())

existing_movie_id = set([])
contents = []
with open(args.meta_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        c = json.loads(line)
        if c['movieID'] not in existing_movie_id:
            contents.append(c)
            existing_movie_id.add(c['movieID'])

with open(args.unique_meta_file, 'w') as f:
    for content in contents:
        json.dump(content, f)
        f.write("\n")
    
non_id = all_id.difference(existing_movie_id)

with open(args.not_found_file, 'w') as f:
    for id in non_id:
        f.write(f"{id}\n")

print(f"Those movie id not found in file: {non_id}")
print(f"Total movies: {len(contents)} / {len(all_id)}")