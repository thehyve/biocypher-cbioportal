from enum import Enum

class DiseaseField(Enum):
    """
    Define possible fields the adapter can provide for diseases.
    """
    _ID = "cancerTypeId"
    NAME = "name"
    SHORTNAME = "shortName"
    _LABEL = "Disease"

class StudyField(Enum):
    """
    Define possible fields the adapter can provide for studies.
    """
    NAME = "name"
    CITATION = "citation"
    DESCRIPTION = "description"
    IMPORTDATE = "importDate"
    _ID = "studyId"
    _LABEL = "Study"
    PMID = "pmid"

class PatientField(Enum):
    """
    Define possible fields the adapter can provide for patients.
    """
    _ID = "patientId"
    _LABEL = "Patient"
    UNIQUEPATIENTKEY = "uniquePatientKey"

class SampleField(Enum):
    """
    Define possible fields the adapter can provide for samples.
    """
    _ID = "sampleId"
    _LABEL = "Sample"
    SAMPLETYPE = "sampleType"
    UNIQUESAMPLEKEY = "uniqueSampleKey"

class GeneField(Enum):
    _ID = "entrezGeneId"
    HUGO_GENE_SYMBOL = "hugoGeneSymbol"
    TYPE = "type"
    GENETIC_ENTITY_ID = "geneticEntityId"
    
class GenePanelField(Enum):
	_ID = "genePanelId"
	_LABEL = "GenePanel"
	DESCRIPTION = "description"
	GENES = "genes"

class MolecularProfileField(Enum):
	_ID = "molecularProfileId"
	_LABEL = "MolecularProfile"
	DESCRIPTION = "description"
	DATATYPE = "dataType"
	GENERIC_ASSAY_TYPE = "genericAssayType"
	MOLECULAR_ALTERATION_TYPE = "molecularAlterationType"
	MOLECULAR_PROFILE_ID = "molecularProfileId"
	NAME = "name"
	PATIENT_LEVEL = "patientLevel"
	PIVOT_THRESHOLD = "pivotThreshold"
	SHOW_PROFILE_IN_ANALYSIS_TAB = "showProfileInAnalysisTab"
	SORT_ORDER = "sortOrder"
	STUDY = "study"
	STUDY_ID = "studyId"