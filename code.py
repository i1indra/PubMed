from Bio import Entrez
import xml.etree.ElementTree as ET



Entrez.email = "your_email@example.com"
pmid_file_path = "/home/crossfire/Downloads/PMIDs_list.txt"


with open(pmid_file_path, "r") as f:
    pmid_list = [line.strip() for line in f if line.strip()]



def fetch(pmid_list):
    results = []
    for pmid in pmid_list:
        link_handle = Entrez.elink(dbfrom="pubmed", db="gds", id=pmid)
        links = Entrez.read(link_handle)
        link_handle.close()

        geo_ids = []

        for linkset in links:
            for link in linkset.get("LinkSetDb", []):
                if link["DbTo"] == "gds":
                    geo_ids += [l["Id"] for l in link["Link"]]

        if not geo_ids:
            print("No GEO dataset found for PMID {}".format(pmid))
            continue

        gds_id = geo_ids[0]

        try:
            gds_handle = Entrez.efetch(db="gds", id=gds_id, rettype="xml")
            gds_data = gds_handle.read()
            gds_handle.close()

            if not gds_data.strip().startswith("<?xml"):
                print(f"Warning: Unexpected data for GEO ID {gds_id}")
                print(gds_data[:500])
                continue

        except Exception as e:
            print(f"Error fetching GEO ID {gds_id}: {e}")
            continue

        # try:
        #     root = ET.fromstring(gds_data)
        # except ET.ParseError as e:
        #     print(f"XML Parse Error for GEO ID {gds_id}: {e}")
        #     print(gds_data[:500])
        #     continue

        root = ET.fromstring(gds_data)
        title = experiment_type = summary = organism = overall_design = "N/A"

        for docsum in root.findall("DocSum"):
            for item in docsum.findall("Item"):
                name = item.attrib.get("Name")
                if name == "title":
                    title = item.text
                elif name == "gdsType":
                    experiment_type = item.text
                elif name == "summary":
                    summary = item.text
                elif name == "organism":
                    organism = item.text
                elif name == "overall_design":
                    overall_design = item.text
        results.append({
                    "PMID": pmid,
                    "Title": title,
                    "Experiment Type": experiment_type,
                    "Summary": summary,
                    "Organism": organism,
                    "Overall Design": overall_design
                })

        return results



fetch(pmid_list)