from enum import Enum

class CancerTypeField(Enum):
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

class SampleListField(Enum):
    """
    Define possible fields the adapter can provide for sample lists.
    """
    _ID = "sampleListId"
    _LABEL = "SampleList"
    DESCRIPTION = "description"
    NAME = "name"
    CATEGORY = "category"
    SAMPLE_COUNT = "sampleCount"
    SAMPLE_IDS = "sampleIds"

class GeneField(Enum):
    _ID = "entrezGeneId"
    _LABEL = "Gene"
    HUGO_GENE_SYMBOL = "hugoGeneSymbol"
    TYPE = "type"
    GENETIC_ENTITY_ID = "geneticEntityId"
    
class GenePanelField(Enum):
	_ID = "genePanelId"
	_LABEL = "GenePanel"
	DESCRIPTION = "description"
	# GENES = "genes"

class MolecularProfileField(Enum):
	_ID = "molecularProfileId"
	_LABEL = "MolecularProfile"
	DESCRIPTION = "description"
	DATATYPE = "datatype"
	GENERIC_ASSAY_TYPE = "genericAssayType"
	MOLECULAR_ALTERATION_TYPE = "molecularAlterationType"
	# MOLECULAR_PROFILE_ID = "molecularProfileId"
	NAME = "name"
	PATIENT_LEVEL = "patientLevel"
	PIVOT_THRESHOLD = "pivotThreshold"
	SHOW_PROFILE_IN_ANALYSIS_TAB = "showProfileInAnalysisTab"
	SORT_ORDER = "sortOrder"
	STUDY = "study"
	STUDY_ID = "studyId"
     
class ClinicalAttributesField(Enum):
    _ID = "clinicalAttributeId"
    _LABEL = "ClinicalAttribute"
    DESCRIPTION = "description"
    DATATYPE = "datatype"
    NAME = "displayName"
    PATIENT_ATTRIBUTE = "patientAttribute"
    STUDY_ID = "studyId"
    PRIORITY = "priority"

class ClinicalDataField(Enum):
    CLINICAL_ATTRIBUTE = "clinicalAttribute"
    CLINICAL_ATTRIBUTE_ID = "clinicalAttributeId"
    PATIENT_ATTRIBUTE = "patientAttribute"
    # PATIENT_ID = "patientId"
    # SAMPLE_ID = "sampleId"
    # STUDY_ID = "studyId"
    # UNIQUE_PATIENT_KEY = "uniquePatientKey"
    # UNIQUE_SAMPLE_KEY = "uniqueSampleKey"
    VALUE= "value"
    _ID = "clinicalDataId"
    _LABEL = "ClinicalData"

class CopyNumberSegmentField(Enum):
    CHROMOSOME = "chromosome"
    END = "end"
    NUM_OF_PROBES = "numOfProbes"
    # PATIENT_ID = "patientId"
    # SAMPLE_ID = "sampleId"
    SEGMENT_MEAN = "segmentMean"
    START = "start"
    STUDY_ID = "studyId"
     

class PatientSampleStudyEntityField(Enum):
    """
    Define possible fields the adapter can provide for patient-sample-study entities.
    """
    PATIENT_ID = "patientId"
    SAMPLE_ID = "sampleId"
    STUDY_ID = "studyId"
    _LABEL = "PatientSampleStudyEntity"
    _ID = "id"
