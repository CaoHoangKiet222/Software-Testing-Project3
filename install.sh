# install packages for virtual enviroment
python3 -m venv venv && \
  source ./venv/bin/activate && \
  pip install --upgrade pip && \
  pip3 install -r ./packages.txt

# run docker for moodle
docker compose up -d
