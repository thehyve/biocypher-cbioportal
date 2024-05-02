from enum import Enum


class DiseaseDiseaseAssociationField(Enum):
    """
    Define possible fields the adapter can provide for disease-disease associations.
    """
    _SUBJECT = "cancerTypeId"
    _OBJECT = "parent"
    _LABEL = "isChildOf"


class StudyDiseaseAssociationField(Enum):
    """
    Define possible fields the adapter can provide for study-disease associations.
    """
    _SUBJECT = "studyId"
    _OBJECT = "cancerTypeId"
    _LABEL = "StudyDiseaseAssociation"

class studyPatientAssociationField(Enum):
    """
    Define possible fields the adapter can provide for study-patient associations.
    """
    _SUBJECT = "studyId"
    _OBJECT = "patientId"
    _LABEL = "hasPatient"


class samplePatientAssociationField(Enum):
    """
    Define possible fields the adapter can provide for sample-patient associations.
    """
    _SUBJECT = "sampleId"
    _OBJECT = "patientId"
    _LABEL = "fromPatient"