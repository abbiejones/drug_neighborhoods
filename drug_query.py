import xml.etree.ElementTree as ET
import os.path

smmart_drugs = ["olaparib"];


class Drug:

    def __init__(self, name):
        self.name = name


    def get_neighborhood(self):
        drug_file_path = ('./drug_neighborhoods/' + self.name + '.sbgnml')

        if os.path.isfile(drug_file_path):
            tree = ET.parse(drug_file_path)
            root = tree.getroot()

            for gene in root.findall('./map/glyph[@class="neighbor"]'):
                gene_name = gene.find(".label").attrib

                if gene_name:
                    print((gene_name['text'].replace("'", "")))



def get_smmart_neighborhood():
    for drug in smmart_drugs:
        get_neighborhood(drug)


def get_neighborhood(drug):
    Drug(drug).get_neighborhood()


# def main():
#     get_smmart_neighborhood()
#
# if __name__ == "__main__":
#     main()
