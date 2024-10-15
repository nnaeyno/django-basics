# Django Store Project

## Current Status
⚠️ This project is still under development.

* More features are planned as well as frontend/htmls need major updates
* Code refactoring and optimizations are yet to be completed - querying is bad, method names need to be updated (overall it's messy).
* bonus requirements will be added after the deadline

## Project Overview

This Django project is designed to manage products and their categories in an e-commerce-like setup. <br>
The goal of this project is to provide a basic product management system where products can have multiple categories, and categories can have subcategories (creating a tree structure). 

The project includes functionality for listing products along with their categories and parent categories in JSON format.

## Features

- **Product Management**: 
  - Products can have a name, description, price, image and associated categories.
  - Each product can belong to multiple categories.

- **Category Management**:
  - Categories can be nested (subcategories).
  - Each category can have a parent category, allowing for a tree structure.
  
- **API Endpoints**:
  - Fetch all products and their categories along with parent categories in JSON format.

## Models

### Category Model

The `Category` model represents a category in the product hierarchy. It supports nesting, allowing categories to have subcategories.

- `title`: The name of the category.
- `parent`: A self-referential foreign key to allow subcategories (optional).

### Product Model

The `Product` model represents an item in the store. 

- `name`: The product's name.
- `description`: The product's description.
- `price`: The product's price.
- `categories`: A many-to-many relationship with the `Category` model.
- `product_image`: An optional image field for product images.

## Endpoints

### 1. **List Products with Categories**

- **URL**: `/products/`
- **Method**: GET
- **Description**: Returns a list of all products along with their associated categories and parent categories in JSON format.

### Example Response:
```json
[
    {
    "product_id": 2,
    "name": "Margarita",
    "description": "Pizza margarita",
    "price": "20.00",
    "product_image": "/store/product_images/20220211142754-margherita-9920_5a73220e-4a1a-4d33-b38f-26e98e3cd986.jpg",
    "categories": [
      {
        "category_title": "Pizza",
        "parent_category_title": "Baked",
        "parent_category_id": 6
      }
    ]
  }
]
```

