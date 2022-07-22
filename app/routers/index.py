from html import entities
from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey
from typing import List
from app.utilities import sken_logger
from app.middlewares.auth_apikey import get_api_key
from app.services.recoganizer_service.base_recoganizer_implementation import Anomizer
from app.services.recoganizer_service.number_recoganizer_implementation import NumbersRecognizer
from app.services.recoganizer_service.title_recoganizer_implementation import TitleRecoganizer
from app.services.recoganizer_service.adhar_recoganizer_implementation import AdharRecoganizer
from app.services.recoganizer_service.indian_names_recoganizer_implementation import NameRecoganizer
from app.services.entity_service import Entity

entities = Entity()

adhar_obj = AdharRecoganizer(supported_entity="AADHAAR")
title_obj = TitleRecoganizer(supported_entity="TITLE")
indian_names_obj = NameRecoganizer(supported_entity = "INDIAN_NAME")
adhar_recoganizer = adhar_obj.load()
title_recoganizer = title_obj.load()
indian_names_recoganizer = indian_names_obj.load()
number_recoganizer = NumbersRecognizer(supported_entities=["NUMBER"])

anomyzer = Anomizer([adhar_recoganizer,title_recoganizer,indian_names_recoganizer,number_recoganizer])
anomyzer.initialize()


router = APIRouter(
    tags=["Inference"],
    responses={404: {"description": "Not found"}},
)

@router.post("/anonymize_sentences")
def anonymize(sentences: List[str]):
    return anomyzer.batch_anonymize(sentences,entities.get_current_entites())

@router.get("/supported_entities")
async def get_all_entities():
    """This end point gives the list of all the supported entities.
    author: andy
    Returns:
        Dict: ["Supported entities": List[supported entities]]
    """
    return {"Supported Entities": entities.get_supported_entities()}

@router.get("/current_entities")
async def get_current_entities():
    """This end 

    Returns:
        _type_: _description_
    """
    return {"Current Entities": entities.get_current_entites()}

@router.get("/add_entities")
async def add_entities(entity:str):
    """Check the health of services
    author: andy
    Returns:
        [json]: json object with a status code 200 if everything is working fine else 400.
    """
    resp = entities.add_entity(entity)
    if resp:
        return {"message": f"Entity={entity} has been added to the current entity list", "status":200}
    else:
        return {"message": f"Entity={entity} could not be added as it is either present in the current list or is not a supported entity", "status":512}


@router.get("/remove_entities")
async def remove_entities(entity:str):
    """Check the health of services
    author: andy
    Returns:
        [json]: json object with a status code 200 if everything is working fine else 400.
    """
    resp = entities.remove_entity(entity)
    if resp:
        return {"message": f"Entity={entity} has been removed from the current entity list", "status":200}
    else:
        return {"message": f"Entity={entity} could not be removed as it is not present in the current list", "status":512}



