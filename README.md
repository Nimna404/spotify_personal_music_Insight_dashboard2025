🎧 Algorithmic Mirror: Decoding My Spotify Audio Footprint (2025)

Status: 🚧 Currently in Development (ETL Phase)

Project Overview

Spotify's recommendation algorithm claims to know our musical tastes perfectly. But what does that taste actually look like in raw data? Using an export of my top algorithmic Spotify tracks, this project reverse-engineers my personal "audio footprint." By analyzing metadata such as Danceability, Energy, Valence, and Tempo, I am building an end-to-end data pipeline to uncover the acoustic patterns that drive my listening habits.

The Tech Stack

Data Extraction: Exportify (Bypassing API rate limits)
Data Cleaning & ETL: Python (Pandas) accelerated via Generative AI and Prompt Engineering
Visualization: Microsoft Power BI (DAX, Data Modeling)

The Data Dictionary
The raw dataset includes 24 columns. Key metrics include:
                                                         Danceability: How suitable a track is for dancing (0.0 to 1.0).
                                                         Energy: Perceptual measure of intensity and activity.
                                                         Valence: The musical positiveness conveyed by a track.
                                                         Popularity: Spotify's algorithmic ranking.
