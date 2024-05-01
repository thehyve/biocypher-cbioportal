import random
import string
from enum import Enum, auto
from itertools import chain
from typing import Optional
from biocypher._logger import logger
from bravado.client import SwaggerClient

logger.debug(f"Loading module {__name__}.")

class DiseaseField(Enum):
    """
    Define possible fields the adapter can provide for diseases.
    """

    _ID = "cancerTypeId"
    NAME = "name"
    SHORTNAME = "shortName"
    PARENT = "parent"
    _LABEL = "Disease"


class DiseaseDiseaseAssociationField(Enum):
    """
    Define possible fields the adapter can provide for disease-disease associations.
    """
    _SUBJECT = "cancerTypeId"
    _OBJECT = "parent"
    _LABEL = "DiseaseDiseaseAssociation"


class CBioPortalAdapter:
    """
    Example BioCypher adapter. Generates nodes and edges for creating a
    knowledge graph.

    Args:
        node_types: List of node types to include in the result.
        node_fields: List of node fields to include in the result.
        edge_types: List of edge types to include in the result.
        edge_fields: List of edge fields to include in the result.
    """

    def __init__(
        self,
        node_fields: Optional[list] = None,
        edge_fields: Optional[list] = None,
    ):
        self._init_api()
        self.node_fields = node_fields
        self.edge_fields = edge_fields

    def _init_api(self):
        self.cbioportal = SwaggerClient.from_url('https://www.cbioportal.org/api/v2/api-docs',
                                    config={"validate_requests":False,"validate_responses":False,"validate_swagger_spec": False})
    


    def get_data_from_api(self, _type):
        
        # get cancer types
        if _type in [DiseaseField, DiseaseDiseaseAssociationField]:
            return self.cbioportal.Cancer_Types.getAllCancerTypesUsingGET().result()
        else:
            raise ValueError(f"Node type {_type} not supported.")


    def _yield_node_type(self, items, node_type):
        for item in items:
            _id = item[node_type._ID.value]
            _type = node_type._LABEL.value
            _props = {}
            for field in node_type:
                if field not in self.node_fields:
                    continue
                if field in [node_type._ID, node_type._LABEL]:
                    continue
                else:
                    _props[field.value] = item[field.value]
            yield (_id, _type, _props)

    def get_nodes(self):
        """
        Returns a generator of node tuples for node types specified in the
        adapter constructor.
        """

        logger.info("Generating nodes.")

        yield from self._yield_node_type(self.get_data_from_api(DiseaseField), DiseaseField)


    def _yield_edge_type(self, items, edge_type):
        for item in items:
            _subject = item[edge_type._SUBJECT.value]
            _object = item[edge_type._OBJECT.value]

            try:
                item[edge_type._ID.value]
            except AttributeError:
                _id = str(hash((_subject, _object)))

            _type = edge_type._LABEL.value
            _props = {}
            for field in edge_type:
                if field not in self.edge_fields:
                    continue

                try:
                    if field in [edge_type._ID, edge_type._SUBJECT, edge_type._OBJECT]:
                        continue
                except AttributeError:
                    continue
                else:
                    _props[field.value] = item[field.value]
            yield (_id, _subject, _object,_type, _props)

    def get_edges(self):
        """
        Returns a generator of edge tuples for edge types specified in the
        adapter constructor.

        Args:
            probability: Probability of generating an edge between two nodes.
        """

        logger.info("Generating edges.")

        yield from self._yield_edge_type(self.get_data_from_api(DiseaseDiseaseAssociationField), DiseaseDiseaseAssociationField)

    def get_node_count(self):
        """
        Returns the number of nodes generated by the adapter.
        """
        return len(list(self.get_nodes()))
