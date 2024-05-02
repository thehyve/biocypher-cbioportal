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