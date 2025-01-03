import requests
import sys

# Input URL
input_url = "https://www.mxplayer.in/show/watch-hello-mini-telugu-series-online-2cc16384cfea4583f7d1164165de2fdc"

# Handle session input (default to 0 if not provided)
try:
    session_input = int(sys.argv[2]) - 1
except IndexError:
    session_input = 0

# Headers for the request
headers = {
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': 'Android',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2101K7BI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'limit': '20',
}

# Extract the series ID from the input URL
series_id = input_url.split("-")[-1]

# Get season ID details
response = requests.get(
    f"https://api.mxplay.com/v1/web/detail/collection?type=tvshow&id={series_id}", headers=headers
)

# Check if the response is valid
if response.status_code != 200:
    print(f"Failed to retrieve series details. Status code: {response.status_code}")
    sys.exit(1)

get_season_id = response.json()

season_id = get_season_id["tabs"][0]["containers"][session_input]["id"]

# Get episode details
episode_response = requests.get(
    f"https://api.mxplay.com/v1/web/detail/tab/tvshowepisodes?type=season&id={season_id}",
    headers=headers
)

# Check if the episode response is valid
if episode_response.status_code != 200:
    print(f"Failed to retrieve episode details. Status code: {episode_response.status_code}")
    sys.exit(1)

snd_req = episode_response.json()
print(snd_req)

# # Function to check if URL is working
# def check_url(url):
#     try:
#         response = requests.head(url, timeout=5)  # Using HEAD request for faster check
#         if response.status_code == 200:
#             return True
#         else:
#             return False
#     except requests.exceptions.RequestException:
#         return False
#
# # Output file to store the results
# output_file = "output.txt"
#
# # List of bitrates to try
# bitrate_variants = ["64", "96", "128"]
# # Old and new group variants
# group_variants = ["audio_128000_0", "audio_128000_1"]
# new_group_variants = ["h264_high_audio_128000_0", "h264_high_audio_128000_1"]
#
# with open(output_file, "w", encoding="utf-8") as file:
#     for idx, item in enumerate(snd_req["items"], start=1):  # Enumerate to get episode numbers
#         ep_title = item["title"]
#         ep_number = idx
#
#         # Attempt to extract stream_hash safely with detailed logging
#         try:
#             # Check if 'high' exists and is not None
#             if item.get("stream", {}).get("hls", {}).get("high") is not None:
#                 stream_hash = item["stream"]["hls"]["high"].rsplit("/", 1)[0]
#             elif item.get("stream", {}).get("hls", {}).get("base") is not None:
#                 # Fallback to 'base' if 'high' is not available
#                 print(f"Warning: 'high' not found for Episode {ep_number}: {ep_title}, trying 'base'.")
#                 stream_hash = item["stream"]["hls"]["base"].rsplit("/", 1)[0]
#             else:
#                 print(f"Error: No valid stream URL found for Episode {ep_number}: {ep_title}. Skipping episode.")
#                 continue  # Skip this episode if no valid stream is found
#         except (KeyError, IndexError, TypeError) as e:
#             print(f"Error extracting stream_hash for Episode {ep_number}: {ep_title}. Error: {e}. Skipping episode.")
#             continue  # Skip this episode if there is any error extracting the URL
#
#         # Construct the base URL
#         base_url = "https://media-content.akamaized.net/"
#         full_url = None
#
#         # Try old variants first
#         for group in group_variants:
#             for bitrate in bitrate_variants:
#                 variant_url = f"{base_url}{stream_hash}/{group}_{bitrate}.m3u8"
#                 if check_url(variant_url):
#                     full_url = variant_url
#                     break
#             if full_url:
#                 break
#
#         # If old variants fail, try new variants
#         if not full_url:
#             for new_group in new_group_variants:
#                 for bitrate in bitrate_variants:
#                     variant_url = f"{base_url}{stream_hash}/{new_group}_{bitrate}.m3u8"
#                     if check_url(variant_url):
#                         full_url = variant_url
#                         break
#                 if full_url:
#                     break
#
#         if full_url:
#             # Replace the URL with the one having _128.m3u8
#             full_url = full_url.replace("_64.m3u8", "_128.m3u8").replace("_96.m3u8", "_128.m3u8")
#
#             # Format the output
#             output = f"Episode {ep_number}: {ep_title}\nURL: {full_url}\n\n"
#             # Write to file
#             file.write(output)
#         else:
#             print(f"Episode {ep_number}: {ep_title} - All URLs are not working.")
#
# print(f"Data written to {output_file}")
