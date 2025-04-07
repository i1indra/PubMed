# PubMed-GEO Extractor:
A Python script that fetches experiment metadata from the GEO (Gene Expression Omnibus) database using PMIDs (PubMed IDs), leveraging the power of Biopython and NCBI Entrez utilities.

Features
Reads a list of PMIDs from a text file

Links PubMed articles to corresponding GEO datasets

Extracts key metadata fields:

**Title:**

 * Experiment Type
 * Summary
 * Organism
 * Overall Design

Handles XML parsing and basic error checking.
Outputs results to the console
__________________________________________________________________________________________________________________________________________________________________________________________
**Stop Before You Run This:**

Make sure you have Biopython installed.

**You must set your own NCBI Entrez email in the script:**

```Entrez.email = "your_email@example.com"```

Respect NCBI rate limits by keeping delays between requests (time.sleep(0.35) recommended)

Do not overload NCBI with rapid-fire requests — your IP may be temporarily blocked.

Not all PMIDs are guaranteed to be linked to GEO datasets.

**Requirements:**
Python 3.6+
Biopython

**Install dependencies:**

```pip install biopython```

**Input Format**
Save your PMIDs in a plain text file, one per line:

Example: PMIDs_list.txt

```
33785794
30967944
34757009
```

**Usage**

```python geo_extractor.py```

**Sample Output:**
```
--- GEO Record ---
PMID: 33785794
Title: Transcriptomic analysis of XYZ
Experiment Type: Expression profiling by array
Summary: This study investigates ...
Organism: Homo sapiens
Overall Design: Samples collected from ...
```

**License:**
This project is licensed under the MIT License.

**Contributing:**
Contributions, issues, and suggestions are welcome.

