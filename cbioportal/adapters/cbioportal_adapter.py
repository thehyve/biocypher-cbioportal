from typing import Optional
from biocypher._logger import logger
from bravado.client import SwaggerClient
from bravado.exception import HTTPNotFound, HTTPBadRequest
from cbioportal.adapters.node_field_classes import *
from cbioportal.adapters.edge_field_classes import *

logger.debug(f"Loading module {__name__}.")



class CBioPortalAdapter:
    """
    Example BioCypher adapter. Generates nodes and edges for creating a
    knowledge graph.

    Args:
        node_types: List of node types to include in the result.
        edge_types: List of edge types to include in the result.
        limit_nodes: Maximum number of nodes to generate.
        limit_edges: Maximum number of edges to generate.
    """

    def __init__(
        self,
        node_types: Optional[list] = None,
        edge_types: Optional[list] = None,
        limit= None
    ):
        self._init_api()
        self.node_types = node_types
        self.edge_types = edge_types
        self.version = self.cbioportal.Info.getInfoUsingGET().result().dbVersion
        self.api_called = {}
        self.limit = limit

    def _init_api(self):
        self.cbioportal = SwaggerClient.from_url('https://www.cbioportal.org/api/v2/api-docs',
                                    config={"validate_requests":False,"validate_responses":False,"validate_swagger_spec": False})
    

    def check_api_called(self, field):
        if field in self.api_called:
            return self.api_called[field]
        else:
            return self.get_data_from_api(field)    

    def get_data_from_api(self, _type):
        # get cancer types
        if _type in [CancerTypeField, DiseaseDiseaseAssociationField]:
            if "cancer_types" in self.api_called: return self.api_called["cancer_types"]
            self.api_called["cancer_types"] = self.cbioportal.Cancer_Types.getAllCancerTypesUsingGET().result()[0:self.limit]
            return self.api_called["cancer_types"]
        if _type in [StudyField, StudyDiseaseAssociationField]:
            if "studies" in self.api_called: return self.api_called["studies"]
            self.api_called["studies"] = self.cbioportal.Studies.getAllStudiesUsingGET().result()[0:self.limit]
            return self.api_called["studies"]
        if _type in [PatientField, studyPatientAssociationField]:
            if "patients" in self.api_called: return self.api_called["patients"]
            self.api_called["patients"] = self.cbioportal.Patients.getAllPatientsUsingGET().result()[0:self.limit]
            return self.api_called["patients"]
        if _type in [SampleField, samplePatientAssociationField]:
            if "samples" in self.api_called: return self.api_called["samples"]
            self.api_called["samples"] = []
            # studies = self.cbioportal.Studies.getAllStudiesUsingGET().result()
            studies = self.check_api_called(StudyField)
            print(f"Getting samples of {len(studies)} studies")
            for i, study in enumerate(studies):
                study_samples = self.cbioportal.Samples.getAllSamplesInStudyUsingGET(studyId=study.studyId).result()[0:self.limit]
                print(f"Study {i+1}/{len(studies)}: {len(study_samples)} samples")
                for sample in study_samples:
                        self.api_called["samples"].append(sample)
            return self.api_called["samples"]
        if _type in [SampleListField, SampleListToStudyField]:
            if "sample_lists" in self.api_called: return self.api_called["sample_lists"]
            self.api_called["sample_lists"] = self.cbioportal.Sample_Lists.getAllSampleListsUsingGET().result()[0:self.limit]
            return self.api_called["sample_lists"]
        
        if _type == GeneField:
            if "genes" in self.api_called: return self.api_called["genes"]
            self.api_called["genes"] = self.cbioportal.Genes.getAllGenesUsingGET().result()[0:self.limit]
            return self.api_called["genes"]
        if _type in [GenePanelField, GenePanelGeneAssociationField]:
            if "gene_panels" in self.api_called: return self.api_called["gene_panels"]
            self.api_called["gene_panels"] = self.cbioportal.Gene_Panels.getAllGenePanelsUsingGET().result()[0:self.limit]
            return self.api_called["gene_panels"]
        if _type in [MolecularProfileField, MolecularProfiletoStudyField]:
            if "molecular_profiles" in self.api_called: return self.api_called["molecular_profiles"]
            self.api_called["molecular_profiles"] = self.cbioportal.Molecular_Profiles.getAllMolecularProfilesUsingGET().result()[0:self.limit]
            return self.api_called["molecular_profiles"]
        if _type in [ClinicalAttributesField, StudyToClinicalDataField]:
            if "clinical_attributes" in self.api_called: return self.api_called["clinical_attributes"]
            self.api_called["clinical_attributes"] = self.cbioportal.Clinical_Attributes.getAllClinicalAttributesUsingGET().result()[0:self.limit]
            return self.api_called["clinical_attributes"]
        if _type in [PatientSampleStudyEntityField, PatientToPatientSampleStudyEntityField, SampleToPatientSampleStudyEntityField, StudyToPatientSampleStudyEntityField]:
            print("not correctly implemeted yet!")
            return []

            if "patient_sample_study_entities" in self.api_called: return self.api_called["patient_sample_study_entities"]
            patients = self.check_api_called(PatientField)
            samples = self.check_api_called(SampleField)
            studies = self.check_api_called(StudyField)
            self.api_called["patient_sample_study_entities"] = []
            counter = 0
            for _id1 in patients:
                for _id2 in samples:
                    for _id3 in studies:
                        id = hash(f"{_id1.patientId}_{_id2.sampleId}_{_id3.studyId}")
                        self.api_called["patient_sample_study_entities"].append({"patientId":_id1.patientId, "sampleId":_id2.sampleId, "studyId":_id3.studyId, "id":id})
                        counter += 1
                        if counter == self.limit:
                            return self.api_called["patient_sample_study_entities"]
            return self.api_called["patient_sample_study_entities"]
        
        if _type == "test":
            print(dir(self.cbioportal))
            gene_panels = self.cbioportal.Gene_Panels.getAllGenePanelsUsingGET().result()
            print(gene_panels[0])
        else:
            raise ValueError(f"Node type {_type} not supported.")

    def _yield_node_type(self, items, node_type):
        for item in items:
            _id = item[node_type._ID.value]
            _type = node_type._LABEL.value
            _props = {"version": self.version}
            for field in node_type:
                if field in [node_type._ID, node_type._LABEL]:
                    continue
                else:
                    _props[field.value] = item[field.value]

            # if _id is a int, convert it to a string
            if isinstance(_id, int):
                _id = str(_id)

            yield (_id, _type, _props)

    def get_nodes(self):
        """
        Returns a generator of node tuples for node types specified in the
        adapter constructor.
        """
        logger.info("Generating nodes.")
        self.nodes = {}
        for _type in self.node_types:
        # for _type, node in self.nodes.items():
            print("Generating nodes for ", _type)
            self.nodes[_type] = self.get_data_from_api(_type)
            yield from self._yield_node_type(self.nodes[_type], _type)

    def _yield_edge_type(self, items, edge_type):
        for item in items:
            _subject = item[edge_type._SUBJECT.value]
            _object = item[edge_type._OBJECT.value]

            try:
                item[edge_type._ID.value]
            except AttributeError:
                _id = str(hash((_subject, _object)))

            _type = edge_type._LABEL.value
            _props = {"version": self.version}
            for field in edge_type:
                try:
                    if field in [edge_type._ID, edge_type._SUBJECT, edge_type._OBJECT]:
                        continue
                except AttributeError:
                    continue
                else:
                    _props[field.value] = item[field.value]
                        # if _id is a int, convert it to a string
            if isinstance(_id, int):
                _id = str(_id)
            if isinstance(_subject, int):
                _subject = str(_subject)
            if isinstance(_object, int):
                _object = str(_object)
            yield (_id, _subject, _object,_type, _props)

    def get_edges(self):
        """
        Returns a generator of edge tuples for edge types specified in the
        adapter constructor.

        Args:
            probability: Probability of generating an edge between two nodes.
        """
        logger.info("Generating edges.")
        self.edges = {}
        for _type in self.edge_types:
            print("Generating edges for ", _type)
            self.edges[_type] = self.get_data_from_api(_type)
            yield from self._yield_edge_type(self.edges[_type], _type)

    def get_node_count(self):
        """
        Returns the number of nodes generated by the adapter.
        """
        return len(list(self.get_nodes()))

