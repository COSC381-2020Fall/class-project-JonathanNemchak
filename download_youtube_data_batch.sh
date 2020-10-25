
while read p; do
	touch youtube_data/$p.json
	chmod +rx youtube_data/$p.json
	python3 download_youtube_data.py $p > youtube_data/$p.json

done <video_ids.txt
