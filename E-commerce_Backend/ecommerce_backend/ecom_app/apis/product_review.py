from beanie import PydanticObjectId
import logging
from logging.config import dictConfig
from fastapi import APIRouter
from bson import ObjectId
from ecommerce_database.models import productReview
from ecom_app.apis. product_model import Products
from ecommerce.product import add_product_data, get_products_details, get_filter_products
from typing import List
from fastapi import Header
from conf_logger import logging

router = APIRouter()


@router.post('/addproduct', response_description="Review added to the database")
async def add_product(review: Products):

    """create a function to add products """

    logging.debug("Program to add product")

    await add_product_data(review)
    return {'message': 'Review added succesfully'}


@router.get("/productlist", response_description="Review records retrieved")
async def get_products():

    logging.debug("Program to get product")

    """create a function to get products"""

    reviews = await get_products_details()
    return reviews


@router.get("/product/", response_description="Review records retrieved")
async def sort_data(productName: str = None,
                    minAmount: int = None,
                    maxAmount: int = None,
                    sortAmount: int = None) -> Products:

    logging.debug("Program to filter product")

    """create a function to filter product by name and min and max amount"""

    reviews = await get_filter_products(productName, minAmount, maxAmount, sortAmount)
    return reviews
