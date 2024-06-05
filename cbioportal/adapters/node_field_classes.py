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

# EXAMPLE
# Mutation(alleleSpecificCopyNumber=None, aminoAcidChange=None, center='MSKCC', chr='15', driverFilter=None, driverFilterAnnotation=None, driverTiersFilter=None, driverTiersFilterAnnotation=None, endPosition=30700159, entrezGeneId=101059918, gene=None, keyword='GOLGA8R W275 missense', molecularProfileId='acbc_mskcc_2015_mutations', mutationStatus='SOMATIC', mutationType='Missense_Mutation', namespaceColumns=None, ncbiBuild='GRCh37', normalAltCount=None, normalRefCount=None, patientId='AdCC3T', proteinChange='W275R', proteinPosEnd=275, proteinPosStart=275, referenceAllele='A', refseqMrnaId='NM_001282484.1', sampleId='AdCC3T', startPosition=30700159, studyId='acbc_mskcc_2015', tumorAltCount=20, tumorRefCount=80, uniquePatientKey='QWRDQzNUOmFjYmNfbXNrY2NfMjAxNQ', uniqueSampleKey='QWRDQzNUOmFjYmNfbXNrY2NfMjAxNQ', validationStatus='Unknown', variantAllele='G', variantType='SNP')
class MutationField(Enum):
    ALLELE_SPECIFIC_COPY_NUMBER = "alleleSpecificCopyNumber"
    AMINO_ACID_CHANGE = "aminoAcidChange"
    CENTER = "center"
    CHROMOSOME = "chr"
    DRIVER_FILTER = "driverFilter"
    DRIVER_FILTER_ANNOTATION = "driverFilterAnnotation"
    DRIVER_TIERS_FILTER = "driverTiersFilter"
    DRIVER_TIERS_FILTER_ANNOTATION = "driverTiersFilterAnnotation"
    END_POSITION = "endPosition"
    KEYWORD = "keyword"
    MUTATION_STATUS = "mutationStatus"
    MUTATION_TYPE = "mutationType"
    NAMESPACE_COLUMNS = "namespaceColumns"
    NCBI_BUILD = "ncbiBuild"
    NORMAL_ALT_COUNT = "normalAltCount"
    NORMAL_REF_COUNT = "normalRefCount"
    PROTEIN_CHANGE = "proteinChange"
    PROTEIN_POS_END = "proteinPosEnd"
    PROTEIN_POS_START = "proteinPosStart"
    REFERENCE_ALLELE = "referenceAllele"
    REFSEQ_MRNA_ID = "refseqMrnaId"
    START_POSITION = "startPosition"
    TUMOR_ALT_COUNT = "tumorAltCount"
    TUMOR_REF_COUNT = "tumorRefCount"
    UNIQUE_PATIENT_KEY = "uniquePatientKey"
    UNIQUE_SAMPLE_KEY = "uniqueSampleKey"
    VALIDATION_STATUS = "validationStatus"
    VARIANT_ALLELE = "variantAllele"
    VARIANT_TYPE = "variantType"
    _ID = ["molecularProfileId", "sampleId", "patientId", "entrezGeneId", "studyId"]
    _LABEL = "Mutation"