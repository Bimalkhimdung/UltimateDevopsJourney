import os
import logging
from django.shortcuts import render
from .forms import YouTubeDownloadsForm
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.http import StreamingHttpResponse, JsonResponse
import time
import json
import threading
from yt_dlp import *



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

progress_data = {"progress": 0}
def get_download_path():
    """Downloads files at Current Directory."""
    #return os.getcwd()  
    """Downloads files at Downloads Directory"""
    return os.path.join(os.path.expanduser("~"), "Downloads")

def download_video(request):

    def download_progress(d):
     global progress_data
     if d['status'] == 'downloading':
         progress_data["progress"] = d['_percent_str']

def stream_progress():
    """Streaming function for real-time progress updates."""
    def event_stream():
        while True:
            time.sleep(1)
            yield f"data: {json.dumps(progress_data)}\n\n"

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")
def download_video(request):
    """Handles video download."""
    global progress_data
    url = request.POST.get('url')

    if not url:
        return render(request, 'download.html', {'error': 'URL is required'})

    options = {
        'progress_hooks': [download_progress],
        'outtmpl': os.path.join(get_download_path(), '%(title)s.%(ext)s'),
    }

    def run_download():
        with YoutubeDL(options) as ydl:
            ydl.download([url])

    threading.Thread(target=run_download).start()

    return render(request, 'downloader/index.html', {'message': 'Download started!'})

    # global progress_data
    # print(f"Request method: {request.method}")
    # if request.method == "GET":
        # form = YouTubeDownloadsForm()
        # return render(request, "downloader/index.html", {"form": form})    
    # if request.method == "POST":
        # form = YouTubeDownloadsForm(request.POST)
        # if form.is_valid():
            # url = form.cleaned_data["url"]
            # logger.debug(f"Received URL for download: {url}")
# 
            # def progress_hook(d):
                # """Update the progress dictionary with download status"""
                # if d['status'] == 'downloading':
                    # progress_data['progress'] = d['_percent_str']
                    # progress_data['speed'] = d['_speed_str']
                    # progress_data['eta'] = d['_eta_str']
# 
            # ydl_opts = {
                # 'outtmpl': os.path.join(get_download_path(), '%(title)s.%(ext)s'),
                # 'progress_hooks': [progress_hook],  # Attach progress hook
            # }
# 
            # def stream_response():
                # """Yields progress updates as streaming HTTP response"""
                # global progress_data
                # with YoutubeDL(ydl_opts) as ydl:
                    # ydl.download([url])
                    # progress_data = {}  # Reset after download
# 
            # threading.Thread(target=stream_response).start()
# 
            # return JsonResponse({"status": "Downloading started"}, status=200)
    # 
    # return JsonResponse({"error": "Invalid request"}, status=400)
def download_progress(request):
    """API endpoint to fetch progress updates"""
    global progress_data
    return JsonResponse(progress_data)

def custom_404_view(request, exception):
    logger.warning("404 error: Page not found")
    return HttpResponseNotFound("<h1>404 - Page Not Found</h1>")

def custom_500_view(request):
    logger.error("500 error: Internal Server Error")
    return HttpResponseServerError("<h1>500 - Internal Server Error</h1>")


