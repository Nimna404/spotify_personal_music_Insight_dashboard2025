<h1 align="center">🎧 Algorithmic Mirror: Decoding My Spotify Audio Footprint</h1>

<p align="left"><b>Status: 🚀 Completed</b></p>

Industry Background & Business Context
Spotify's recommendation algorithm claims to know our musical tastes perfectly. But what does that taste actually look like in raw, quantifiable data? Most commercial music dashboards simply visualize what a user listens to. They act as digital mirrors.

The objective of this project was to go deeper and build an analytics engine to investigate why a recommendation algorithm keeps a user engaged. As a DJ and music producer, I know how to read a room to keep a crowd moving. As a data analyst, I applied that same logic to reverse-engineer my personal "audio footprint." By extracting and modeling metadata such as Danceability, Energy, Valence, and Tempo, I set out to uncover the exact acoustic patterns driving my listening habits and form data-backed hypotheses about Spotify's user retention strategies.

<br>
<h2>🎯 Northstar Objectives:</h2>
<ul>
   <li><b>Reverse-Engineer the Loop:</b> Move beyond basic play-counts to analyze the underlying audio chemistry of algorithmic recommendations.</li>
   <li><b>Behavioral Mapping:</b> Map acoustic features (Energy vs. Valence) to identify psychological fatigue-mitigation strategies.</li>
   <li><b>LTV Optimization Analysis:</b> Determine how the algorithm structures tempo and mood to minimize skip rates, extend session lengths, and ultimately maximize subscriber Lifetime Value (LTV).</li>
</ul>

<br>
<h2>Executive Summary</h2>
<h3><b>1. The Behavioral Strategy: Acoustic Retention Models</b></h3>
<br>
<table align="center" width=100>

<tr>
<td valign="top">
<ul>
<li><strong>1. The "Anti-Skip" Pocket (Tempo Plateau):</strong>


The algorithm rarely recommends tracks outside the 90-120 BPM window, anchoring heavily on a strict 100-110 BPM plateau. It actively ignores genre boundaries to maintain this tempo.</li>


<li><strong>2. Emotional Rubber-Banding (Valence Variance):</strong>


The recommendation engine establishes a strict "energy floor" (refusing to serve tracks with Energy < 0.4). However, it wildly varies the Valence (the mathematical measurement of a track's mood—happiness vs. sadness).</li>
</ul>
</td>
<td valign="top">
<ul>
<li><strong>1. Optimizing for Passive Consumption:</strong>


100-110 BPM physically mirrors the biological human walking and resting heart rate pace. The algorithm is optimizing for "passive consumption"—keeping the listener in a mid-tempo zone where psychological friction is lowest, thereby minimizing skip rates.</li>


<li><strong>2. Fatigue Mitigation:</strong>


By alternating between dark, moody tracks and highly positive tracks while keeping baseline energy consistently high, the algorithm creates a variable reward schedule. This maintains psychological engagement and prevents listener burnout.</li>
</ul>
</td>
</tr>
</table>

<h3><b>2. Technical Architecture & Deep-Dive Visuals</b></h3>
Raw exported data is rarely dashboard-ready. An end-to-end pipeline was engineered to transform messy API outputs into a highly stylized, interactive UI.
<br>
<h2>Dataset Structure & Data Dictionary</h2>
Data was extracted bypassing API rate limits via Exportify, capturing 24 raw columns. Key metrics driving the behavioral analysis include:
<br>
<table>
<thead>
<tr>
<th>Column Name</th>
<th>Data Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Danceability</td>
<td>Float</td>
<td>How suitable a track is for dancing based on musical elements (0.0 to 1.0).</td>
</tr>
<tr>
<td>Energy</td>
<td>Float</td>
<td>Perceptual measure of intensity and activity (0.0 to 1.0). Fast, loud, and noisy tracks score closer to 1.0.</td>
</tr>
<tr>
<td>Valence</td>
<td>Float</td>
<td>The musical positiveness conveyed by a track. High valence sounds happy/cheerful; low valence sounds sad/angry.</td>
</tr>
<tr>
<td>Tempo</td>
<td>Float</td>
<td>The overall estimated tempo of a track in beats per minute (BPM).</td>
</tr>
<tr>
<td>Popularity</td>
<td>Integer</td>
<td>Spotify's algorithmic ranking of the track's current global traction (0 to 100).</td>
</tr>
</tbody>
</table>

<h2>Technical Pipeline & Repository Structure</h2>
<h3>Tools Utilized:</h3>
<ul>
<li><b>Data Extraction:</b> Exportify (Bypassing API rate limits).</li>
<li><b>Python (Data Engineering):</b> <code>pandas</code> (ETL, cleaning, imputation, transformation).</li>
<li><b>Power BI (Visualization):</b> Custom DAX measures, data binning, locked-axis scatter plotting, interactive tooltips, custom dark-mode UI design.</li>
</ul>
<br>
<h2>🚀 Future Scope (V2)</h2>
<p></p>Because this initial analysis relies on a sample of top algorithmic tracks, future iterations will focus on scaling the dataset to improve statistical significance. I plan to replace Exportify with a direct Python API connection (<code>Spotipy</code> library) to fully automate the ETL pipeline and process my lifetime Spotify streaming history (10,000+ records) directly into the model.</p>
<br>
<br>
<br>
<br>

<div align="center">
 

 📖 [Read the full formatted Case Study and UI breakdown on Notion here](https://chestnut-ridge-3be.notion.site/Project-01-Algorithmic-Mirror-Decoding-My-Spotify-Audio-Footprint-2025-326a927116ea8031842fd483ad1aa26c?source=copy_link)) 📖

<br>
© 2026 [Nimna D Aluthgamage]. All Rights Reserved.
Data and insights are based on a personal algorithmic footprint and are for portfolio demonstration purposes. Spotify is a trademark of Spotify AB.
</div>
