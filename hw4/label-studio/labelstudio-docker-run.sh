docker volume create labelstudio-data
docker run -d \
  --name label-studio \
  -p 8080:8080 \
  -v labelstudio_data:/label-studio/data \
  heartexlabs/label-studio:latest
