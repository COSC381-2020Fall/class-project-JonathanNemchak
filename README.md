# config.py
you need to add api key and cse id key before anything will work

# google search results
step1: python3 cse.py

# youtube data
step1: wget https:github.com/COSC381-2020Fall/course_project/raw/master/google_search.txt
step2: grep "link" google_search.txt | awk -F "=" '{print substr($2,1,11)}' > video_ids.txt
step3: python3 download_youtube_data.py E1gtWNHJ4h8
step4: bash donwload_youtube_data_batch.sh > youtube_data.txt
step5: grep " 'description':" youtube_data.txt
step6: grep " 'description':" youtube_data.txt | wc -l

# whoosh indexing


# whoosh indexing and does a test query
step1: python3 create_whoosh_index.py

# Query on whoosh
step1: run 'python3 query_on_whoosh.py home 2 1' will output a json-format result
