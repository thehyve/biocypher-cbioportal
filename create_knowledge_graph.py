from biocypher import BioCypher, Resource
from cbioportal.adapters.cbioportal_adapter import (
    CBioPortalAdapter,
    DiseaseField,
    DiseaseDiseaseAssociationField
)

# Instantiate the BioCypher interface
# You can use `config/biocypher_config.yaml` to configure the framework or
# supply settings via parameters below
bc = BioCypher()

# Choose protein adapter fields to include in the knowledge graph.
# These are defined in the adapter (`adapter.py`).
node_fields = [
    # Proteins
    # ExampleAdapterProteinField.ID,
    # ExampleAdapterProteinField.SEQUENCE,
    # ExampleAdapterProteinField.DESCRIPTION,
    # ExampleAdapterProteinField.TAXON,
    # Diseases
    DiseaseField._ID,
    DiseaseField.NAME,
    DiseaseField.SHORTNAME,
    DiseaseField.PARENT,
]

edge_fields = [
    DiseaseDiseaseAssociationField._SUBJECT,
    DiseaseDiseaseAssociationField._OBJECT,
    DiseaseDiseaseAssociationField._LABEL


]

# Create a protein adapter instance
adapter = CBioPortalAdapter(
    node_fields = node_fields,
    edge_fields= edge_fields
)


# Create a knowledge graph from the adapter
bc.write_nodes(adapter.get_nodes())
bc.write_edges(adapter.get_edges())

# Write admin import statement
bc.write_import_call()

# Print summary
bc.summary()
