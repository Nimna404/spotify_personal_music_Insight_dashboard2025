🎧 Algorithmic Mirror: Decoding My Spotify Audio Footprint (2025)

Status: Status: 🚀 Completed
🎯 The Analytical Goal & Project Overview

Spotify's recommendation algorithm claims to know our musical tastes perfectly. But what does that taste actually look like in raw data?

Most music dashboards simply visualize what a user listens to. The objective of this project was to build an analytics engine to investigate why a recommendation algorithm keeps a user engaged. Using an export of my top algorithmic Spotify tracks, I built an end-to-end data pipeline to reverse-engineer my personal "audio footprint." By analyzing metadata such as Danceability, Energy, Valence, and Tempo, I set out to uncover the exact acoustic patterns driving my listening habits and form data-backed hypotheses about user retention strategies.

🛠️ The Tech Stack

Data Extraction: Exportify (Bypassing API rate limits)
Data Cleaning & ETL: Python (Pandas)
Visualization: Microsoft Power BI (DAX, Data Modeling, Custom UI Design)

 📖 The Data Dictionary

The raw dataset includes 24 columns. Key metrics include:

Danceability: How suitable a track is for dancing (0.0 to 1.0).
Energy: Perceptual measure of intensity and activity.
Valence: The musical positiveness conveyed by a track.
Tempo: The overall estimated tempo of a track in beats per minute (BPM).
Popularity: Spotify's algorithmic ranking.

⚙️ Phase 1: Data Engineering (The Pipeline)

Raw exported data is rarely dashboard-ready. I engineered a Python ETL script to process the metadata:

Cleaning: Dropped irrelevant tracking columns to optimize file size.
Imputation: Handled null values in the `Genres` array to prevent blank visuals in the BI interface.
Transformation: Converted `Duration (ms)` to a user-friendly `Duration (mins)` integer, and standardized `Release Date` into datetime formats for accurate time-series modeling.

📊 Phase 2: Dashboard Architecture (Power BI)

I architected a single-page, high-impact dashboard using a custom Spotify Dark-Mode Application Interface (`#1DB954` / `#181818`) focused strictly on algorithmic drivers.

1. The Vibe Matrix (Scatter Plot): Mapped `Valence` against `Energy` to visualize emotional and energetic boundaries. Engineered custom tooltips so data aggregations wouldn't summarize individual tracks.

2. Top N Algorithmic Drivers (Bar Chart): Applied dynamic `Top N` filtering to isolate only the artists who heavily dominate the recommendation loop, eliminating visual clutter.

3. The Heartbeat Mountain (Area Chart): Solved the continuous decimal issue by engineering custom data bins (`Tempo (bins) = 10 BPM`) to group exact tempos into a clean distribution curve.

💡 Key Hypotheses: Decoding the Recommendation Loop

Based on my specific dataset, the algorithm appears to be optimizing for Lifetime Value (LTV) through two distinct behavioral strategies:

Hypothesis 1: The "Anti-Skip" Pocket (Tempo Distribution)
As a DJ and producer, I understand that tempo dictates crowd retention. In my dataset, the algorithm rarely recommends tracks outside the 90-120 BPM window, anchoring heavily on a 100-110 BPM plateau. In audio theory, this mirrors the biological human walking/driving pace. This suggests the algorithm is heavily optimizing my profile for "passive consumption"—keeping me in a mid-tempo zone where psychological friction is lowest, thereby minimizing skip rates and extending session lengths.

Hypothesis 2: Emotional Rubber-Banding (Energy vs. Valence)
The Vibe Matrix reveals that my recommendation engine establishes a strict "energy floor" (refusing to serve tracks with `Energy < 0.4`), ensuring baseline intensity remains high. However, it wildly varies the `Valence` (happiness vs. sadness). This variance suggests a textbook fatigue mitigation strategy. By alternating between dark, moody tracks and highly positive tracks while keeping energy high, the algorithm creates a variable reward schedule, maintaining psychological engagement without causing listener burnout.

🚀 Future Scope (V2)

Because this initial analysis relies on a sample of top algorithmic tracks, future iterations will focus on scaling the dataset to improve statistical significance. I plan to replace Exportify with a direct Python API connection (`Spotipy` library) to fully automate the ETL pipeline and process my lifetime Spotify streaming history (10,000+ records).


📖 [Read the full formatted Case Study and UI breakdown on Notion](https://chestnut-ridge-3be.notion.site/Project-01-Algorithmic-Mirror-Decoding-My-Spotify-Audio-Footprint-2025-326a927116ea8031842fd483ad1aa26c?source=copy_link)) 📖


© 2026 [Nimna D Aluthgamage]. All Rights Reserved.
Data and insights are based on a personal algorithmic footprint and are for portfolio demonstration purposes. Spotify is a trademark of Spotify AB.

