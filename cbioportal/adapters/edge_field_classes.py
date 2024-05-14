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

class GenePanelGeneAssociationField(Enum):
    """
    Define possible fields the adapter can provide for genePanel-gene associations.
    """
    _SUBJECT = "genePanelId"
    _OBJECT = "genes"
    _LABEL = "hasGene"

class MolecularProfiletoStudyField(Enum):
    """
    Define possible fields the adapter can provide for molecular profile - study associations.
    """
    _SUBJECT = "molecularProfileId"
    _OBJECT = "studyId"
    _LABEL = "hasStudy"

class SampleListToStudyField(Enum):
    """
    Define possible fields the adapter can provide for sample list - study associations.
    """
    _SUBJECT = "sampleListId"
    _OBJECT = "studyId"
    _LABEL = "hasStudy"

class StudyToClinicalDataField(Enum):
    """
    Define possible fields the adapter can provide for study - clinical data associations.
    """
    _SUBJECT = "studyId"
    _OBJECT = "clinicalAttributeId"
    _LABEL = "hasClinicalAttribute"

class CopyNumberSegmentToSampleField(Enum):
    """
    Define possible fields the adapter can provide for copy number segment - sample associations.
    """
    _SUBJECT = "copyNumberSegmentId"
    _OBJECT = "sampleId"
    _LABEL = "fromSample"


class PatientToPatientSampleStudyEntityField(Enum):
    """
    Define possible fields the adapter can provide for patient - patient sample study entity associations.
    """
    _SUBJECT = "patientId"
    _OBJECT = "id"
    _LABEL = "partOf"

class SampleToPatientSampleStudyEntityField(Enum):
    """
    Define possible fields the adapter can provide for sample - patient sample study entity associations.
    """
    _SUBJECT = "sampleId"
    _OBJECT = "id"
    _LABEL = "partOf"

class StudyToPatientSampleStudyEntityField(Enum):
    """
    Define possible fields the adapter can provide for study - patient sample study entity associations.
    """
    _SUBJECT = "studyId"
    _OBJECT = "id"
    _LABEL = "partOf"
