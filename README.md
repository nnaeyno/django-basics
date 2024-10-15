# Django Store Project

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

## Current Status
⚠️ This project is still under development.

* More features are planned, such as authentication, more API endpoints, and user management.
* Code refactoring and optimizations are yet to be completed.




კატეგორიების ლისტინგის გვერდი(/category/)
უნდა გამოჩნდეს ყველა კატეგორია, რომელსაც არ ყავს მშოველი კატეგორია (ანუ ყველაზე მაღალი დონე კატეგორიების ხეში.
კატეგორიის გამოჩენაში იგულისხმება მისი დასახელების გამოტანა
დასახელების გვერდით ყველა კატეგორიას მიუწერეთ მის ქვევით(ასევე საბკატეგორიებში) არსებული პროდქტების რაოდენობა
თითოეულ კატეგორიის გვერდზე დაკლიკებისას უნდა გადავდიოდეთ კატეგორიის დეტალურ გვერდზე ანუ პროდუქტების ლისტინგზე
კატეგორიის პროდუქტების ლისტინგის გვერდი(/category/{category_id}/products/)
ამ გვერდზე უნდა გამოვიტანოთ იმ პროდუქტების დასახელებების ჩამონათვალი რომლებიც მოქცეულია კონკრეტულ კატეგორიაში(არჩეული კატეგორია უშუალოდ მიმაგრებულია პროდუქტს ან მისი შთამომავალი კატეგორია არის მიმაგრებული პროდუქტს)
ყველა დასახელების გვერდით გამოვიტანოთ მარაგში არსებული ამ პროდუქტის საერთო ჯამური ღირებულება(Product ის მოდელს უნდა ქონდეს quantity და price ველები)
ასევე ამ გვერდზე უნდა გამოვიტანოთ შემდეგი სტატისტიკა:
ყველაზე ძვირიანი პროდუქტის ფასი
ყველაზე იაფიანი პროდუქტის ფასი
პროდუქტის საშუალო ფასი
კატეგორიაშია არსებული ყველა პროდუქტის ჯამური ღირებულება(გაითვალისწინეთ რაოდენობებიც)
პროდუქტის დასახელებაზე დაკლიკების შემდეგ უნდა გვამისმართებს პროდუქტის დეტალურ ფეიჯზე
გააკეთეთ პაგინაცია(ყველა პროდუქტი ერთ გვერდზე რომ არ ჩანდეს)
პროდუქტის დეტალური გვერდი
ამ გვერდზე უნდა გამოვაჩინოთ ყველა ველი რომელიც გააჩნია პროდუქტს, მათ შორის სურათიც


წითლად მონიშნული სექციები არასავალდებულოა და წარმოადგენს შედარებით რთულ დავალებებს
მარტივი ქვერების საწერად ჯერ ცალკე იპოვეთ მშობელი კატეგორიის შთამომავალი კატეგორიის აიდები და შემდეგ მარტივად დაწერთ სხვა ქვერისეტებს
პაგინაციის გაკეთების ინსტრუქცია: https://chatgpt.com/share/67090ff8-9e48-8009-8daf-3a9f066b7e1a