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

class mutationToSampleField(Enum):
    """
    Define possible fields the adapter can provide for mutation - sample associations.
    """
    _SUBJECT = ["molecularProfileId", "sampleId", "patientId", "entrezGeneId", "studyId"]
    _OBJECT = "sampleId"
    _LABEL = "fromSample"

class mutationToGeneField(Enum):
    """
    Define possible fields the adapter can provide for mutation - gene associations.
    """
    _SUBJECT = ["molecularProfileId", "sampleId", "patientId", "entrezGeneId", "studyId"]
    _OBJECT = "entrezGeneId"
    _LABEL = "fromGene"

class mutationToStudyField(Enum):
    """
    Define possible fields the adapter can provide for mutation - study associations.
    """
    _SUBJECT = ["molecularProfileId", "sampleId", "patientId", "entrezGeneId", "studyId"]
    _OBJECT = "studyId"
    _LABEL = "hasStudy"

class mutationToPatientField(Enum):
    """
    Define possible fields the adapter can provide for mutation - patient associations.
    """
    _SUBJECT = ["molecularProfileId", "sampleId", "patientId", "entrezGeneId", "studyId"]
    _OBJECT = "patientId"
    _LABEL = "fromPatient"

class mutationToMolecularProfileField(Enum):
    """
    Define possible fields the adapter can provide for mutation - molecular profile associations.
    """
    _SUBJECT = ["molecularProfileId", "sampleId", "patientId", "entrezGeneId", "studyId"]
    _OBJECT = "molecularProfileId"
    _LABEL = "fromMolecularProfile"