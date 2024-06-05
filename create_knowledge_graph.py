from biocypher import BioCypher, Resource
from cbioportal.adapters.node_field_classes import *
from cbioportal.adapters.edge_field_classes import *
from cbioportal.adapters.cbioportal_adapter import CBioPortalAdapter


# Instantiate the BioCypher interface
# You can use `config/biocypher_config.yaml` to configure the framework or
# supply settings via parameters below
bc = BioCypher()

node_types = [
    MutationField,
    MolecularProfileField,
    # SampleListField,
    # ClinicalAttributesField,
    GeneField,
    # GenePanelField,
    # CancerTypeField,
    StudyField,
    PatientField,
    SampleField,
]
edge_types = [
    # SampleListToStudyField,
    # StudyToClinicalDataField,
    # MolecularProfiletoStudyField,
    # DiseaseDiseaseAssociationField,
    # StudyDiseaseAssociationField,
    # studyPatientAssociationField,
    # samplePatientAssociationField,
    mutationToMolecularProfileField,
    mutationToSampleField,
    mutationToGeneField,
    mutationToStudyField,
    mutationToPatientField

]

# Create a protein adapter instance
adapter = CBioPortalAdapter(
    node_types=node_types,
    edge_types=edge_types,
    limit=None
)


# adapter.get_data_from_api("test")
# quit()
# Create a knowledge graph from the adapter
bc.write_nodes(adapter.get_nodes())
bc.write_edges(adapter.get_edges())

# Write admin import statement
bc.write_import_call()

# Print summary
bc.summary()
