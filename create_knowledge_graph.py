from biocypher import BioCypher, Resource
from cbioportal.adapters.node_field_classes import *
from cbioportal.adapters.edge_field_classes import *
from cbioportal.adapters.cbioportal_adapter import CBioPortalAdapter

# Instantiate the BioCypher interface
# You can use `config/biocypher_config.yaml` to configure the framework or
# supply settings via parameters below
bc = BioCypher()

node_fields = [

    DiseaseField._ID,
    DiseaseField.NAME,
    DiseaseField.SHORTNAME,
    StudyField.NAME,
    StudyField.CITATION,
    StudyField.DESCRIPTION,
    StudyField.IMPORTDATE,
    StudyField._ID,
    StudyField.PMID,
    DiseaseField._LABEL,
    # StudyField._LABEL,
    PatientField._ID,
    PatientField.UNIQUEPATIENTKEY,
    PatientField._LABEL,
    SampleField._ID,
    SampleField.SAMPLETYPE,
    SampleField.UNIQUESAMPLEKEY,

]

edge_fields = [
    DiseaseDiseaseAssociationField._SUBJECT,
    DiseaseDiseaseAssociationField._OBJECT,
    DiseaseDiseaseAssociationField._LABEL,
    StudyDiseaseAssociationField._SUBJECT,
    StudyDiseaseAssociationField._OBJECT,
    StudyDiseaseAssociationField._LABEL,
    studyPatientAssociationField._SUBJECT,
    studyPatientAssociationField._OBJECT,
    studyPatientAssociationField._LABEL,
    samplePatientAssociationField._SUBJECT,
    samplePatientAssociationField._OBJECT,
    samplePatientAssociationField._LABEL


]

# Create a protein adapter instance
adapter = CBioPortalAdapter(
    node_fields = node_fields,
    edge_fields= edge_fields
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
