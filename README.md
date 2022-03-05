# 😲 Streamlit based Deep Emotion Detector 😄 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A simple streamlit based webapp to process text and detect emotions from the underlying text piece built using "EmoRoBERTa" Model from Huggingface Transformers 🤗.

![text](https://user-images.githubusercontent.com/29462447/156898269-e6154cda-4e4c-4113-96c6-dc7fcd25dbf9.gif)
![doc](https://user-images.githubusercontent.com/29462447/156898267-8b33d311-6d11-47f7-8638-c213b9cd30fc.gif)

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Simply run the command: 
```
streamlit run app.py
```
3. Navigate to http://localhost:8501 in your web-browser.
4. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading audio files, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

## Results:
1. Perform emotion detection on random text on the fly!

![text](https://user-images.githubusercontent.com/29462447/156898275-e5ec4c14-845c-4311-9396-b4703537c2ad.png)

2. Upload your document ***(supports PDFs, Word Files, Text files)*** and perform detection of emotions from the underlying text:

![doc_1](https://user-images.githubusercontent.com/29462447/156898297-8dbc6a3a-f6ab-472b-929e-ab6cbcd9bdb8.png)
![doc_2](https://user-images.githubusercontent.com/29462447/156898300-dbc20937-c34b-4fd5-9bfe-2b010e83e6f6.png)


### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
